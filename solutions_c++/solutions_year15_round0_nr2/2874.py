#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>
#include <queue>
#include <complex>

#define INF 1145141919
#define INF_INT_MAX 2147483647
#define INF_LL_MAX 9223372036854775807
#define EPS 1e-10
#define Pi acos(-1)
#define LL long long
#define ULL unsigned long long

using namespace std;

#define MAX_D 1005
#define MAX_P 1005

string mPass = "C:\\C\\pra\\Debug\\";

int D;
int P[MAX_D];
int dp[MAX_D][MAX_P];

int main(){

	ifstream ifs(mPass + "input.in");
	ofstream ofs(mPass + "output.out");

	int T;

	ifs >> T;

	for (int testCase = 1; testCase <= T; testCase++){

		memset(dp, 0, sizeof(dp));

		int ans = INF;

		ifs >> D;
		for (int i = 0; i < D; i++){
			ifs >> P[i];
		}

		for (int i = 0; i < D; i++){
			for (int j = 1; j <= 1000; j++){
				if (P[i] <= j)
					dp[i + 1][j] = dp[i][j];
				else{
					dp[i + 1][j] = dp[i][j] + (P[i] - 1) / j;
				}
			}
		}

		for (int j = 1; j <= 1000; j++){
			ans = min(ans, dp[D][j] + j);
		}

		ofs << "Case #" << testCase << ": " << ans;
		if (testCase <= T - 1)
			ofs << endl;

	}

	ifs.close();
	ofs.close();

	return 0;

}