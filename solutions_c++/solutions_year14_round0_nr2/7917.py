#include<bits/stdc++.h>

#define foreach(it,v) for (__typeof((v).begin()) it = (v).begin(); it != (v).end(); it++)
#define MP(a,b) make_pair((a),(b))
#define __input ios::sync_with_stdio(false), cin.tie(0)

template <class T> void Cmin(T &t,T x){if (x < t) t = x;}
template <class T> void Cmax(T &t,T x){if (x > t) t = x;}
template <class T> T sqr(T a) {return a * a;}

using namespace std;

typedef long long LL;
typedef vector<string> VS;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef pair<double, double> PDD;

const double PI = acos(-1.0);
const double EPS = 1e-6;
const int INF = 0x3FFFFFFF;
const int MOD = 1000000007;
const int P = 9875321;

int main()
{		
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; cas++){
		double C, F, X;
		cin >> C >> F >> X;
		double ans = X / 2.0, now = 2.0, last = 0.0;
		while(1){
			last += C / now;
			now += F;
			double delta = last + X / now;
			if (delta >= ans) break;
			ans = delta;
		}
		printf("Case #%d: %.7f\n", cas, ans);
	}
    return 0;
}
