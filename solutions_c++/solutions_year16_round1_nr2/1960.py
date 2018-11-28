#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<bitset>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<cstring>
#include<sstream>
#include<climits>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define S(x) scanf("%d",&x)
#define SD(x) scanf("%lf",&x)
#define SL(x) scanf("%lld",&x)
#define pb(x) push_back(x)
#define mp make_pair
#define F(i, a, b) for (int i = int(a); i < int(b); i++)
#define forit(it, a) for (it = (a).begin(); it != (a).end(); it++)
#define M(x,i) memset(x,i,sizeof(x))

/* -------------------CODE GOES HERE---------------------- */

int main(){

	int T, N, temp, n, yo, tst = 1; S(T);
	vi row,y,ans,t;
	vector<vi> rows,x;
	map<int,vi> m;
	bool flag,a;

	while(T--){

		S(N);
		rows.clear();
		x.clear();
		ans.clear();
		a = false;
		n = -1;

		F(i,0,N){
			x.pb(t);
		}

		F(i,0,2*N-1){

			row.clear();

			F(i,0,N){
				S(temp);
				x[i].pb(temp);
				row.pb(temp);
			}

			rows.pb(row);
		}

		F(i,0,N){
			sort(x[i].begin(), x[i].end());
		}

		F(i,0,N){

			if(i!=N-1){
		
				if(x[i][2*i] != x[i][2*i+1]){
					n = i;
					yo = x[i][2*i];
					break;
				}
			}

			if(n == -1){
				n = N-1;
				yo = x[n][2*n];
			}
		}

		F(i,0,2*N-1){

			if(rows[i][n] == yo){
				y = rows[i];
				break;
			}
		}

		ans.pb(yo);

		F(i,0,2*N-1){
			flag = false;
			F(j,0,N){
				if(x[n][i] == y[j]){
					y[j] = 3000;
					flag = true;
					break;
				}
			}
			if(!flag) ans.pb(x[n][i]);
		}

		sort(ans.begin(), ans.end());
		printf("Case #%d:", tst++);
		F(i,0,N){
			printf(" %d", ans[i]);
		}
		printf("\n");
	}
}
