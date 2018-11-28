#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define repd(i,a,b) for (int i=(a);i>=(b);i--)

const int maxn=120;
int a[maxn];
string s;
int ans,n,cnt;

int main() {
	freopen("b.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		cin>>s;
		ans=0;
		rep(i,0,s.length()-1)
			a[i+1]=s[i]=='+'?1:0;
		n=s.length();
		rep(i,1,n) {
			cnt=0;
			rep(j,1,n) cnt+=a[j];
			if (cnt==n) break;
			int k=1;
			while (k<n && a[k+1]==a[1]) k++;
			rep(j,1,k) a[j]^=1;
			ans++;
		}
		printf("%d\n",ans);
	}
	return 0;
}
