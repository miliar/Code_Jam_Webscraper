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

int arr[10];

int solve(){

	int mx, ret;

	for(int i = 9; i >= 1; i--){
		
		if(arr[i]){

			mx = i;
			break;
		}
	}

	ret = mx;

	if(arr[mx] >= (mx/2)) return mx;

	F(i,1,(mx/2)+1) {

		arr[mx]--;
		arr[i]++;
		arr[mx-i]++;

		ret = min(ret, 1+ solve());

		arr[mx]++;
		arr[i]--;
		arr[mx-i]--;
	}

	return ret;
}

int main(){
	
	int T, D; S(T);

	int tst = 1, temp, ans;
	bool e;

	while(T--){

		M(arr,0);
		ans = 0;
		e = false;

		S(D);

		F(i,0,D){

			S(temp);
			arr[temp]++;
		}

		ans = solve();
		
		printf("Case #%d: %d\n", tst++, ans);
	}
}