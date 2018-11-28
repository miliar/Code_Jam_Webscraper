#include <iostream>
#include <string>
#include <iomanip>
#include <stdio.h>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; ++i)
#define rep2(i, x, n) for (int i = x; i < n; ++i)
#define repd(i, n) for (int i = n - 1; i >= 0; --i)
#define repd2(i, x, n) for (int i = n - 1; i >= x; --i)
#define _(a, b) memset(a, b, sizeof(a))
int ri() { int a; scanf( "%d", &a ); return a; }
double rf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; 
string rs() { scanf( "%s", sbuf ); return sbuf; }
long long rll() { long long a; scanf( "%lld", &a ); return a; }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;
typedef map<string,string> mss;

bool isPalindrome(int i)
{
	char ch[100];
	itoa(i, ch, 10);
	string s(ch);
	if (s.size() == 1) return true;
	int j = 0;
	for (; j < s.size() / 2; j++)
	{
		if (s[j] != s[s.size()-1-j])
			break;
	}
	if (j == s.size() / 2)
		return true;
}

int main()
{
	freopen("C:\\Users\\Administrator\\Desktop\\C-small-attempt0.in","rt",stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\C-large-practice.out","wt",stdout);
	
	int T = ri();
	vector<string> v;
	rep(t, T)
	{
		ll start = ri();
		ll end = ri();
		int count = 0;
		for (ll i = start; i <= end; i++)
		{
			if (!isPalindrome(i))
				continue;
			float b=pow(10,-6.0);
			float sqr = sqrt(i*1.0);
			if (sqr - int(sqr) > b || sqr - int(sqr) < -b)
				continue;
			if (!isPalindrome(int(sqr)))
				continue;
			count++;
		}

		printf("Case #%d: %d\n", t+1, count);
	}
	return 0;
}


