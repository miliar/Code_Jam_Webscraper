#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
#define sc(x) scanf("%d", &x)
#define scl(x) scanf("%I64d", &x)
#define loop(i,s,e) for(int i=s ; i<e ; i++)
#define rep(i,s,e) for(int i=s ; i>=e ; i--)
#define INF 1000000
#define MOD 1000000007
#define f first
#define s second
#define EPS 1e-7
#define Rd freopen("in.txt", "r", stdin)
#define Wr freopen("out.txt", "w", stdout)
#define PS push_back
#define M_PI           3.14159265358979323846  /* pi */
#define DFS_WHITE -1
#define DFS_BLACK 0

int main() {
	Rd;
	Wr;
	pair<int, char> arr[30];
	int T; sc(T);
	vector<string> vec;
	loop(t,0,T) {
		vec.clear();
		int n;
		sc(n);
		int sum = 0;
		loop(i,0,n) {
			sc(arr[i].f);
			sum += arr[i].f;
			arr[i].s = i + 'A';
		}
		sort(arr, arr+n, greater< pair<int, char> >());
		printf("Case #%d:", t+1);
		int m = n;
		while(sum > 0) {
			string ans = "";
			ans = arr[0].s;
			arr[0].f--;
			sum--;
			if(sum > 0) {
				if(arr[0].f > arr[1].f) {
					ans += arr[0].s;
					arr[0].f--;
					sum--;
				} else {
					ans += arr[1].s;
					arr[1].f--;
					sum--;
				}				
			}
			sort(arr, arr+m, greater< pair<int, char> >());
			vec.push_back(ans);
			// printf(" %s", ans.c_str());
		}
		int last = vec.size() - 1;
		if( vec[last].size() == 1 ) {
			swap( vec[last], vec[last-1] );
		}
		loop(i,0,vec.size()) {
			printf(" %s", vec[i].c_str());
		}
		printf("\n");
	}
	return 0;
}