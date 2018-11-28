#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <string.h>


using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi = acos(-1.0);
const double eps = 1e-11;
template<class T> inline void checkmin(T &a, T b){ if (b<a) a = b; }
template<class T> inline void checkmax(T &a, T b){ if (b>a) a = b; }
template<class T> inline T sqr(T x){ return x*x; }
typedef pair<int, int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)

template<class T> 
T exgcd(T a, T b, T *s, T *t)
{
	if (T(0) == b)
	{
		if (s) *s = T(1);
		if (t) *t = T(0);
		return a;
	}
	T k, r;
	k = a / b;
	r = a % b;
	T gcd = exgcd(b, r, s, t);
	T tmp;
	if (s && t)
	{
		tmp = *t;
		*t = *s - *t * k;
		*s = tmp;
	}
	return gcd;
}
template<class T>
T mpow(T a, T n, T mod)
{
	if (n == T(0)) return T(1);
	T tmp = mpow(a, n / T(2), mod);
	tmp = (tmp * tmp) % mod;
	return (((n % T(2)) ? a : T(1)) * tmp) % mod;
}
template<class T>
bool is_prime(T n)
{
	T list[] = { T(2), T(3), T(61) };
	T d(n - 1);
	int s = 0;
	while (0 == (d % T(2)))
	{
		d /= T(2);
		s++;
	}
	T x;
	for (int i = 0; i < sizeof(list) / sizeof(T); ++i)
	{
		if (list[i] > n - 2) break;
		x = mpow(list[i], d, n);
		if (T(1) == x || n - T(1) == x) continue;
		bool ok = false;
		for (int j = 0; j < s - 1; ++j)
		{
			x *= x;
			x %= n;
			if (x == T(1)) return false;
			if (x == T(n - 1))
			{
				ok = true;
				break;
			}
		}
		if (!ok) return false;
	}
	return true;
}

int getmax(int a[],int n) {
	int re = 0;
	for (int i = 0; i < n; ++i) {
		if (a[i] > a[re]) re = i;
	}
	return re;
}
int getmin(int a[], int n) {
	int re = 0;
	for (int i = 0; i < n; ++i) {
		if (a[i] < a[re]) re = i;
	}
	return re;
}




#include <fstream>
int t;
int smax;
char s[1010];

int main()
{
	//freopen("input.txt","r",stdin);
	std::ios::sync_with_stdio(false);
	
	//ofstream log("1.txt");
	//cout.rdbuf(log.rdbuf());
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	cin >> t;
	for (int i = 0; i < t; ++i) {
		cin >> smax;
		cin >> s;
		int ac = 0;
		int add = 0;
		for (int i = 0; i <= smax; ++i) {
			if (ac >= i) {
				ac += s[i] - '0';
			}
			else {
				add += i - ac;
				ac += i - ac + s[i] - '0';
			}
		}
		cout << "Case #" << i + 1 << ": " << add << endl;
	}


	return 0;
}


