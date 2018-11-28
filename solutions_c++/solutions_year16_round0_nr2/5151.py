#include<bits/stdc++.h>
using namespace std;
#define MAXN 200005
#define mod 1000000007
#define ll long long
#define ull unsigned long long
ull gcd(ull a,ull b){
	ull r;
	while(1){
		r=a%b;
		if(r==0) return b;
		a=b;
		b=r;
	}
	return r;
}

int  main(){
    ll n,t,k,f,test = 1;
	#ifndef ONLINE_JUDGE
    	freopen("inp.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif
	cin>>t;
    bool flag[10];
    string s;
    ll dp[500];
    while(t--){
        cin>>s;
        cout<<"Case #"<<test<<": ";
        ll sz = s.size();
        if(s[0] == '-') dp[0] = 1;
        else dp[0] = 0;
        for(int i=1;i<sz;i++){
            if(s[i] == '-'){
                if(s[i-1] == '-') dp[i] = dp[i-1];
                else dp[i] = dp[i-1] + 2;
            } 
            else{
                dp[i] = dp[i-1];
            }
        }
        cout<<dp[sz-1]<<endl;
        test++;
    }
    
    return 0;
}
