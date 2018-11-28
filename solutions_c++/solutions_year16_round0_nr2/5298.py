	#include <iostream>
	#include <cstring>
	#include <cstdio>
	#include <ctime>
	#include <algorithm>
	#include <string>
	#include <vector>
	#include <queue> 
	#include <stack>
	#include <deque> 
	#include <set>
	#include <map>
	#include <list>
	#include <utility>
	#include <bitset>
	#include <stdio.h>
	#include <iomanip>
	#include <climits>
	#include <cmath>
	#include <functional>
	#include <sstream>
	#include <math.h>
	#include <stdio.h>


	#define FOR(i,n) for(int i=0; i<n ; i++)
	#define pi 3.14159265358979323846
	#define mp make_pair
	#define pb push_back
	#define all(x) (x).begin(), (x).end()
	#define F first
	#define S second
	typedef long long ll;
	typedef unsigned long long ull;
	typedef long double ld;
	const double EPS = 1e-9;
	const int MOD = 1000003;
	const int INF = 2000 * 1000 * 1000;
	using namespace std;
	int popcount(int n) { bitset<32> b(n); return b.count(); }
	long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }
	int lcm(int a, int b) { int temp = gcd(a, b); 	return temp ? (a / temp * b) : 0; }
	template <typename T>
	T modpow(T base, T exp, T modulus) { base %= modulus; T result = 1; while (exp > 0) { if (exp & 1) result = (result * base) % modulus; base = (base * base) % modulus; exp >>= 1; } return result; }
	inline bool isInteger(const std::string & s){if (s.empty() || ((!isdigit(s[0])) && (s[0] != '-') && (s[0] != '+'))) return false; char * p; strtol(s.c_str(), &p, 10);return (*p == 0);}
		
	
	int main()
	{
		freopen("B-large.in", "r", stdin);
		freopen("out.out", "w", stdout);

		int tc; cin >> tc;
		for (int j = 1; j <= tc; j++)
		{
			string s; cin >> s;
			ll ans = 0;
			if (s[0] == '-') ans++;
			for (int i = 1; i < s.length(); i++)
			{
				if (s[i] == '-' && s[i - 1] == '+') ans += 2;
			}
			cout << "Case #"<<j<<": ";
			cout << ans << endl;
		}

		return 0;
	}