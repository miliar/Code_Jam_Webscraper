#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <ctime>
#include <cstring>
#include <sstream>

//#include <unordered_map>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<pii, pii> ppii;
typedef vector<int> vi;


#define SI(n) scanf("%d", &n)
#define SII(x, y) scanf("%d%d", &x, &y)
#define SD(n) scanf("%lf", &n)
#define SPII(n) scanf("%d%d", &n.first, &n.second)
#define FI(n) for (int i=0; i<n; i++)
#define WS(n) while(SI(n) != EOF && n)
#define DB(n) cout<<#n<<" = "<<n<<" ";
#define DBN(n) cout<<#n<<" = "<<n<<"\n";
#define FIX(n) cout.precision(2), cout.setf(cout.fixed)
#define PI(n) printf("%d", n)
#define SPACE() putchar(' ')
#define ENDL() putchar('\n')

char s[1000001];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	SI(t);
	for (int j=1; j<=t; j++) {
		int n;
		SI(n);
		scanf("%s", &s);
		int curlvl = 0;
		int ans = 0;
		for (int i = 0; i <= n; i++) {
			if (i > curlvl) {
				ans += i - 
					curlvl;
				curlvl = i;
			}
			curlvl += s[i] - '0';
		}
		printf("Case #%d: %d\n", j, ans);
	}

	getchar(); getchar();
//	cin.get(); cin.get();
	return 0;
}