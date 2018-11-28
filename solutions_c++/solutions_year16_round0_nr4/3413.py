#include <bits/stdc++.h>
using namespace std;
 
#define MOD 1000000007
#define modulo(a) (a>0?a:-a)
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll; 
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<long long> vll;
ifstream fin("D-small-attempt1.in");
ofstream fout("D-small-attempt1.out");
#define cin fin
#define cout fout
ll expo(ll x,ll n){
	if(n==0) return 1;
	else{
		ll t=expo(x,n/2);
		if(n%2==0){
			return t*t;
		}
		else{
			return t*t*x;
		}
	}
}
int main(){
	ll t,k,c,s;
	// cout<<"Hi";
	cin>>t;
	for(ll iter=1;iter<=t;iter++){
		cin>>k>>c>>s;
		cout<<"Case #"<<iter<<": ";
		
		if(s<k-c+1){
			cout<<"IMPOSSIBLE"<<endl;
		}
		else{
			// cout<<"inside else!!!"<<endl;
			ll factor=expo(k,c-1);
			ll index=0;
			if(c==1){
				for(int i=0;i<k;i++){
					cout<<i+1<<" ";
				}cout<<endl;
				continue;
			}
			// cout<<"loop will iterate for "<<k<<" number of times"<<endl;
			for(ll i=0;i<(k);i++){
				// cout<<", index:"<<index<<",  "<<endl;
				if(factor<1){
					// cout<<"adding 1 as factor is 1"<<endl;
					index++;
				}
				else{
					index+=i*factor;
					// cout<<"adding index by"<<i*factor<<endl;
					factor/=k;

				}
				// cout<<"the value of i"<<i<<", the value of c-1 is:"<<c-1<<endl;
				if(i>=c-1){
					cout<<index+1<<" ";
				}
				else if(i==k-1){
					cout<<index+1<<" ";
				}
			}cout<<endl;
		}
	}
	return 0;

}