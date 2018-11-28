/*************************************************************
CodeJam 2016 - https://code.google.com/codejam/contest/6254486/dashboard
16/04/16
Sahil Arora
*************************************************************/
#include<bits/stdc++.h>
using namespace std;

#define ll 			long long
#define vll 		vector< long long >
#define vvll 		vector< vll >
#define vd 			vector< double > 
#define ford(i,x,a) for(ll i=x;i<=a;++i)
#define fore(i,x,a) for(ll i=x;i>=a;--i)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mp make_pair
#define ff first
#define ss second
#define all(a) a.begin(), a.end()
#define pb push_back 
const ll mod = 1e9+7;

int main(int argc, char const *argv[])
{
	/* code */
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	long long test;
	cin>>test;
	ford(t,1,test){
		cout<<"Case #"<<t<<":";
		ll n;
		cin>>n;
		vll v(2501,0), u;
		ford(i,0,2*n-2){
			ford(j,0,n-1){
			int temp;
			cin>>temp;
			++v[temp];}
		}
		ford(i,1,2500)
			if(v[i]%2)
				u.pb(i);
		sort(all(u));	
		ford(i,0,n-1)
			cout<<" "<<u[i];
		cout<<"\n";	
	}
	return 0;
}
