#include <iostream>
#include <stdio.h>
#include <algorithm>
#define FOR(i,n) for(ll i=0;i<n;i++)
#define FR(i,k,n) for(ll i=k;i<n;i++)
#define size 10000007
typedef long long int ll;
using namespace std;
ll s[size];
bool func(ll x,ll r, ll c){
    FR(i,1,x+1){
        if(x%i==0){
            if(( x/i>min(r,c) && i>min(r,c) ) || (x/i>max(r,c) && i>max(r,c) )){return 0;}
         }
    }
    return 1;
}
bool fun(ll x, ll r, ll c){
    bool ans = func(x,r,c);
    if(ans==0)return 0;
    if(x==3){
        if(min(r,c)<2)return 0;
    }
    if(x==4){
        if(min(r,c)<3)return 0;
    }
    return ans;
}
int main() {
    freopen("r.txt","r",stdin);
    freopen("out.txt","w",stdout);
	ll t,r,c,x;
	cin>>t;
	FR(q,1,t+1){
		cout<<"Case #"<<q<<": ";
		cin>>x>>r>>c;
		cerr<<q<<": "<<x<<" "<<r<< " "<<c<<"\n";
		if(r*c%x!=0){cout<<"RICHARD\n";continue;}
		if(x==1||x==2){cout<<"GABRIEL\n";continue;}
		if(x==3){if(min(r,c)<2)cout<<"RICHARD\n";else cout<<"GABRIEL\n";continue;}
		if(x==4){if(min(r,c)<=2)cout<<"RICHARD\n";else cout<<"GABRIEL\n";continue;}
		if(x>=7){cout<<"RICHARD\n";continue;}
		if(x>=max(r,c)){cout<<"RICHARD\n";continue;}
		if((x+1)/2>min(r,c)){cout<<"RICHARD\n";continue;}
		bool ans = fun(x,r,c);
		if(ans)cout<<"GABRIEL\n";
		else cout<<"RICHARD\n";
		//cerr<<ans<<"\n";
	}
	return 0;
}
