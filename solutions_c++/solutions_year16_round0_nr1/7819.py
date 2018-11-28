// By manrajsingh
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define d1(a)cout<<#a<<": "<<a<<"\n";
#define d2(a,b)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<"\n";
#define d3(a,b,c)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<"\n";
#define d4(a,b,c,d)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<"\n";

ll dp[10];

int main() {
	ll t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for(int x=1;x<=t;x++){
        ll n;
        cin>>n;
        memset(dp,0,sizeof(dp));
        if(n == 0){
            cout<<"Case #"<<x<<": "<<"INSOMNIA\n";
            continue;
        }
        int f=0;
        for(ll i=1;i<=100;i++){
            ll num = i*n;
            ll ans = num;
            while(num){
                int d = num%10;
                dp[d]++;
                num=num/10;
            }
            f=0;
            for(int j=0;j<=9;j++){
                if(dp[j] == 0){
                    f=1;
                    break;
                }
            }
            if(f==0){
                cout<<"Case #"<<x<<": "<<ans<<"\n";
                break;
            }
        }
        if(f == 1){
            cout<<"Case #"<<x<<": "<<"INSOMNIA\n";
        }
	}
	return 0;
}
