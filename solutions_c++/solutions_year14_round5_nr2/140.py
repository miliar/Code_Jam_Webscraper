// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#define dibs reserve
#define OVER9000 1234567890LL
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-10
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) ((x < 0)?-(x):x)
#define uint unsigned int
using namespace std;
// mylittledoge

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	srand(time(0));
	int T;
	cin >> T;
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		int N,P,Q;
		int H =204;
		cin >> P >> Q >> N;
		vector< pair<int,int> > M(N+1,make_pair(0,0));
		for(int i =0; i < N; i++) cin >> M[i].ff >> M[i].ss;

		vector< vector< vector<int> > > ans(N+1,vector< vector<int> >(H,vector<int>(1000+tisic,-100000000)));
		// 3. cislo: zasoba hitov
		ans[0][M[0].ff][0] =0;
		for(int i =0; i < N; i++) for(int j =H-1; j >= 0; j--) for(int k =0; k <= 1000; k++) {
			// pouzi zvysny hit
			if(k > 0) {
				int h2 =j-P;
				if(h2 <= 0) ans[i+1][M[i+1].ff][k-1] =max(ans[i+1][M[i+1].ff][k-1],ans[i][j][k]+M[i].ss);
				else ans[i][h2][k-1] =max(ans[i][h2][k-1],ans[i][j][k]);}
			// skip
			int h2 =j-Q;
			if(h2 <= 0) ans[i+1][M[i+1].ff][k+1] =max(ans[i+1][M[i+1].ff][k+1],ans[i][j][k]);
			else ans[i][h2][k+1] =max(ans[i][h2][k+1],ans[i][j][k]);
			// hit
			h2 =j-P;
			if(h2 > 0) {
				int h3 =h2-Q;
				// tower hit
				if(h3 > 0) ans[i][h3][k] =max(ans[i][h3][k],ans[i][j][k]);
				// tower crit
				else ans[i+1][M[i+1].ff][k] =max(ans[i+1][M[i+1].ff][k],ans[i][j][k]);}
			// crit
			if(h2 <= 0) {
				if(i+1 == N) ans[N][0][k] =max(ans[N][0][k],ans[i][j][k]+M[i].ss);
				else {
					int h3 =M[i+1].ff-Q;
					// tower hit
					if(h3 > 0) ans[i+1][h3][k] =max(ans[i+1][h3][k],ans[i][j][k]+M[i].ss);
					// tower crit
					else ans[i+2][M[i+2].ff][k] =max(ans[i+2][M[i+2].ff][k],ans[i][j][k]+M[i].ss);}
				}
			}
		int ansR =0;
		for(int i =0; i <= 1001; i++) ansR =max(ansR,ans[N][0][i]);
		cout << ansR << "\n";}
	return 0;}

// look at my code
// my code is amazing
