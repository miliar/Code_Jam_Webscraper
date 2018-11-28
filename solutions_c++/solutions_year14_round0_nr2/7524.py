#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>

#define f first
#define s second
#define ll long long
#define mp make_pair
#define pb push_back
#define pii pair < int, int >
#define pll pair < long long, long long >
#define forit(it,S) for(typeof(S.begin()) it = S.begin(); it!= S.end(); it++)

using namespace std;
int const maxn = (int)1e5 + 111;
int const inf = (1<<30) - 1;

void Solve(){
	double C, F, X;
	cin >>C>>F>>X;

	double rate = 2.0;
	double sum = 0.0;
	while ( true ){
		double t = C/rate;
		if ( X/(rate+F) + t < X/rate ){
			rate += F;
			sum += t;
		}
		else {
			printf("%.7f\n", sum + X/rate);
			return;
		}
	}

}

int main (){
	#ifdef LOCAL
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	#endif

	int tests;
	scanf("%d", &tests);

	for (int i=0;i<tests;i++){
		printf("Case #%d: ",i+1);
		Solve();
	}








	return 0;
}






