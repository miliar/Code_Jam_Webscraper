#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <cctype>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <complex>
#include <numeric>
#include <valarray>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;

#define inf 1061109567LL
#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define mem(x,a) memset(x,a,sizeof(x))
#define rep(i,n) for(int i(0),_n(n);i<_n;++i)
#define repi(i,a,b) for(int i(a),_b(b);i<_b;++i)
#define repr(i,a,b) for(int i(a),_b(b);i>=_b;--i)
#define repe(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define len(x) ((int)(x.size()))

#define DEBUG 1 
#if DEBUG && !ONLINE_JUDGE 
	#define debug(args...) (Debugger()) , args
	class Debugger { public: Debugger(const std::string& _separator = ", ") : first(true), separator(_separator){} template<typename ObjectType> Debugger& operator , (const ObjectType& v) { if(!first) std::cerr << separator; std::cerr << v; first = false; return *this; } ~Debugger() { std::cerr << endl;} private: bool first; std::string separator; }; template <typename T1, typename T2> inline std::ostream& operator << (std::ostream& os, const std::pair<T1, T2>& p) { return os << "(" << p.first << ", " << p.second << ")"; } template<typename T> inline std::ostream &operator << (std::ostream & os,const std::vector<T>& v) { bool first = true; os << "["; for(unsigned int i = 0; i < v.size(); i++) { if(!first) os << ", "; os << v[i]; first = false; } return os << "]"; } template<typename T> inline std::ostream &operator << (std::ostream & os,const std::set<T>& v) { bool first = true; os << "["; for (typename std::set<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) { if(!first) os << ", "; os << *ii; first = false; } return os << "]"; } template<typename T1, typename T2> inline std::ostream &operator << (std::ostream & os,const std::map<T1, T2>& v) { bool first = true; os << "["; for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii) { if(!first) os << ", "; os << *ii ; first = false; } return os << "]"; } 
#else 
		#define debug(args...) 
#endif



int n,t1,t2;

double in;

vi v1,v2;




int main(){
	ios_base::sync_with_stdio(0);
	
	freopen("inc", "r", stdin);
	freopen("out", "w", stdout);
	
	
	
	int tests;
	cin>>tests;
	for(int t=1;t<=tests;t++){
		cout<<"Case #"<<t<<": ";
		
		cin>>n;
		
		v1.clear();
		v2.clear();
		
		vi vv1,vv2;
		
		rep(i,n){
			cin>>in;
			t1=in*1000000;
			v1.pb(t1);

		}
		rep(i,n){
			cin>>in;
			t1=in*1000000;
			v2.pb(t1);

		}
		

		
		vv1=v1;vv2=v2;
		
		sort(all(vv1));
		sort(all(vv2));
		
		set<int> sst=set<int>(all(vv2));
		
		
		
		int nn=0;
		
		int pos=0;
		
		rep(i,n){
			
			
			
			if(vv1[i]>vv2[pos]){
				nn++;	
				pos++;			
			}
			else {
				
			}
			
			
			//~ rep(j,len(vv2))if(vv1[i]>vv2[j]){
				//~ 
				//~ vi tem;
				//~ 
				//~ rep(k,len(vv2))if(j!=k)tem.pb(vv2[k]);
				//~ 
				//~ vv2=tem;
				//~ nn++;
				//~ goto lll;
				//~ 
			//~ }
			//~ 
			//~ vv2.pop_back();
			//~ 
//~ 
			//~ lll:;
		}
		
		
		
		cout<<nn<<" ";
		
		
		int mx=0;

		set<int> sss=set<int>(all(v2));
		
		sort(all(v1));
		
		vi v3;
		
		rep(i,n)v3.pb(i);
		
		//~ int flag=0;
		
		//~ do{
			set<int> st=sss;
			int cur=0;
			rep(i,n){
				
				if(st.lower_bound(v1[v3[i]])==st.end()){
					st.erase(st.begin());
					cur++;
				}
				else {

					st.erase(st.lower_bound(v1[v3[i]]));
				}
				
			}
			mx=max(mx,cur);
			
		//~ }while(next_permutation(all(v3)));
		
		cout<<mx<<endl;
		
	}
	
	
	
}








