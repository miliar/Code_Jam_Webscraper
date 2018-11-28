/*

 Email : ahmed.aly.tc@gmail.com

 ahmed_aly on HackerRank, Codeforces and TopCoder

 Google Code Jam tools website: http://a2oj.com/CodeJamTools/

 */

#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int N, I, J, n, m;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

//#define SMALL
#define LARGE

string s1, s2;

ll abs2(ll x) {
	if (x < 0)
		return -x;
	return x;
}

string tos(ll x) {
	ss S;
	S << x;
	string ret = S.str();
	while (sz(ret) < n)
		ret = "0" + ret;
	return ret;
}
ll ten[20];

pll solve(int from, int gr) {
	pll ret = mp(0, 0);
	if (gr) {
		// s1 prefix > s2 prefix
		rep2(i,from,n)
		{
			if (s1[i] != '?')
				ret.first += ten[i] * (s1[i] - '0');
			if (s2[i] != '?')
				ret.second += ten[i] * (s2[i] - '0');
			else
				ret.second += ten[i] * 9;
		}
	} else {
		// s1 prefix < s2 prefix
		rep2(i,from,n)
		{
			if (s1[i] != '?')
				ret.first += ten[i] * (s1[i] - '0');
			else
				ret.first += ten[i] * 9;
			if (s2[i] != '?')
				ret.second += ten[i] * (s2[i] - '0');
		}
	}
	return ret;
}

pll solve(ll a, ll b, int i, int d1, int d2) {
	pll ret = mp(a, b);
	ret.first += ten[i] * d1;
	ret.second += ten[i] * d2;
	pll temp;
	if (d1 > d2)
		temp = solve(i + 1, 1);
	else
		temp = solve(i + 1, 0);
	ret.first += temp.first;
	ret.second += temp.second;
	return ret;
}

vll best(vll cur, pll temp) {
	vll ret(3);
	ret[1] = temp.first;
	ret[2] = temp.second;
	ret[0] = abs2(ret[1] - ret[2]);
	if (!sz(cur) || ret < cur)
		return ret;
	return cur;
}

int main() {
	/*freopen("a.txt", "wt", stdout);
	cout << 200 << endl;
	rep(i,200)
	{
		rep(j,18)
		{
			if (rand() % 5)
				cout << "?";
			else
				cout << rand() % 10;
		}
		cout << " ";
		rep(j,18)
		{
			if (rand() % 5)
				cout << "?";
			else
				cout << rand() % 10;
		}
		cout << endl;
	}
	return 0;*/
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
#endif
	cin >> N;
	rep2(nn,1,N+1)
	{
		cout << "Case #" << nn << ": ";
		cin >> s1 >> s2;
		n = sz(s1);
		ten[n - 1] = 1;
		for (int i = n - 2; i >= 0; i--)
			ten[i] = ten[i + 1] * 10;
		int diff = 0;
		while (diff < n
				&& (s1[diff] == '?' || s2[diff] == '?' || s1[diff] == s2[diff]))
			diff++;
		if (diff == n) {
			rep(i,n)
				if (s1[i] == '?' && s2[i] == '?')
					s1[i] = s2[i] = '0';
				else if (s1[i] == '?')
					s1[i] = s2[i];
				else
					s2[i] = s1[i];
			cout << s1 << " " << s2 << endl;
			continue;
		}
		vll ret;
		ll a = 0, b = 0;
		rep(i,diff+1)
		{
			if (s1[i] == '?' || s2[i] == '?' || s1[i] != s2[i]) {
				if (s1[i] == '?' && s2[i] == '?') {
					ret = best(ret, solve(a, b, i, 0, 1));
					ret = best(ret, solve(a, b, i, 1, 0));
				} else if (s1[i] == '?') {
					int d = s2[i] - '0';
					if (d)
						ret = best(ret, solve(a, b, i, d - 1, d));
					if (d < 9)
						ret = best(ret, solve(a, b, i, d + 1, d));
				} else if (s2[i] == '?') {
					int d = s1[i] - '0';
					if (d)
						ret = best(ret, solve(a, b, i, d, d - 1));
					if (d < 9)
						ret = best(ret, solve(a, b, i, d, d + 1));
				} else {
					ret = best(ret, solve(a, b, i, s1[i] - '0', s2[i] - '0'));
				}
			}
			if (s1[i] != '?' && s2[i] != '?') {
				a += ten[i] * (s1[i] - '0');
				b += ten[i] * (s2[i] - '0');
			} else if (s1[i] != '?' && s2[i] == '?') {
				a += ten[i] * (s1[i] - '0');
				b += ten[i] * (s1[i] - '0');
			} else if (s1[i] == '?' && s2[i] != '?') {
				a += ten[i] * (s2[i] - '0');
				b += ten[i] * (s2[i] - '0');
			}
		}

		cout << tos(ret[1]) << " " << tos(ret[2]) << endl;

#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
