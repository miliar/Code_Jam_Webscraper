#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>
#include <iostream>
#include <sstream>
#include <cctype>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> ii;

void solve()
{
    string s, t = "";
    cin >> s;
    for(char& c : s)
    {
        if (s.size() == 0 || t[0] > c)
            t += c;
        else
            t = c + t;
    }
    cout << t << endl;
}

int main() {
	int T;
	scanf("%d", &T);
	REP(t, T)
	{
		printf("Case #%d: ", t+1);
		solve();
	}
	return 0;
}
