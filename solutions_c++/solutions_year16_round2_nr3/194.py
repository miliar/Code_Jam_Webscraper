#include<bits/stdc++.h>
using namespace std;

const int MAXN=22000,MAXM=440000;
struct Dinic{
    struct edge{
        int x,y;//�������� 
        int c;//���� 
        int f;//��ǰ���� 
        edge *next,*back;//��һ���ߣ������ 
        edge(int x,int y,int c,edge* next):x(x),y(y),c(c),f(0),next(next),back(0){}
        void* operator new(size_t, void *p){return p;}
    }*E[MAXN],*data;//E[i]���涥��i�ı߱�
    char storage[2*MAXM*sizeof(edge)];
    int S,T;//Դ����
    
    int Q[MAXN];//DFS�õ���queue
    int D[MAXN];//�����ţ�-1��ʾ���ɴ�
    void DFS(){
        memset(D,-1,sizeof(D));
        int head=0,tail=0;
        Q[tail++]=S;
        D[S]=0;
        for(;;){
            int i=Q[head++];
            for(edge* e=E[i];e;e=e->next){
                if(e->c==0)continue;
                int j=e->y;
                if(D[j]==-1){
                    D[j]=D[i]+1;
                    Q[tail++]=j;
                    if(j==T)return;
                }
            }
            if(head==tail)break;
        }
    }
    edge* cur[MAXN];//��ǰ��
    edge* path[MAXN];//��ǰ�ҵ�������·
    int flow(){
        int res=0;//������������� 
        int path_n;//path�Ĵ�С
        for(;;){
            DFS();
            if(D[T]==-1)break;
            memcpy(cur,E,sizeof(E));
            path_n=0;
            int i=S;
            for(;;){
                if(i==T){//���ҵ�һ������·������֮ 
                    int mink=0;
                    int delta=INT_MAX;
                    for(int k=0;k<path_n;++k){
                        if(path[k]->c < delta){
                            delta = path[k]->c;
                            mink=k;
                        }
                    }
                    for(int k=0;k<path_n;++k){
                        path[k]->c -= delta;
                        path[k]->back->c += delta;
                    }
                    path_n=mink;//���� 
                    i=path[path_n]->x;
                    res+=delta;
                }
                edge* e;
                for(e=cur[i];e;e=e->next){
                    if(e->c==0)continue;
                    int j=e->y;
                    if(D[i]+1==D[j])break;//�ҵ�һ�������ӵ�·���� 
                }
                cur[i]=e;//��ǰ���ṹ�����ʹ��Ĳ�������Ļ������ٷ���
                if(e){
                    path[path_n++]=e;
                    i=e->y;
                }
                else{//�ýڵ���û���κο�����Ļ�����ͼ��ɾȥ������һ�� 
                    D[i]=-1;
                    if(path_n==0)break;
                    path_n--;
                    i=path[path_n]->x;
                }
            }
        }
        return res;
    }
    int cut(int* s){
        int rst=0;
        for(int i=0;i<MAXN;++i)
            if(D[i]==-1&&E[i])
                s[rst++]=i;
        return rst;
    }
    void init(int _S,int _T){
        S=_S,T=_T;
        data=(edge*)storage; 
        memset(E,0,sizeof(E));
    }
    void add_edge(int x,int y,int w){//�ӽ�һ��x��y����Ϊw�ıߣ���Ҫ��֤0<=x,y<MAXN��0<w<=INT_MAX 
        E[x]=new((void*)data++) edge(x,y,w,E[x]);
        E[y]=new((void*)data++) edge(y,x,0,E[y]);
        E[x]->back = E[y];
        E[y]->back = E[x];
    }
};

string u[MAXN], v[MAXN];
int vis[MAXN];

Dinic dinic;
int main(){
	freopen("Cl.in", "r", stdin);
	freopen("Cl.out", "w", stdout);
	int T;
	cin>>T;
	for(int o = 1; o <= T; o++){
		int n;
		scanf("%d", &n);
		string s, t;
		map<string, int> p, q;
		int pp = 0, qq = 0;
		for(int i = 1; i <= n; i++){
			cin>>s>>t;
			if (p.find(s) == p.end())
				p[s] = ++pp;
			if (q.find(t) == q.end())
				q[t] = ++qq;
			u[i] = s, v[i] = t;
		}
		dinic.init(1, pp + qq + 2);
		for(int i = 1; i <= pp; i++)
			dinic.add_edge(1, i + 1, 1);
		for(int i = 1; i <= qq; i++)
			dinic.add_edge(pp + i + 1, pp + qq + 2, 1);
		for(int i = 1; i <= n; i++)
			dinic.add_edge(p[u[i]] + 1, q[v[i]] + 1 + pp, 1);
		int ans = dinic.flow();
	//	cout<<ans<<endl;
		ans = n - (pp + qq - ans);
		/*
		int ans = 0;
		for(int i = 1; i <= n; i++)
			vis[i] = 0;
		for(int i = 1; i <= n; i++){
			int flag = 0;
			for(int j = 1; j <= n; j++)
				if (!vis[j] && p[u[j]] > 1 && q[v[j]] > 1){
					ans++;
					flag = 1;
					vis[j] = 1;
					p[u[j]]--;
					q[v[j]]--;
					break;
				}
			if (!flag)
				break;
		}*/
		printf("Case #%d: %d\n", o, ans);
	}
	return 0;
	/*
    int N,M;
    while(2==scanf("%d%d",&N,&M)){
        int rst=0;
        int S=0,T=N+1;
        dinic.init(S,T);
        for(int i=1;i<=N;++i){
            int a,b;
            scanf("%d%d",&a,&b);
            dinic.add_edge(S,i,a);
            dinic.add_edge(i,T,b);
        }
        for(int i=0;i<M;++i){
            int x,y,w;
            scanf("%d%d%d",&x,&y,&w);
            dinic.add_edge(x,y,w);
            dinic.add_edge(y,x,w);
        }
        rst=dinic.flow();
        printf("%d\n",rst);
    }*/
}
 
