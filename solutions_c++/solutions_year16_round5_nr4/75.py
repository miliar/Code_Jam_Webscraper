#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <sstream>
#include <fstream>
#include <functional>
#include <cassert>
#include <complex>
#include <valarray>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long ll;
typedef pair<int, int> pii;
#define X first
#define Y second
#define mp make_pair

const int N = (int)1e5 + 10;
int n, l;
string G[N];
string B;

void read()
{
	scanf("%d%d", &n, &l);
	for (int i = 0; i < n; i++)
		cin >> G[i];
	cin >> B;
}

void solve()
{
	for (int i = 0; i < n; i++)
	{
		if (G[i] == B)
		{
			puts("IMPOSSIBLE");
			return;
		}
	}
	if (n == 1)
	{
		for (int i = 0; i < l; i++)
			cout << G[0][i] << "?";
		cout << " " << "0" << endl;
	}
	else
	{
		for (int i = 0; i < l; i++)
			cout << "0?";
		cout << " ";
		for (int i = 0; i < l - 1; i++)
			cout << "1";
		cout << endl;
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
