#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
template<class T> T sqr(T x) {return x*x;}
#define pi acos(-1)
#define INF 100000000
#define debug(x) cerr<<#x"="<<(x)<<"\n";
#define foreach(it,v) for (__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)

struct sg {
	int son[26];
};
sg g[100];
string a[100];
vector<int> c[100];
int tot,n,p,a1,a2;

void ins(string s) {
	int i,x;
	x=1;
	for (i=0;i<s.size();i++) {
		if (!g[x].son[s[i]-'A']) g[x].son[s[i]-'A']=++tot;
		x=g[x].son[s[i]-'A'];
	}
}

void dfs(int dep) {
	int i,j,sum;
	if (dep>n) {
		for (i=1;i<=p;i++) if (c[i].empty()) return;
		sum=0;
		for (i=1;i<=p;i++) {
			tot=1;
			memset(g,0,sizeof(g));
			for (j=0;j<c[i].size();j++) ins(a[c[i][j]]);
			sum+=tot;
		}
		if (a1<sum) a1=sum,a2=0;
		if (a1==sum) a2++;
		return;
	}
	for (i=1;i<=p;i++) {
		c[i].push_back(dep);
		dfs(dep+1);
		c[i].pop_back();
	}
}

int main() {
	int tt,te,i;
	scanf("%d",&tt);
	for (te=1;te<=tt;te++) {
		scanf("%d%d",&n,&p);
		for (i=1;i<=n;i++) cin>>a[i];
		a1=a2=0;
		dfs(1);
		printf("Case #%d: %d %d\n",te,a1,a2);
	}
}
