#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cassert>
#include <bitset>
#include <fstream>

using namespace std;

#define fst first
#define snd second
#define pb push_back
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double

template<typename T>
T abs(T x) {
	return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
	return x * x;
}

template<typename T>
ostream& operator << (ostream &s, const vector<T> &x) {
	s << "[";
	for (auto it : x) {
		s << it << ", ";
	}
	s << "]";
	return s;
}

template<typename T>
ostream& operator << (ostream &s, const set<T> &x) {
	s << "{";
	for (auto it : x) {
		s << it << ", ";
	}
	s << "}";
	return s;
}


template<typename U, typename V>
ostream& operator << (ostream &s, const pair<U, V> &x) {
	s << "(" << x.fst << ", " << x.snd << ")";
	return s;
}

template<typename T>
bool chmax(T &x, const T &y) {
	if (x < y) {
		x = y;
		return true;
	}
	return false;
}

template<typename T>
bool chmin(T &x, const T &y) {
	if (x > y) {
		x = y;
		return true;
	}
	return false;
}

//---------------------------------------------------------------------

int get_winner(int p, int r, int s)
{
	if (p + r + s == 1)
	{
		if (p)
			return 0;
		if (r)
			return 1;
		return 2;
	}
	if (p % 2 == 0)
	{
		if (p > r)
		{
			return get_winner(p / 2, r / 2, p / 2);
		}
		else
		{
			return get_winner(p / 2, (r + 1) / 2, p / 2);
		}
	}
	if (r % 2 == 0)
	{
		if (r > p)
		{
			return get_winner(r / 2, r / 2, p / 2);
		}
		else
		{
			return get_winner(r / 2, r / 2, (p + 1) / 2);
		}
	}
	if (s % 2 == 0)
	{
		if (s > r)
		{
			return get_winner(r / 2, s / 2, s / 2);
		}
		else
		{
			return get_winner((r + 1) / 2, s / 2, s / 2);
		}
	}
	return 0;
}

string t[] = {"P", "R", "S"};
string dp[3][15];

string get_string(int winner, int n)
{
	if (n == 0)
	{
		return t[winner];
	}
	if (dp[winner][n].length() > 0)
		return dp[winner][n];
	string s1 = get_string(winner, n - 1), s2 = get_string((winner + 1) % 3, n - 1);
	if (s1 > s2)
		swap(s1, s2);
	return dp[winner][n] = s1 + s2;
}

int main() {
	srand(time(NULL));
	#ifdef LOCAL
		//gen();
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
	#else
		//freopen("springs.in", "r", stdin);
		//freopen("springs.out", "w", stdout);
	#endif
	//check();
	
	
	int a, b, c;
	a = 0, b = 1, c = 1;
	set < vector < int > > setic;
	for (int i = 1; i <= 16; i++)
	{
		setic.insert({a, b, c});
		vector < int > v = {a + b, a + c, b + c};
		sort(v.begin(), v.end());
		a = v[0], b = v[1], c = v[2];
	}
	int T;
	cin >> T;
	
	for (int iter = 1; iter <= T; iter++)
	{
		cout << "Case #" << iter << ": ";
		int n, p, r, s;
		cin >> n >> r >> p >> s;
		vector < int > v = {p, r, s};
		sort(v.begin(), v.end());
		if (setic.find(v) == setic.end())
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}
		
		int winner = get_winner(p, r, s);
		//cout << winner << "\n";
		cout << get_string(winner, n) << "\n";
	}
	
	return 0;
}
