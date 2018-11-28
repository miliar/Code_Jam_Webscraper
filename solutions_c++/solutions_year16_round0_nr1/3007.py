/*************************************************************
CodeJam 2016 - https://code.google.com/codejam/contest/6254486/dashboard
09/04/16
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
		cout<<"Case #"<<t<<": ";
		ll n;
		cin>>n;
		if(n==0)
			cout<<"INSOMNIA\n";
		else{
			vector<bool> v(10,false);
			int i = 0;
			while(1){
				bool flag = true;
				ford(j,0,9)
					if(!v[j]){
						flag = false;
						break;
					}
				if(flag)
					break;
				++i;
				ll temp = i*n;
				while(temp){
					v[temp%10] = true;
					temp /= 10;
				}		
			}
			cout<<i*n<<"\n";
		}	
	}
	return 0;
}
