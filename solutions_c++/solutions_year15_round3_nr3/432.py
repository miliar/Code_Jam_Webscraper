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
#define SIII(x, y, z) scanf("%d%d%d", &x, &y, &z)
#define SD(n) scanf("%lf", &n)
#define SPII(n) scanf("%d%d", &n.first, &n.second)
#define FI(n) for (int i=0; i<n; i++)
#define FJ(n) for (int j=0; j<n; j++)
#define WS(n) while(SI(n) != EOF && n)
#define DB(n) cout<<#n<<" = "<<n<<" ";
#define DBN(n) cout<<#n<<" = "<<n<<"\n";
#define FIX(n) cout.precision(2), cout.setf(cout.fixed)
#define PI(n) printf("%d", n)
#define SPACE() putchar(' ')
#define ENDL() putchar('\n')
#define in_count(a, n, x) (upper_bound(a, a+n, x) - lower_bound(a, a+n, x) + 1)


#define x first
#define y second

const int N = 200010;


typedef pair < ll, char > plc;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	SI(t);
	for (int i=1; i<=t; i++) {
		int C, D, V;
		SIII(C, D, V);
		//C - limit
		//D - was
		//V - max
		
		set<int> st;
		for (int i = 0; i < D; i++) {
			int x;
			SI(x);
			for (std::set<int>::reverse_iterator it = st.rbegin(); it != st.rend(); it++)
				st.insert(x + (*it));
			st.insert(x);
		}

		int answer = 0;
		for (int i = 1; i <= V; i++)
			if (st.find(i) == st.end()) {
				int x = i;
				answer++;
				for (std::set<int>::reverse_iterator it = st.rbegin(); it != st.rend(); it++)
					st.insert(x + (*it));
				st.insert(x);
			}

		printf("Case #%d: %d\n",  i, answer);
	}


	cin.get(); cin.get();
	return 0;
}