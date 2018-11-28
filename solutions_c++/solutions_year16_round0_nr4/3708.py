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
//#define local

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

int main(){
	std::ios::sync_with_stdio(false);
	#ifdef local
		freopen("in.in","r",stdin);
		freopen("out.txt","w",stdout);
	#endif

	ll t;
	cin>>t;

	ll cases = 1;

	while(t--){
		int k,c,s;
		cin>>k>>c>>s;

		if(k == s){
			cout<<"Case #"<<cases<<": ";
			for(int i = 1;i <= k;i++){
				cout<<i<<" ";
			}
			cout<<endl;
		}
		cases++;
	}
}