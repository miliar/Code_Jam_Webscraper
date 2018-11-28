#pragma comment(linker, "/STACK:10000000000")
#include <map>
#include <unordered_map>
#include <set>
#include <vector>
#include <cstring>
#include <cmath>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <time.h>
#include <iostream>
#include <stdio.h>
#include <queue>
#include <bitset>
#include <random>
#include <iterator>
#include <cassert>
#include <cstdint>
#include <string>
#include <numeric>

using namespace std;

#define LLD "%lld"

void print_str(const char* s)
{
	while (*s != 0)
	{
		putchar(*s);
		s++;
	}
}

template<typename T> void scan(T &t)
{
	cin >> t;
}

template<> void scan<int>(int &t)
{
	scanf("%d", &t);
}

template<> void scan<long long>(long long &t)
{
	scanf(LLD, &t);
}

template<> void scan<string>(string &t)
{
	cin >> t;
}

template<> void scan<char*>(char* &t)
{
	scanf("%s", t);
}

template<> void scan<char>(char &t)
{
	t = getchar();
	while (t <= 32)
		t = getchar();
}

template<> void scan<double>(double &t)
{
	scanf("%lf", t);
}

template<typename T> void scan(vector<T> &t)
{
	for (int i = 0; i < t.size(); i++)
	{
		scan(t[i]);
	}
}


template<typename T, typename... Ts> void scan(T& t, Ts&... ts)
{
	scan(t);
	scan(ts...);
}

template<typename T> void print(T t)
{
	cout << t;
}

template<> void print<string>(string s)
{
	print_str(s.c_str());
}

template<> void print<int>(int t)
{
	printf("%d", t);
}

template<> void print<long long>(long long t)
{
	printf(LLD, t);
}

template<> void print<char>(char t)
{
	putchar(t);
}

template<> void print<const char*>(const char* t)
{
	print_str(t);
}

template<> void print<double>(double t)
{
	printf("%lf", t);
}

template<typename T, typename V> void print(pair<T, V> t)
{
	printf("(");
	print(t.first);
	printf(", ");
	print(t.second);
	printf(")");
}

template<typename T, typename... Ts> void print(T t, Ts... ts)
{
	print(t);
	print(ts...);
}

#define TASK "attract"
#define X first
#define Y second

const int INF = 1e9;
const long long LINF = 3e18;
const int maxN = 10 + 100;
const int maxM = 5000 + 100;
const int K = 3000;
const int SIZE = (1 << 19);
const int mb = 30;
const long long MOD = 1000200013;
const long long P = 1009;
const double EPS = 1e-8;

mt19937_64 random_generator;

long long random(long long l, long long r)
{
	uniform_int_distribution<long long> dist(l, r);
	long long res = dist(random_generator);
	return res;
}

namespace solution
{
}

namespace bruteforce
{
}

void init(bool testing = false)
{

}

char neg(char c)
{
	return c == '-' ? '+' : '-';
}

int solve(string s, int k)
{
	int res = 0;
	int n = s.size();
	for (int i = 0; i <= n - k; i++)
	{
		if (s[i] == '-')
		{
			res++;
			for (int j = 0; j < k; j++)
			{
				s[i + j] = neg(s[i + j]);
			}
		}
	}

	int cnt = 0;
	for (int i = 0; i < n; i++)
	{
		cnt += s[i] == '+';
	}

	if (cnt != n)
		return -1;
	else
		return res;
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//freopen(TASK".in", "r", stdin);
	//freopen(TASK".out", "w", stdout);
#endif

	int t;
	scan(t);
	for (int test = 0; test < t; test++)
	{
		string s;
		int k;
		scan(s, k);
		int res = solve(s, k);
		print("Case #", test + 1, ": ");
		if (res == -1)
			print("IMPOSSIBLE\n");
		else
			print(res, '\n');
	}
	return 0;
}