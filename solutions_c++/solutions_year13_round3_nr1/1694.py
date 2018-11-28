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

#define REP(i, a, n) for(int (i) = (a); (i) < (n); ++(i))

int nextInt() {
	int x; scanf("%d", &x); return x;
}
long long nextLong() {
	//long long x; scanf("%I64d", &x); return x;
	long long x; cin >> x; return x;
}

const int BUFSIZE = 1000000;
char buf[BUFSIZE + 1];
string nextString() {
	scanf("%s", buf); return buf;
}

bool IsConsonant(char c)
{
	return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}

vector<int> ToV(const string& s)
{
	const int n = s.size();
	vector<int> v(n, 0);
	REP(i, 0, n) v[i] = (int)IsConsonant(s[i]);
	return v;
}

void SolveCase()
{
	string s = nextString();
	vector<int> v = ToV(s);
	const int vn = v.size();
	const int N = nextInt();
	int ans = 0;
	REP(i, 0, vn) REP(j, i, vn)
	{
		int a = 0;
		int b = 0;
		for(int k = i; k <=j; ++k)
		{
			if(v[k] == 1) a += v[k];
			if(v[k] == 0 || k == j)
			{
				if(a >= N) ++b;
				a = 0;
			}
			//cout << s[k];
		}
		if(b) ++ans;
		//cout << b << endl;
	}
	cout << ans << endl;
}

int main()
{
	int n = nextInt();
	REP(i, 0, n){ cout << "Case #" << i+1 << ": "; SolveCase(); }
	return 0;
}
