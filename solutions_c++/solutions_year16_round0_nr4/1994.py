//include
//------------------------------------------
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//math
//-------------------------------------------
template<class T> inline T sqr(T x) {return x*x;}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

int main(){
	int T;
	cin >> T;
	for(int t = 0; t< T; t++){
		long K,C,S;
		cin >> K;
		cin >> C;
		cin >> S;
		list<long> l;
		if(C*S >= K){
			long n = 0;
			
			long b;
			if(K%C == 0){
				 b = K/C;
			}else{
				b = K/C + 1;
			}
			for(long i = 0; i< b; i++){
				long cnt = 1;
				for(long k = 0; k < C; k++){
					long a = 1;
					//K^k
					for(int kk = 0; kk < k; kk++){
						a = a* K;
					}
					if(n < K){
						cnt += n * a;
					}
					n++;
				}
				l.PB(cnt);
				dump(cnt);
			}
			
			l.sort();
			cout << "Case #" << t + 1 << ":" ;
			for(long i = 0; i< b; i++){
				cout << " " << l.front();
				l.pop_front();
			}
			cout << endl;
				
			
		}else{
			cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
			
		}

		
	}
}
	