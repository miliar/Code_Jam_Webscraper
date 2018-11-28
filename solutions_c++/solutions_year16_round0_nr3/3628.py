//include
//------------------------------------------
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <array>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
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
inline int toInt(string s) { int v; istringstream sin(s); sin >> v; return v; }
template<class T> inline string toString(T x) { ostringstream sout; sout << x; return sout.str(); }

//math
//-------------------------------------------
template<class T> inline T sqr(T x) { return x*x; }

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
const double PI = acos(-1.0);

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;


using ULL = unsigned long long int;

// jamcoin ‚Í 1‚ÅŽn‚Ü‚è1‚ÅI‚í‚é
// 2~10‚¢‚¸‚ê‚©‚Ìi”‚ÅŒvŽZ‚µ‚Ä‚à‘f”‚É‚È‚ç‚È‚¢
// ‘f”‚Å‚Í–³‚¢Ø‹’‚ð•t‚¯‚Äjamcoin‚ð—ñ‹“‚¹‚æ

void solve(int N, int J, ofstream& ofs ) {
	int count = 0;

	ULL maxi = pow(2, N);
	array<ULL,11> buff;
	array<ULL, 11> interbuff;

	for (ULL i = 0; i < maxi; i++) {
		if ((i & 0x01) == 0) continue;
		if ((i & (maxi >> 1)) == 0) continue;

		/*
		ofs << endl << "check : ";
		for (ULL n = N; n > 0; n--) {
			ofs << ((i & (0x01 << (n-1))) ? 1 : 0);
		}
		ofs << endl;
		*/
		buff.fill(0);
		interbuff.fill(0);
		bool success = true;

		for (ULL b = 2; b <= 10; b++) {
			ULL inter = 0;
			for (ULL n = 0; n < N; n++) {
				inter += pow(b, n) * ((i & (0x01 << n)) ? 1 : 0);
			}
			if ((inter % 2) == 0) {
				buff[b] = 2;
				interbuff[b] = inter;
				continue;
			}
			
			bool isprime = true;
			for (ULL d = 2; d <= inter / d; d++) {
				if ((inter%d) == 0) {
					buff[b] = d;
					isprime = false;
					interbuff[b] = inter;
					break;
				}
			}

			if (isprime == true) {
				success = false;
				break;
			}
		}

		if (success) {
			for (ULL n = N; n > 0; n--) {
				ofs << ((i & (0x01 << (n - 1))) ? 1 : 0);
			}
			for (ULL b = 2; b <= 10; b++) {
				ofs << " " << /*interbuff[b] << "=" << */ buff[b];
			}
			ofs << endl;
			count++;
		}

		if (count >= J) {
			break;
		}
	}
}

int main(void) {
	ifstream ifs("c.in");
	ofstream ofs("c.out");

	string str;
	
	int T = 0;
	ifs >> T;

	
	for (int t = 0; t < T; t++) {
		int n, j;
		ifs >> n >> j;
		ofs << "Case #" << t + 1 << ": "<< endl;
		solve(n, j, ofs);
	}




	return 0;
}