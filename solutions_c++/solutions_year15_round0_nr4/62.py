#include <bits/stdc++.h>
using namespace std;

#define repu(i, a, b) for (int i = (a); i < (b); ++i)
#define repd(i, a, b) for (int i = (a); i > (b); --i)
#define mem(a, x) memset(a, x, sizeof(a))
#define all(a) a.begin(), a.end()
#define uni(a) a.erase(unique(all(a)), a.end())
#define count_bits(x) __builtin_popcount(x)
#define count_bitsll(x) __builtin_popcountll(x)
#define least_bits(x) __builtin_ffs(x)
#define least_bitsll(x) __builtin_ffsll(x)
#define most_bits(x) 32 - __builtin_clz(x)
#define most_bitsll(x) 64 - __builtin_clz(x)

vector<string> split(const string &s, char c) {
	vector<string> v;
	stringstream ss(s);
	string x;
	while (getline(ss, x, c)) v.push_back(x);
	return v;
}

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

void err(vector<string>::iterator it) {}

template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
	cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
	err(++it, args...);
}

typedef long long ll;
const int MOD = 1000000007;

template<class T, class U> inline T tmin(T a, U b) {return (a < b) ? a : b;}
template<class T, class U> inline T tmax(T a, U b) {return (a > b) ? a : b;}
template<class T, class U> inline void amax(T &a, U b) {if (b > a) a = b;}
template<class T, class U> inline void amin(T &a, U b) {if (b < a) a = b;}
template<class T> inline T tabs(T a) {return (a > 0) ? a : -a;}
template<class T> T gcd(T a, T b) {while (b != 0) {T c = a; a = b; b = c % b;} return a;}

const int N = 21;
bool good[N][N][N];

int main(int argc, char *argv[]) {
    ios_base::sync_with_stdio(false);
    int ntest, R, C, X;

    mem(good, 0);
    
    for (int i = 2; i < 21; i += 2)
    	good[4][2][i] = 1;
    for (int i = 5; i < 21; i += 5)
    	good[5][2][i] = 1;
    good[5][3][5] = 1;
    for (int i = 3; i < 21; i += 3)
    	good[6][2][i] = 1;
    for (int i = 2; i < 21; i += 2)
    	good[6][3][i] = 1;

    cin >> ntest;
    repu(it, 1, ntest + 1) {
    	cin >> X >> R >> C;
    	if (R > C) swap(R, C);
    	bool ric = 0;
    	if ((R * C) % X) ric = 1;
    	else if (X >= 7) ric = 1;
    	else if (X == R * C && X > 2) ric = 1;
    	else if (R == 1 && X > 2) ric = 1;
    	else if (X > C) ric = 1;
    	else ric = good[X][R][C];

    	cout << "Case #" << it << ": " << (ric ? "RICHARD" : "GABRIEL") << endl;
    }
    return 0;
}
