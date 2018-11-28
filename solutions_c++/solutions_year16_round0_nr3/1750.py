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
	
		int N,J;
		cin >> N;
		cin >> J;
		
		cout << "Case #" << t + 1 << ":" << endl; 
				
		
		int cnt = 0;
		for(long i = 32769; i < 65536;i+=2){
					long d[11] = {0};
					long d2[11] = {0};
			int flag = 0;
			for(long j = 2; j < 11 ; j++){
				long a = i;
				
				//16回るp−ぷ
				for(long k = 0; k < 16; k++){
					long b = 1;
					//j^k
					for(long l = 0; l < k; l++){
						b = b*j;
					}
					d[j] += a%2 * b;
					a = a/2;
				}
				//dump(d[j]);
				
			}
			
			
			for(long j = 2; j < 11 ; j++){
				
				//d[j]が何かで割り切れるか調べる
				if(flag >= j-2){
					for(long k = 2; k<100; k++){
						if(d[j]%k == 0){
							flag++;
							d2[j] = k;
							break;
						}
					}
				}
		
				
			}
			if(flag == 9){
				cnt++;
				if(cnt == 51)break;
				cout << d[10] ;
				for(long j = 2; j < 11 ; j++){
					cout << " " << d2[j];
				}
				cout << endl;

			}
			
	
			
		}
			
		
			
			
			
			
			
		
	//	cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
			
		

		
	}
}
	