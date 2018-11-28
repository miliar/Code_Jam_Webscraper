#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define MP make_pair
#define PB push_back

using namespace std;

using ll = long long;

int read(){
	int i;
	scanf("%d",&i);
	return i;
}

const int Nmax=4;
int n;
char op[Nmax][Nmax+1];

void Input(){
	n=read();
	REP(i,n)
		scanf("%s",op[i]);
}

bool con[Nmax][Nmax];

struct BipareMatching{
	static const int SIZE=Nmax*2;
	vector<int> graph[SIZE];
	void add_edge(int f,int t){
		graph[f].push_back(t);
		graph[t].push_back(f);
	}
	void Clear(){
		REP(i,SIZE)
			graph[i].clear();
	}
	bool used[SIZE];
	int match[SIZE];
	bool dfs(int i){
		used[i]=true;
		for(int j=0;j<(int)graph[i].size();j++){
			int c=graph[i][j];
			int m=match[c];
			if(m==-1||(!used[m] && dfs(m))){
				match[i]=c;
				match[c]=i;
				return true;
			}
		}
		return false;
	}
	int Calc(){
		int res=0;
		memset(match,-1,sizeof(match));
		REP(i,SIZE)
			if(match[i]==-1){
				memset(used,false,sizeof(used));
				if(dfs(i))
					res++;
			}
		return res;
	}
} bm;

void Solve(){
	int ans=INT_MAX;
	for(int bit=0;bit<(1<<(n*n));bit++){
		int cost=0;
		REP(i,n)
			REP(j,n){
				int k=i*n+j;
				bool d=op[i][j]=='1';
				bool e=(bit>>k)&1;
				if(d&&!e)
					goto endloop;
				if(!d&&e)
					cost++;
				con[i][j]=e;
			}
		if(cost>=ans)
			continue;
		REP(i,n){
			bm.Clear();
			int c=0;
			REP(k,n)
				if(con[i][k]){
					c++;
					REP(j,n){
						if(i==j)
							continue;
						if(con[j][k])
							bm.add_edge(j,k+n);
					}
				}
			if(bm.Calc()>=c)
				goto endloop;
		}
		ans=cost;
		endloop:;
	}
	printf("%d\n",ans);
}

int main(){
	int t=read();
	REP(caseNumber,t){
		Input();
		printf("Case #%d: ",caseNumber+1);
		Solve();
	}
}