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
	int row1;
	scanf("%d", &row1);
	row1--;
	set < int > S;
	for (int i=0;i<4;i++){
		for (int j=0;j<4;j++){
			int x;
			scanf("%d", &x);
			if ( i == row1 )
				S.insert(x);
		}
	}
	int row2;
	scanf("%d", &row2);
	row2--;
	int ans = -1;
	int cnt = 0;
	for (int i=0;i<4;i++){
		for (int j=0;j<4;j++){
			int x;
			scanf("%d", &x);
			if ( row2 == i){
				if ( S.find(x) != S.end() ){
					ans = x;	
					cnt++;
				}	
			}
		}
	}
	if ( cnt == 0){
		printf("Volunteer cheated!\n");
	}
	else if ( cnt == 1){
		printf("%d\n", ans);
	}
	else
		printf("Bad magician!\n");

}

int main (){
	#ifdef LOCAL
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	#endif

	int tests;
	scanf("%d", &tests);

	for (int i=0;i<tests;i++){
		printf("Case #%d: ", i+1);
		Solve();
	}






	return 0;
}






