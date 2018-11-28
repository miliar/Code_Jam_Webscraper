#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define rep(i, l, r) for(int i = l; i <= r; ++i)
using namespace std;
const int maxn = 210;
int n, m;
double p[maxn];
double q[maxn];
double f[maxn][maxn];
int main(){
	
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	rep(cas, 1, T){
		printf("Case #%d: ", cas);
		cin >> n >> m;
		rep(i, 1, n)
			cin >> p[i];
		sort(p + 1, p + n + 1);
		double ans = 0;
		rep(k, 0, m){
			int tot = 0;
			rep(i, 1, k)
				q[++tot] = p[i];
			rep(i, 1, m - k)
				q[++tot] = p[n - i + 1];
			/*rep(i, 1, tot)	
				printf("q[%d] = %f\n", i, q[i]);
			*/memset(f, 0, sizeof(f));
			f[0][0] = 1; 
			rep(i, 1, tot){
				rep(j, 0, i){
					f[i][j] = f[i - 1][j] * (1 - q[i]);
					if(j > 0){
						f[i][j] += f[i - 1][j - 1] * q[i];
					}
				//	printf("f[%d][%d] = %f\n", i, j, f[i][j]);
				}
			}
			//printf("k = %d f = %f\n", k, f[tot][m >> 1]);
			ans = max(ans, f[tot][m >> 1]);
		}
		printf("%.9f\n", ans);
	}
	return 0;
} 
/*
1
4 2
0.00 0.00 1.00 1.00
*/
