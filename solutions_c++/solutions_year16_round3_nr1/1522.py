/*************************************************************
CodeJam 2016 - https://code.google.com/codejam/contest/4314486/dashboard
30/04/16
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
		ll n,tot=0;
		cin>>n;
		vector< pii > v(n);
		ford(i,0,n-1){
			int temp;
			cin>>temp;
			v[i] = mp(temp,i);
		}
		ford(i,0,n-1)
			tot += v[i].first;
		while(tot){
			sort(v.begin(), v.end());
			if(v[n-2].first <= (tot - min(2, v[n-1].first))/2){
				if(v[n-1].first > 1){
					cout<<" "<<(char)('A' + v[n-1].second)<<(char)('A' + v[n-1].second);
					v[n-1].first -= 2;
					tot -= 2;
				}
				else{
					cout<<" "<<(char)('A' + v[n-1].second);
					v[n-1].first -= 1;
					tot -= 1;	
				}
			}
			else{
				cout<<" "<<(char)('A' + v[n-1].second)<<(char)('A' + v[n-2].second);
				v[n-1].first -= 1;
				v[n-2].first -= 1;
				tot -= 2;
			}
		}	
		cout<<"\n";	
	}
	return 0;
}
