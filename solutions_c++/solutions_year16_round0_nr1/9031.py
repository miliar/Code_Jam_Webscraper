#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define vi vector<int>
#define vii vector<long long int>
#define all(v) v.begin(),v.end()
ll gcd (ll a, ll b){
    ll x;
    while (b){
        x = a % b;
        a = b;
        b = x;
    }
    return a;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
	    ll n;
	    cin>>n;
	    ll ad=n;
	    set<int>s;
	    if(n==0){
	    	cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		}
	    else{
			while(1){
		    	ll m=n;
		    	while(n!=0){
		    		int a=n%10;
		    		n=n/10;
		    		s.insert(a);
				}
				if(s.size()==10){
					cout<<"Case #"<<i+1<<": "<<m<<endl;
					break;
				}
				else{
					n=m+ad;
				}
			}
		}
	}
	return 0;
}
