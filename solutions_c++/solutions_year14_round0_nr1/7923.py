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
const double EPS = 1e-9;
const int INF = 0x3FFFFFFF;
const int MOD = 1000000007;
const int P = 9875321;

int a[5][5], b[5][5];

int main()
{	
	int T, A, B;
	cin >> T;
	for (int cas = 1; cas <= T; cas++){
		cin >> A; 
		for (int i = 1; i <= 4; i++){
			for (int j = 1; j <= 4; j++){
				cin >> a[i][j];
			}
		}
		cin >> B; 
		for (int i = 1; i <= 4; i++){
			for (int j = 1; j <= 4; j++){
				cin >> b[i][j];
			}
		}
		int cnt = 0, ans;
		for (int i = 1; i <= 4; i++){
			for (int j = 1; j <= 4; j++){
				if (a[A][i] == b[B][j]){
					ans = a[A][i];
					cnt++;
				}
			}
		}
		if (cnt == 0){
			printf("Case #%d: Volunteer cheated!\n", cas);
		}
		if (cnt == 1){
			printf("Case #%d: %d\n", cas, ans);
		}
		if (cnt > 1){
			printf("Case #%d: Bad magician!\n", cas);
		}
	}
	
    return 0;
}
