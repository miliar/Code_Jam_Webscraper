#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define si(X) scanf("%d", &(X))
#define sll(X) scanf("%lld",&(X))
ll gcd(ll a,ll b){
	if(b==0)
	return a;
	return gcd(b,a%b);
}
const int mod = 1e9+7;
ll expo(ll base,ll pow){
    ll ans = 1;

    while(pow!=0){
        if(pow&1==1){
            ans = ans*base;
            ans = ans%mod;
        }
        base *= base;
        base%=mod;
        pow/=2;

    }
    return ans;
}
double pi = 3.141592653589793238462643;
double error = 0.0000001;
/* -------Template ends here-------- */

const int M = 100001;

int main(){

	int t;
	si(t);

	for(int alp = 1;alp<=t;alp++){

		string s;
		cin>>s;
		string ans = "";
		char la = s[0];
		ans+=s[0];
		int len = s.length();

		for(int i = 1;i<len;i++){
			if(s[i]>=la){
				ans = s[i]+ans;
				la = s[i];
			}
			else{
				ans = ans+s[i];
			}
		}











		cout<<"Case #"<<alp<<": "<<ans<<endl;

	}











}























