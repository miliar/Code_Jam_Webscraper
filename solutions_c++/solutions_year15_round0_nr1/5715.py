#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define rep(i,a,b) for(i=a; i<=b; i++)
int main()
{
	ios_base::sync_with_stdio(false);
	ll test,t; cin>>test;
	rep (t,0,test-1){
		ll n; cin>>n;
		string s; cin>>s;
		ll m = 0,j,ps=0;
		rep (j,0,n){
			m = max(m, j-ps);
			ps += s[j] - '0';
		}
		cout<<"Case #"<<t+1<<": "<<m<<endl;
	}
	return 0;
}
