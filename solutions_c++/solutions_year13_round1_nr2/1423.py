#include <cstring>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

class Network{
public:
     static const int SIZE = 1005;       // ������
    static const int INF = 1000000007;  // �����ļ���ֵ
    typedef long long int VAL;    // ���õ�����
	typedef struct ARC{int t,c; VAL w; ARC* o;ARC() {} ARC(int _t, int _c, VAL _w, ARC* _o):t(_t), c(_c), w(_w), o(_o) {}}* PTR;
     ARC arc[200005];    // ��������ע��һ����ͨ�ӱ߲�����Ҫռ��������
    PTR now[SIZE],e[SIZE];              // now[]Ϊ��ǰ����e[]Ϊ��������
    int cnt[SIZE],l[SIZE],r[SIZE],edge; // cnt[]Ϊ��������l[]Ϊ��α��
    VAL sum;   // sumΪ��ǰ�������µķ���
    // ����Դ��S�ͻ��T���������������������ʱ������ĳ�spfa_johnson
     int flow(int S, int T){return spfa_johnson(S,T,INF);}
     ARC& REV(PTR x){return arc[(x-arc)^1];}                 // ȡ�����
    void clear(){memset(e,edge=sum=0,sizeof(e));}           // ��ձ߱�
    // ����һ��x��y������ߣ�����Ϊc������Ϊw
     PTR add_edge(int x, int y, int c, VAL w = 0){
         e[x]=&(arc[edge++]=ARC(y,c,+w,e[x]));
         e[y]=&(arc[edge++]=ARC(x,0,-w,e[y]));
         return e[x];
     }
     // ����һ��x��y������ߣ�����Ϊc������Ϊ0
     PTR add_edge_simple(int x, int y, int c){
         e[x]=&(arc[edge++]=ARC(y,c,0,e[x]));
         e[y]=&(arc[edge++]=ARC(x,c,0,e[y]));
         return e[x];
     }
     // ����һ��x��y������ߣ��½�Ϊlo���Ͻ�Ϊhi������Ϊw
     // ����Դ��SIZE-2����������SIZE-1��ע�����������Ԥ���ռ�
    PTR add_edge_bounded(int x, int y, int lo, int hi, VAL w = 0){
         add_edge(SIZE-2,y,lo,w);
         add_edge(x,SIZE-1,lo,0);
         return add_edge(x,y,hi-lo,w);
     }
     // ��S��T�ҳ���Ϊnow[]������·�����ɳڣ����ر������Ľ��
    int aug(int S, int T, int& can){
         int x,z=T,use=can;
         for(x=S;x!=T;x=now[x]->t) if(use>now[x]->c) use=now[z=x]->c;
         for(x=S;x!=T;x=now[x]->t){
                 now[x]->c-=use;
             REV(now[x]).c+=use;
             sum+=use*now[x]->w;
         }
         can-=use;
         return z;
     }
     // ��Ȩֵ���·�����㷨�������޷��õ��������ϣ���������
    int improved_sap(int S, int T, int can){
         if(S==T) return can; // canΪ�����������������
        int in=can,x,m;
         memcpy(now,e,sizeof(now));
         memset(cnt,0,sizeof(cnt));
         memset(l,127,sizeof(l));
         for(int i=m=l[r[0]=T]=0;i<=m;i++){
             cnt[l[x=r[i]]]++;
             for(PTR u=e[x];u;u=u->o)
                 if(l[u->t]>=INF && REV(u).c) l[r[++m]=u->t]=l[x]+1;
         }
         for(x=r[S]=S;l[S]<INF;x=r[x]){
         JMP:for(PTR& u=now[x];u;u=u->o) if(l[u->t]<l[x] && u->c){
                 r[u->t]=x;
                 x=u->t==T?aug(S,T,can):u->t;
                 if(x==T) return in; else goto JMP;
             }
             if(!--cnt[l[x]]) break; else l[x]=INF;
             for(PTR u=e[x];u;u=u->o)
                 if(l[u->t]+1<l[x] && u->c) now[x]=u,l[x]=l[u->t]+1;
             if(l[x]<INF) cnt[l[x]]++;
         }
         return in-can;
     }
     // �������·�����㷨�����Դ�����������Ȧ�ķ���������������
    int spfa_johnson(int S, int T, int can){
         if(S==T) return can; // canΪ�����������������
        int in=can,x,m;
         VAL phi[SIZE],len[SIZE],MAXW=1000000007; // ���ü���ֵ
        fill_n(phi,SIZE,MAXW);
         memset(l,0,sizeof(l));
         phi[r[0]=T]=0;
         for(int i=m=0;i<=m;i++){ // �ӻ���������SPFA
             l[x=r[i%SIZE]]=0;
             for(PTR u=e[x];u;u=u->o){ // ������������Ǹ���Ƚ�Ҫ��EPS
                 if(phi[x]+REV(u).w>=phi[u->t] || !REV(u).c) continue;
                 phi[u->t]=phi[x]+REV(u).w;
                 if(!l[u->t]) l[r[++m%SIZE]=u->t]=1;
             }
         }
         do{
             typedef pair<VAL,int> TPL;
             priority_queue<TPL> q;
             fill_n(len,SIZE,MAXW);
             memset(l,0,sizeof(l));
             q.push(TPL(len[T]=0,T));
             while(q.size()){
                 x=q.top().second; q.pop();
                 if(!l[x]) l[x]=1; else continue;
                 for(PTR u=e[x];u;u=u->o){
                     if(!REV(u).c || l[u->t]) continue;
                     VAL at=len[x]+phi[x]+REV(u).w-phi[u->t];
                     if(at>=len[u->t]) continue; // ����Ǹ���Ƚ�Ҫ��EPS
                     len[u->t]=at;
                     now[u->t]=&REV(u);
                     q.push(TPL(-at,u->t));
                 }
             }
             for(x=0;x<SIZE;x++) phi[x]+=len[x];
         }while(phi[S]<MAXW && aug(S,T,can)!=T);
         // ʹ��phi[S]<MAXW����С�����������ʹ��phi[S]<0����С������
        return in-can;
     }
     // �ж���Դ�����½�������Ƿ����
    // �����(T,S)=INF�ɴ����Դ����������ʱ����S->T��c��Ϊ����
    bool feasible_bounded(){
         flow(SIZE-2,SIZE-1);
         for(PTR u=e[SIZE-2];u;u=u->o) if(u->c) return false;
         return true;
     }
     // ��Դ�����½����/��С��������-1��ʾ�����ڿ����������򷵻�����
    int max_flow_bounded(int S, int T){
         add_edge(T,S,INF);
         bool ok=feasible_bounded();
         int ret=e[S]->c;
         edge-=2,e[S]=e[S]->o,e[T]=e[T]->o;
         return ok?ret+flow(S,T):-1;
     }
     int min_flow_bounded(int S, int T){
         flow(SIZE-2,SIZE-1);
         add_edge(T,S,INF);
         bool ok=feasible_bounded();
         int ret=e[S]->c;
         edge-=2,e[S]=e[S]->o,e[T]=e[T]->o;
         return ok?ret:-1;
     }
     // �����д��½�ıߺϲ���ԭͼ��
    void merge_bounded(){
         for(PTR u=e[SIZE-1];u;u=u->o) u->c=REV(u).c=0;
         for(PTR u=e[SIZE-2];u;u=u->o){
             (u+4)->c+=u->c;
             (u+5)->c+=REV(u).c;
             u->c=REV(u).c=0;
         }
     }
};

Network net;

int main()
{
	int T;
	int E, R, N;
	int v;
	cin >> T;
	for (int j = 0; j < T; ++j)
	{
		net.clear();
		cin >> E >> R >> N;
		for (int i = 1; i <= N; ++i)
		{
			cin >> v;
			if (i == 1)
				net.add_edge(0, i, E, 0);
			else
			{
				net.add_edge(0, 2 * i - 2, R, 0);
				net.add_edge(2 * i - 3, 2 * i - 2, E, 0);
				net.add_edge(2 * i - 2, 2 * i - 1, E, 0);
			}
			net.add_edge(2 * i - 1, 2 * N, E, -v);
		}
		net.flow(0, 2 * N);
		cout << "Case #" << j + 1 << ": " << -net.sum << endl;
	}
}