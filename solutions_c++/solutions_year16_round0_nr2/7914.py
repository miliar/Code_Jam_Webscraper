// By manrajsingh
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define d1(a)cout<<#a<<": "<<a<<"\n";
#define d2(a,b)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<"\n";
#define d3(a,b,c)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<"\n";
#define d4(a,b,c,d)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<"\n";

ll dp1[105],dp2[105];

int main() {
	ll t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for(ll x=1;x<=t;x++){
		string s;
		cin>>s;
		memset(dp1,0,sizeof(dp1));
		memset(dp2,0,sizeof(dp2));
		ll len = s.length();
		for(ll i=0;i<len;i++){
			if(s[i]=='-'){
				dp1[i]=0;
				dp2[i]=0;
			}
			else{
				dp1[i]=1;
				dp2[i]=1;
			}
		}
		ll min1=0;
		for(ll i=len-1;i>=0;i--){
			if(dp1[i]==1){
				continue;
			}
			else{
				min1++;
				for(ll j=i;j>=0;j--){
					dp1[j]=1-dp1[j];
				}
			}
		}
		ll min2=0;
		for(ll i=len-1;i>=0;i--){
			if(dp2[i]==0){
				continue;
			}
			else{
				min2++;
				for(ll j=i;j>=0;j--){
					dp2[j]=1-dp2[j];
				}
			}
		}
		min2++;
		cout<<"Case #"<<x<<": "<<min(min1,min2)<<"\n";
	}
	return 0;
}
