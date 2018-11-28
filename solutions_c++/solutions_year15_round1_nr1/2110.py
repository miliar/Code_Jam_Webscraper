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
	
	int T, N; S(T);
	int tst = 1;
	int y,z;
	int curr, prev, diff;
	vi cakes;

	while(T--){

		S(N);
		prev = y = z = diff = 0;
		cakes.clear();

		F(i,0,N){
			S(curr);
			cakes.pb(curr);
			
			if(curr < prev){
				y += (prev - curr);
				diff = max(diff, (prev - curr));
			}

			prev = curr;
		}

		F(i,0,N-1){
			z += min(cakes[i], diff);
		}

		printf("Case #%d: %d %d\n", tst++, y, z);
	}
}