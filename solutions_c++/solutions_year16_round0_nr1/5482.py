#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
typedef stack<long long> ss;
#define get(a) #a

//#define DEBUG
#define local

#define endl '\n'

#ifdef DEBUG
 
#define debug(args...) {dbg,args; cerr<<endl;}
 
#else
 
#define debug(args...) // Just strip off all debug tokens
 
#endif
 
struct debugger
 
{
 
template<typename T> debugger& operator , (const T& v)
 
{
 
cerr<<v<<" ";
 
return *this;
 
}
 
} dbg;

vector<int> arr(10,0);

bool checkdigits(ll n){
	while(n >= 1){
		//cout<<(n%10)<<" "<<endl;
		arr[n%10] = 1;
		n /= 10;
	}

	for(int i = 0;i < 10;i++){
		if(!arr[i]){
			return false;
		}
	}
	return true;
}

int main(){
	std::ios::sync_with_stdio(false);
	#ifdef local
		freopen("in.in","r",stdin);
		freopen("out.txt","w",stdout);
	#endif

	ll t,n;
	cin>>t;

	ll cases = 1;

	while(t--){
		cin>>n;

		if(n == 0){
			cout<<"Case #"<<cases<<": INSOMNIA\n";
			cases++;
			continue;
		}
		ll k = n;
		ll j = 1;
		while(true){
			if(checkdigits(k)){
				break;
			}
			j++;
			k = j*n; 
		}
		cout<<"Case #"<<cases<<": "<<k<<"\n";
		for(int i = 0;i < 10;i++){
			arr[i] = 0;
		}
		cases++;
	}
}