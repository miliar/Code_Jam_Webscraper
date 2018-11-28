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
		string s;
		cin>>s;

		ll count = 0;

		
		ll something = 0;
		ll next = 102;
		for(int i = 0;i < s.size();i++){
			if(s[i] == '-'){
				something++;
			}	
			else if(s[i] == '+'){
				next = i;
				break;
			}
		}
		if(something){
			count++;
		}


		for(int i = next;i < s.size();i++){
			if(s[i] == '-' && s[i-1] == '+'){
				count += 2;
			}
		}

		cout<<"Case #"<<cases<<": "<<count<<"\n";
		cases++;
	}
}