#include <iostream>
#include <set>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

//#define SMALL
#define LARGE

bool is_squar(const long long&);
bool is_palindrome(const long long&);

const long long N = 100000000;

struct node {
	char a[105];
};
char dig[105];
vector <node> ns;
vector <long long> as;
long long ans[] = {
1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004,
100000020000001,
100220141022001,
102012040210201,
102234363432201,
121000242000121,
121242363242121,
123212464212321,
123456787654321,
400000080000004,
0
};

bool is_squar(const long long& num) {
	long long temp = num;
  temp = (long long)sqrt(temp);
  if (temp * temp == num)
		return is_palindrome(temp);
	return false;
}

bool is_palindrome(const long long& num) {
	int len = 0;
	long long temp = num;
	while (temp) {
		dig[len++] = temp % 10;
		temp /= 10;
	}
	int len0 = ((len + 1) >> 1);
	for (int i = 0; i < len0; ++i)
		if (dig[i] != dig[len - i - 1])
			return false;
	return true;
}

void reserve(string& a) {
	int len = a.length();
	int len0 = (len + 1) / 2;
	char temp;
	for (int i = 0; i < len0; ++i) {
		temp = a[i];
		a[i] = a[len - i - 1];
		a[len - i - 1] = a[i];
	}
}

string operator * (const string& a, const string& b) {
	string a0 = a;
	string b0 = b;
  reserve(a0);
	reserve(b0);
	int len1 = a0.length();
	int len2 = b0.length();
	string ret(len1 + len2 + 1, 0);
	for (int i = 0; i < len1; ++i)
		for (int j = 0; j < len2; ++j)
			ret[i + j] += (a0[i] - '0') * (b0[i] - '0');
	for (int i = 0; i < len1 + len2; ++i)
		ret[i] += '0';
	reserve(ret);
	return ret;
}

void dfs(char* s, char insert, bool has_two, int len) {
	s[len] = insert;
	if (insert == '2') {
		/*if (!has_two) {
			node temp;
			memcpy(temp.a, s, len);
			ans.push_back(temp);
		}*/
		return;
	}
	if (len == 24)
		return;
	for (int i = 0; i < 3; ++i)
		dfs(s, i + '0', has_two, len + 1);
}

int main()
{
#ifdef SMALL
	freopen("C_small.in", "r", stdin);
	freopen("C_small.out", "w", stdout);
#endif

#ifdef LARGE
	freopen("C_large1.in", "r", stdin);
	freopen("C_large1.out", "w", stdout);
#endif
  int cnt = 0;
/*	for (long long i = 1; i <= N; ++i)
		if (is_palindrome(i) && is_palindrome(i * i))
			//ans[cnt++] = i * i;
			printf("%lld %lld\n", i, (long long)i * i);*/
	int t;
	long long a, b;
	cin >> t;
	for (int Case = 0; Case != t; ++Case) {
		cin >> a >> b;
		int ans_number = 0;
		for (int i = 0; i < 100 && ans[i] != 0; ++i)
			if (ans[i] >= a && ans[i] <= b)
				ans_number++;
		printf("Case #%d: %d\n", Case + 1, ans_number);
	}
/*	char a[105];
	a[0] = '0';
  for (int i = 0; i < 3; ++i)
    dfs(a, i + '0', false, 1);
  for (int i = 0; i < 3; ++i)
	  dfs("1", i + '0', false, 1);
  for (int i = 0; i < 3; ++i)
    dfs("2", i + '0', true, 1);
  for (int i = 0; i < 3; ++i)
	  dfs("00", i + '0', false, 0);
  for (int i = 0; i < 3; ++i)
	  dfs("11", i + '0', false, 0);*/
	return 0;
}
