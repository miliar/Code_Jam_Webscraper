//#pragma comment(linker, "/STACK:134217728")
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

typedef pair<int, int> PII;
typedef vector<int> VI;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define MOD 1000000009
#define INF 1000000007
#define y1 agaga
#define ll long long
#define ull unsigned long long


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	FOR(T, 0, t) {
		cout << "Case #" << T + 1 << ": ";
		string s,t="";
		cin >> s;
		int j = s.size() - 1;
		while (j >= 0 && s[j] == '+') --j;
		FOR(i, 0, j + 1) {
			if (i==0 || s[i] != s[i - 1]) {
				t += s[i];
			}
		}
		cout << t.size() << endl;


	}

	return 0;
}