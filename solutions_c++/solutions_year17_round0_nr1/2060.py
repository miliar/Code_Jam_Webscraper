#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 1000000000
#define INFLL 1000000000000000010ll
#define UQ(x) (x).resize(distance((x).begin(),unique(all((x)))))
#define mid(x,y) (((x)+(y))>>1)
int tc,n,k;
char s[10005];
int main() {
	scanf("%d",&tc);
	for (int kk=1;kk<=tc;kk++) {
		scanf("%s%d",s,&k);
		n=strlen(s);
		int ans=0;
		for (int i=0;i<n-k+1;i++) {
			if (s[i]=='-') {
				ans++;
				for (int j=0;j<k;j++) {
					if (s[i+j]=='-') s[i+j]='+';
					else s[i+j]='-';
				}
			}
		}
		bool can=1;
		for (int i=0;i<n;i++) {
			if (s[i]=='-') {
				can=0;
				break;
			}
		}
		if (can) printf("Case #%d: %d\n", kk,ans);
		else printf("Case #%d: IMPOSSIBLE\n", kk);
	}
}