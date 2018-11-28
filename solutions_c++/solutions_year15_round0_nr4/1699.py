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
	
	int T, X, R, C; S(T);

	int tst = 1;
	bool ans;

	while(T--){

		ans = false;
		S(X); S(R); S(C);

		if(((R*C) % X) == 0){

			if((X == 1) || (X == 2)) ans = true;
			else if((min(R,C) >= (X-1))) ans = true;
		}

		printf("Case #%d: %s\n", tst++, (ans ? "GABRIEL" : "RICHARD"));
	}
}