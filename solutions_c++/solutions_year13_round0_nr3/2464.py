#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>

using namespace std;

#define REP(i, n) for(int i = 0; i < n; ++i)

const int MAX_STR_LEN = 120;

int nextInt() {
	int x; scanf("%d", &x); return x;
}
long long nextLong() {
	//long long x; scanf("%I64d", &x); return x;
	long long x; cin >> x; return x;
}

string LongLongToString(long long value)
{
	if(value < 0)
		return string();
	vector<char> v;
	while(v.empty() || (value > 0))
	{
		v.push_back(value % 10 + '0');
		value /= 10;
	}
	reverse(v.begin(), v.end());
	return string(v.begin(), v.end());
}

bool IsPalindrom(const string& s)
{
	const int n = s.length();
	REP(i, n/2)
		if(s[i] != s[n-1-i])
			return false;
	return true;
}

bool IsPalindrom(const long long val)
{
	return IsPalindrom(LongLongToString(val));
}

const long long table[39][2] =
{
{1, 1},
{2, 4},
{3, 9},
{11, 121},
{22, 484},
{101, 10201},
{111, 12321},
{121, 14641},
{202, 40804},
{212, 44944},
{1001, 1002001},
{1111, 1234321},
{2002, 4008004},
{10001, 100020001},
{10101, 102030201},
{10201, 104060401},
{11011, 121242121},
{11111, 123454321},
{11211, 125686521},
{20002, 400080004},
{20102, 404090404},
{100001, 10000200001},
{101101, 10221412201},
{110011, 12102420121},
{111111, 12345654321},
{200002, 40000800004},
{1000001, 1000002000001},
{1001001, 1002003002001},
{1002001, 1004006004001},
{1010101, 1020304030201},
{1011101, 1022325232201},
{1012101, 1024348434201},
{1100011, 1210024200121},
{1101011, 1212225222121},
{1102011, 1214428244121},
{1110111, 1232346432321},
{1111111, 1234567654321},
{2000002, 4000008000004},
{2001002, 4004009004004}
};

void SolveCase()
{
	long long a = nextLong();
	long long b = nextLong();
	long long count = 0;
	for(int i = 0; i < 39; ++i)
	{
		if(a <= table[i][1] && table[i][1] <= b)
			++count;
	}
	cout << count << endl;
}

void SolveCase_2()
{
	long long a = nextLong();
	long long b = nextLong();
	long long count = 0;
	cout << endl;
	for(long long i = static_cast<long long>(sqrt(a)); i*i <= b; ++i)
	{
		const long long x = i*i;
		if(	x < a ||
			!IsPalindrom(i) ||
			!IsPalindrom(x)) continue;
		++count;
		cout << i << " " << x << endl;//!!!
	}
	cout << count << endl;
}

int main()
{
	int n = nextInt();
	REP(i, n){
		cout << "Case #" << i+1 << ": ";
		SolveCase();
	}
	return 0;
}
