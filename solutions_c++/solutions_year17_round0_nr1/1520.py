#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<string>
#include<cstdio>
#include<vector>
#include<cstring>
#include<iostream>
#include<algorithm>
#define rep(i,a,b) for (int i=a; i<=b; i++)
#define per(i,a,b) for (int i=a; i>=b; i--)
#define debug(x) {cout<<(#x)<<" "<<x<<endl;}
using namespace std;
typedef long long LL;

inline int read() {
    int x=0,f=1; char ch=getchar();
    while (!(ch>='0'&&ch<='9')) {if (ch=='-')f=-1;ch=getchar();}
    while (ch>='0'&&ch<='9') {x=x*10+(ch-'0'); ch=getchar();}
    return x*f;
}

const int N = 1005;

bool a[N];
char s[N];

int main() {

	#ifndef ONLINE_JUDGE
		freopen("A-large.in","r",stdin);
		freopen("data.out","w",stdout);
	#endif

	int T=read();
	rep(t,1,T) {
		printf("Case #%d: ",t);
		int ans=0,n; scanf("%s",s+1); n=strlen(s+1);
		rep(i,1,n) if (s[i]=='-') a[i]=0; else a[i]=1;
		int k=read(); 
		rep(i,1,n-k+1) {
			if (!a[i]) {
				ans++;
				rep(j,i,i+k-1) a[j]^=1;
			}
		}
		bool flag=1;
		rep(i,n-k+2,n) if (!a[i]) flag=0;
		if (flag) printf("%d\n",ans); else printf("IMPOSSIBLE\n");
		
	}

	return 0;
}

