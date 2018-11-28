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


int main(void) {
	ifstream ifs("input.dat");
	ofstream ofs("output.dat");

	string str;
	
	int T = 0;
	ifs >> T;

	
	auto set = [](ULL N, array<int, 10>& flags) -> void {
		do {
			flags[N % 10] = 1;
			N /= 10;
		} while (N > 0);
	};

	for (int t = 0; t < T; t++) {
		ULL N;
		ifs >> N;

		if (N == 0) {
			ofs << "Case #" << t + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}

		array<int,10> flags;
		flags.fill(0);


		for (int i = 1; i < 100000; i++ ) {
			set(N*i, flags);
			if (accumulate(flags.begin(), flags.end(), 0) == 10) {
				ofs << "Case #" << t + 1 << ": " << N*i << endl;
				break;
			}
		}

	}





	return 0;
}