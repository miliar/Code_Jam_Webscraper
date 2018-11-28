#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,a,b) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 1e9
#define eps 1e-7
#define PI 3.14159265358979323846264338327950
#define MAX 2001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define iter(it,s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); it++)

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0.in", "rt", stdin);
		freopen("o.txt", "wt", stdout);
#endif
	int t , cs = 1;
	cin >> t;
	while(t--) {
		long double c , f , x , res , lst = -1;
		cin >> c >> f >> x;
		res = x / 2.0;
		int n = 1;
		while(true) {
			if(res - lst > eps && lst != -1) {
				printf("Case #%d: %.7lf\n" ,cs ++ ,(double) lst);
				break;
			}
			long double cnt = 0 , cur_f = 2.0;
			FOR(i , 0 , n) {
				cnt += c / cur_f;
				cur_f += f;
			}
			lst = res;
			res = cnt + (x / cur_f);
			n++;
		}
	}
	return 0;
}
