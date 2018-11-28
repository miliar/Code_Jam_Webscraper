#include <iostream>
#include <stdio.h>
#include <algorithm>
#define FOR(i,n) for(ll i=0;i<n;i++)
#define FR(i,k,n) for(ll i=k;i<n;i++)
#define size 10000007
typedef long long int ll;
using namespace std;
ll s[size];

int main() {
    freopen("r.txt","r",stdin);
    freopen("out.txt","w",stdout);
	ll t,n,ans,d=2,sum;
	cin>>t;
	FR(q,1,t+1){
		cout<<"Case #"<<q<<": ";
		cin>>n;
		FOR(i,n)cin>>s[i];
		ans = s[0];
		FOR(i,n)if(ans<s[i])ans=s[i];d=2;
		while(ans>d){
			sum=0;
			FOR(i,n){
				sum+=(s[i]-1)/d;
			}
			ans = min(ans, sum+d);d++;
		}
		cout<<ans<<"\n";
	}
	return 0;
}
