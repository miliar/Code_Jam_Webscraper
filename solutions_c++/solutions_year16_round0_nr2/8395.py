#include <bits/stdc++.h>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pll pair<ll,ll>
#define MOD 1000000007
#define ll long long int
#define MAXINT 1000000001ll
#define SET(x,y) memset(x,y,sizeof(x));

using namespace std;

char S[10000];

int main() {
	int t,i,j,ans,l;
	char pre;
	cin>>t;
	for(j=1;j<=t;j++) {
		cin>>S;
		l=strlen(S);
		for(i=l-1;i>=0;i--)
			if(S[i]=='-')
				break;
		pre='+';
		ans=0;
		for(;i>=0;i--) {
			if(S[i]!=pre) {
				ans++;
				pre=S[i];
			}
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}