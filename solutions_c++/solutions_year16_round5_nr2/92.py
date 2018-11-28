#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int MAXN=110;
const int MAXL=25;
const int MAXM=8;
char Cool[MAXM][MAXL];
char Title[MAXN];
int req[MAXN];

const int TRY=10000;

VI add[MAXN];
int down[MAXN];

const int seed=514;

mt19937 rng(seed);
int randint(int lb,int ub) { // [lb, ub]
	return uniform_int_distribution<int>(lb,ub)(rng);
}

void init(int N) {
	int out[MAXN]={0};
	VI add[MAXN];
	for(int i=1;i<=N;i++) out[req[i]]++;
	for(int i=1;i<=N;i++) add[ i ].PB(req[i]);
	fill(down,down+N+1,1);
	stack<int> st;
	for(int i=1;i<=N;i++) if(out[i]==0) st.push(i);
	while(SZ(st)) {
		int nxt=st.top(); st.pop();
		debug("%d **\n",nxt);
		down[req[nxt]]+=down[nxt];
		for(int t:add[nxt]) {
			out[t]--;
			debug("%d -- %d\n",t,out[t]);
			if(out[t]==0)
				st.push(t);
		}
	}
	for(int i=1;i<=N;i++)
		debug("%d:%d\n",i,down[i]);
}

int get(const VI &pos) {
	int sum=0;
	for(int t:pos) sum+=down[t];
	int r=randint(1,sum);
	for(int i=0;;i++) {
		r-=down[pos[i]];
		if(r<=0) return i;
	}
}

int main() {
	int all_kase;
	scanf("%d",&all_kase);
	for(int num_kase=1;num_kase<=all_kase;num_kase++) {
		int N,M;
		int cnt[10]={0};
		scanf("%d",&N);
		for(int i=1;i<=N;i++) scanf("%d",req+i);
		scanf("%s",Title);
		scanf("%d",&M);
		for(int i=0;i<M;i++) scanf("%s",Cool[i]);

		for(int i=0;i<=N;i++) add[i].clear();
		for(int i=1;i<=N;i++) add[ req[i] ].PB(i);
		init(N);
		for(int _i=0;_i<TRY;_i++) {
			VI pos;
			for(int t:add[0]) pos.PB(t);
			string res;
			for(int i=1;i<=N;i++) {
				int ch=get(pos);
				int id=pos[ch];
				if(_i==0) debug("%d:%d %d\n",i,ch,id);
				swap(pos[ch],pos.back());
				pos.pop_back();
				res=res+Title[ id-1 ];
				for(int t:add[id]) pos.PB(t);
			}
			if(_i==0) debug("%s\n",res.c_str());
			for(int i=0;i<M;i++) if(res.find(Cool[i])!=string::npos) cnt[i]++;
		}
		printf("Case #%d:",num_kase);
		for(int i=0;i<M;i++) printf(" %f",(double)cnt[i]/TRY);
		puts("");
	}
	return 0;
}
