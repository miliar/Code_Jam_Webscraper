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
		freopen("in.in", "r", stdin);
		freopen("out.out", "w", stdout);
		int tc; cin >> tc;
		for (int t = 1; t <= tc; t++)
		{
			cout << "Case #1:" << endl;
			int n, limit; cin >> n >> limit;
			ll ans = 0;
			for (int i = 1; i < (1 << n); i++)
			{
				if ((i & 1) && (i&(1 << (n - 1))))
				{
					vector<ull> sol(11); bool foundnum = 1;
					for (int base = 2; base <= 10; base++)
					{
						ull num = 0, mul = 1;
						for (int j = 0; j < n; j++)
						{
							if (i & (1 << j)) num += mul;
							mul *= base;
						}

						for (ull div = 2; div*div <= num; div++)
						{
							if ((num % div) == 0) { sol[base] = div; break; }
						}
						if (!sol[base]) { foundnum = 0; break; }
					}
					if (foundnum)
					{
						ans++;
						string s = "";
						for (int j = 0; j < n; j++)
						{
							if (i & (1 << j)) s += "1";
							else s += "0";
						}
						reverse(s.begin(), s.end());
						cout << s << " ";
						for (int pr = 2; pr <= 10; pr++)
						{
							cout << sol[pr];
							if (pr != 10) cout << " ";
						}
						cout << endl;
					}
				}

				if (ans == limit) break;
			}

		}
		return 0;
	}