#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define repd(i,a,b) for (int i=(a);i>=(b);i--)

typedef long long ll;
typedef unsigned long long ull;

const int inf=~0u>>1;
const int maxn=3000;
int n,r,p,s,tr,tp,ts;
int a[maxn][3];
int ans[maxn];

void solve(int k,int st,int type,int x) {
	if (k==0) {
		a[st][x]=type;
		return;
	}
	solve(k-1,st,type,x);
	solve(k-1,st+(1<<(k-1)),(type+1)%3,x);
}

bool chk(int x) {
	rep(i,0,(1<<n)-1) {
		if (a[i][x]==0) tp--;
		if (a[i][x]==1) tr--;
		if (a[i][x]==2) ts--;
	}
	return tp==0 && tr==0 && ts==0;
}

bool compare(int lef,int rig,int len,int x) {
	rep(i,0,len-1) {
		if (a[lef+i][x]<a[rig+i][x]) return true;
		if (a[lef+i][x]>a[rig+i][x]) return false;
	}
	return false;
}

bool comp(int x) {
	rep(i,0,(1<<n)-1) {
		if (ans[i]<a[i][x]) return true;
		if (ans[i]>a[i][x]) return false;
	}
	return false;
}

void prettify(int k,int st,int x) {
	if (k==0) {
		return;
	}
	prettify(k-1,st,x);
	prettify(k-1,st+(1<<(k-1)),x);
	if (!compare(st,st+(1<<(k-1)), 1<<(k-1),x)) {
		int rig=st+(1<<(k-1));
		rep(i,0,(1<<(k-1))-1) {
			swap(a[st+i][x],a[rig+i][x]);
		}
	}
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%d%d%d%d\n",&n,&r,&p,&s);
		bool ft[3];
		memset(a,-1,sizeof a);
		memset(ans,-1,sizeof ans);
		rep(i,0,2) {
			ft[i]=false;
			tr=r;tp=p;ts=s;
			solve(n,0,i,i);
			if (chk(i)) {
				ft[i]=true;
				prettify(n,0,i);
				if (ans[0]==-1) {
					rep(j,0,(1<<n)-1)
						ans[j]=a[j][i];
				} else {
					if (comp(i))
						rep(j,0,(1<<n)-1)
							ans[j]=a[j][i];
				}
			}
		}
		if (ans[0]>=0) {
			rep(i,0,(1<<n)-1) {
				if (ans[i]==0) putchar('P');
				if (ans[i]==1) putchar('R');
				if (ans[i]==2) putchar('S');
			}
			puts("");
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
