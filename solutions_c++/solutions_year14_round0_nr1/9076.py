#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,a,b) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 1e9
#define eps 1e-9
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
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("o.txt", "wt", stdout);
#endif
	int cs = 1, t, x, y, a[4][4], b[4][4];
	cin >> t;
	while (t--) {
		vector<int> v;
		cin >> x;
		FOR(i , 0 , 4)
			FOR(j , 0 , 4)
			{
				cin >> a[i][j];
				if (i + 1 == x)
					v.pb(a[i][j]);
			}

		cin >> y;
		FOR(i , 0 , 4)
			FOR(j , 0 , 4)
			{
				cin >> b[i][j];
				if (i + 1 == y)
					v.pb(b[i][j]);
			}
		sort(all(v));
		int cnt = 0 , res;
		FOR(i , 0 , sz(v)-1)
			if(v[i] == v[i+1])
				cnt++ , res = v[i];
		printf("Case #%d: ",cs++);
		if(cnt == 0)
			printf("Volunteer cheated!\n");
		else if (cnt == 1)
			printf("%d\n" ,res);
		else
			printf("Bad magician!\n");


	}
	return 0;
}
