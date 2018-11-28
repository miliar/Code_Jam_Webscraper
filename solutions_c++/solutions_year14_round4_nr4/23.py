#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void read();
void kill();
void pre();

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	pre();

	int t;

	cin>>t;

	for (int i=1; i<=t; ++i){
		read();
		cout<<"Case #"<<i<<": ";
		kill();
	}

	return 0;
}

#define M 100100
#define A 30
#define p 1000000007ll
#define long long long
#define N 111

struct node{
	int to[A];
	long c,w;
	bool term;
};

int n,m,k;
node t[M];
long cnk[N][N];

void pre(void){
	for (int i=0; i<N; ++i)
		cnk[i][0]=1;
	for (int i=1; i<N; ++i)
		for (int j=1; j<N; ++j)
			cnk[i][j]=(cnk[i-1][j]+cnk[i-1][j-1])%p;
}

void clear(void){
	k=1;
	for (int i=0; i<M; ++i){
		for (int j=0; j<A; ++j)
			t[i].to[j]=-1;
		t[i].c=t[i].w=0;
		t[i].term=0;
	}
}

void read(){
	cin>>m>>n;
	string s;
	clear();
	for (int i=0; i<m; ++i){
		cin>>s;
		int x = 0;
		for (int j=0; j<s.length(); ++j){
			int ch = s[j]-'A';
			if (t[x].to[ch]>=0)
				x=t[x].to[ch];
			else
				x=t[x].to[ch]=k,++k;
		}
		t[x].term=1;
	}
}

long f[10*N][2*N];

void dfs(int v){
	std::vector<long> c,w;
	int sum = 0;
	if (t[v].term){
		c.push_back(1);
		w.push_back(1);
		sum = 1;
	}
	
	for (int i=0; i<A; ++i)
		if (t[v].to[i]>0){
			int to = t[v].to[i];
			dfs(to);
			sum+=t[to].c;
			c.push_back(t[to].c);
			w.push_back(t[to].w);
		}

	sum = min(n,sum);
	t[v].c=sum;


	for (int i=0; i<=c.size(); ++i)
		for (int j=0; j<=sum; ++j)
			f[i][j]=0;

	f[0][c[0]]=w[0];

	for (int i=1; i<c.size(); ++i)
		for (int j=0; j<=sum; ++j)
			for (int t=0; t<=c[i] && j+t<=sum; ++t){
				long bon = (cnk[j][c[i]-t]*cnk[j+t][t])%p;
				bon=(bon*w[i])%p;
				bon = (bon*f[i-1][j])%p;
				f[i][j+t]=(f[i][j+t]+bon)%p;
			}

	t[v].w=f[c.size()-1][sum];
}

void kill(void){
	dfs(0);
	int c = 0;
	long w = (cnk[n][t[0].c]*t[0].w)%p;
	for (int i=0; i<k; ++i)
		c+=t[i].c;
	cout<<c<<" "<<w<<"\n";
}
