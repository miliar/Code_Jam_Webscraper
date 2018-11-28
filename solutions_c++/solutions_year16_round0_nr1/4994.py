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

	int T, N, x, tst = 1; S(T);
	int ans;
	bool flag[10];
	bool all;

	while(T--){

		S(N);
		ans = 0;

		if(!N){
			printf("Case #%d: INSOMNIA\n", tst++);
			continue;
		}

		x = N;

		M(flag, false);

		while(true){

			all = true;
			F(j,0,10){

				if(to_string(x).find(to_string(j)) != std::string::npos){
					flag[j] = true;
				}
			}

			F(j,0,10){
				if(!flag[j]) all = false;
			}

			if(all){
				ans = x;
				break;
			}

			x += N;
		}

		printf("Case #%d: %d\n", tst++, ans);
	}
}
