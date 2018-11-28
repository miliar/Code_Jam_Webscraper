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
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin>>t;
    for(int j=0;j<t;j++){
    	string s;
    	cin>>s;
    	int a[s.length()];
    	for(int i=0;i<s.length();i++){
    		if(s[i]=='+'){
    			a[i]=1;
			}
			else{
				a[i]=0;
			}
		}
		ll ans=0;
		int c=a[0];
		for(int i=1;i<s.length();i++){
			if(a[i]!=c){
				c=a[i];
				ans++;
			}
		}
		if(a[s.length()-1]==0){
			ans++;
		}
		cout<<"Case #"<<j+1<<": "<<ans<<endl;
	}
	return 0;
}
