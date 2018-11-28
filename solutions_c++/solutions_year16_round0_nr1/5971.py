#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <cmath>
#include <iomanip>
#include <list>
#include <tuple>
#include <bitset>
#include <ciso646>
#include <cassert>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
typedef vector<ll> vec;

inline bool check(ll x, ll y, ll xMax, ll yMax) { return x >= 0 && y >= 0 && xMax > x && yMax > y; }
inline int toint(string s) { int v; istringstream sin(s); sin >> v; return v; }
template<class T> inline string tostring(T x) { ostringstream sout; sout << x; return sout.str(); }
template<class T> inline T sqr(T x) { return x*x; }
template<class T> inline T mypow(T x, ll n) { T res = 1; while (n > 0) { if (n & 1)res = res * x;	x = x * x;	n >>= 1; }return res; }
inline ll gcd(ll a, ll b) { return b ? gcd(b, a%b) : a; }
inline ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }

#define For(i,a,b)	for(ll (i) = (a);i < (b);(i)++)
#define rep(i,n)	For(i,0,n)
#define rFor(i,a,b)	for(ll (i) = (a-1);i >= (b);(i)--)
#define rrep(i,n)	rFor(i,n,0)
#define each(i,n)	for(auto &i : n)
#define clr(a)		memset((a), 0 ,sizeof(a))
#define mclr(a)		memset((a), -1 ,sizeof(a))
#define all(a)		(a).begin(),(a).end()
#define sz(a)		(sizeof(a))
#define tostr(a)	tostring(a)
#define dump(val) 	cerr << #val " = " << val << endl;
#define Fill(a,v)	fill((int*)a,(int*)(a+(sz(a)/sz(*(a)))),v)

const ll dx[8] = { 1, 0, -1, 0, 1, 1, -1, -1 }, dy[8] = { 0, -1, 0, 1, -1, 1, -1, 1 };

const ll mod = 1e9 + 7;
const ll INF = 1e10 + 9;

#define int ll
#define double ld

struct BigInteger{
	string num;
	BigInteger() 
		: num("0")
	{}
	BigInteger(string num) 
		: num(num)
	{}
	friend istream& operator >> (istream &is, BigInteger &my) {
		is >> my.num;
		return is;
	}
	friend ostream& operator << (ostream &os, BigInteger &my) {
		os << my.num;
		return os;
	}
	bool operator == (const BigInteger &other) const {
		return num == other.num;
	}
	bool operator == (const int &other) const {
		return num == tostr(other);
	}

	BigInteger operator + (BigInteger &other) {
		string add = other.num;
		string num2 = num;
		if (add.size() > num.size()) {
			swap(add, num);
		}
		reverse(all(num2));
		reverse(all(add));

		rep(i, add.size()) {
			int tmp = add[i] - '0';
			num2[i] += tmp;
			for (int j = i ;num2[j] > '9'; j++) {
				int over = 0;
				while (num2[j] > '9') {
					over++;
					num2[j] -= 10;
				}
				if (j + 1 == num2.size()) {
					num2 += '0';
				}
				num2[j + 1] += over;
			}
		}

		reverse(all(num2));
		return num2;
	}
};

signed main() {
	cin.tie(0);
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;
	rep(_, T) {
		BigInteger t;
		cin >> t;
		cout << "Case #" << _ + 1 << ": ";
		if (t == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		BigInteger now = t;
		set<int> se;
		while (1) {
			rep(i, now.num.size()) {
				se.insert(now.num[i] - '0');
			}
			if (se.size() == 10) {
				break;
			}
			now = now + t;
		}
		cout << now << endl;
	}
	return 0;
}

