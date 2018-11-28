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
int n;
int a[10][10];
int S,ans;
int b[10];
bool ft[10];
int cnt[1<<20];

bool chk(int sta) {
	int tmp=(1<<n)-1;
	memset(b,0,sizeof b);
	rep(i,1,n) ft[i]=false;
	rep(i,1,n) {
		b[i]=(sta&tmp)>>((i-1)*n);
		tmp=tmp<<n;
	}
	rep(i,1,n)
		if (ft[i]==false) {
			int c=cnt[b[i]];
			rep(j,i+1,n)
				if (b[j]==b[i]) c--;
			if (c==1) {
				bool ff=true;
				rep(j,1,n)
					if (b[j]!=b[i] && (b[j]&b[i])!=0) {ff=false;break;}
				if (ff) {
					ft[i]=true;
					rep(j,i+1,n)
						if (b[j]==b[i]) ft[j]=true;
				} else return false;
			} else {
				return false;
			}
		}
	rep(i,1,n) if (ft[i]==false) return false;
	return true;
}

int main() {
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(i,0,(1<<18)-1) cnt[i]=__builtin_popcount(i);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%d\n",&n);
		memset(a,0,sizeof a);
		S=0;
		rep(i,0,n-1) {
			rep(j,0,n-1) {
				char ch;
				scanf("%c",&ch);
				if (ch=='0') a[i][j]=0;
				else a[i][j]=1;
			}
			scanf("\n");
		}
		repd(i,n-1,0) repd(j,n-1,0)
			S=S*2+a[i][j];
		ans=inf;
		rep(i,0,(1<<(n*n))-1) {
			if ((i&S)==S) {
				if (chk(i))
					ans=min(ans,cnt[i]-cnt[S]);
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
