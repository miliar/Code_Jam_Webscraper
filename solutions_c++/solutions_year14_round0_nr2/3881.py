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
#include <sys/resource.h>
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




long double target,rate,newf,hic;


long double tdeno[111111],cdeno[111111];



void prepro(){
	
	cdeno[0]=2;
	repi(i,1,111110){
		cdeno[i]=cdeno[i-1];
		tdeno[i]=tdeno[i-1]+newf/(cdeno[i]);
		cdeno[i]=2+i*rate;
		//~ cout<<cdeno[i]<<tdeno[i]<<endl;
	}
	
	
}



pair<double,double> fun(int n){
	
	double cur=2;
	double tm = 0;
	
	//~ int nn=n;
	
	return mp(tdeno[n],cdeno[n]);
	
	while(n){
		n--;
		tm+=newf/cur;
		cur+=rate;
	}
	
	//~ debug(n,nn,tm,tdeno[nn],cur,cdeno[nn]);
	
	return mp(tm,cur);
	
}



int main(){
	ios_base::sync_with_stdio(0);
	
	rlimit R;getrlimit(RLIMIT_STACK, &R);R.rlim_cur = R.rlim_max;setrlimit(RLIMIT_STACK, &R);
	
	
	
	
	freopen("inb", "r", stdin);
	freopen("out", "w", stdout);
	
	
	
	cout.precision(10);
	cout.setf(ios::fixed);
	
	
	int tests;
	cin>>tests;
	for(int t=1;t<=tests;t++){
		cout<<"Case #"<<t<<": ";
		
		cin>>newf>>rate>>target;
		
		prepro();
		//~ debug(tdeno[2000]);
		
		long double ans=inf;
		
		rep(i,110000){
			pair<double,double> p=fun(i);
			ans=min(ans,p.first+target/p.second);
			
		}
		
		cout<<ans<<endl;

		
	}
	
	
	
}








