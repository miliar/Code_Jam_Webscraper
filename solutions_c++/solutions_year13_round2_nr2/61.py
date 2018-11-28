/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <bitset>
#include <iomanip>
#include <utility>

using namespace std;

typedef long long LL;
typedef complex<double> point;
typedef long double ldb;
typedef pair<int,int> pii;

int n,X,Y;
long double dp[3000][3000];

inline void main2(){
	cin >> n >> X >> Y;
	long double ret = 0.0;
	X = max(X,-X);
	Y = max(Y,-Y);
	int me = X+Y;
	for (int i=0; true; i+=2){
		if (me == i){
			if (n>=2*i+1){
				ret = 1.0;
				break;
			}
			if (Y==i){
				ret = 0.0;
				break;
			}
			if (i + Y < n){
				ret = 1.0;
				break;
			}
			if (n>=3000 || i>=3000){
				cerr << "BAD WORK" << endl;
				exit(0);
			}
			memset(dp, 0, sizeof dp);
			dp[0][0] = 1.0;
			for (int j=0; j<n; j++){
				for (int k=0; k<=min(i,j); k++){
					if (k!=i)
						dp[j+1][k+1]+= (j-k!=i) ? (dp[j][k]/2.0) : (dp[j][k]);
					if (j-k!=i)
						dp[j+1][k]+= (k!=i) ? (dp[j][k]/2.0) : (dp[j][k]);
				}
			}
			ret = 0.0;
			for (int j=Y+1; j<=i; j++)
				ret+= dp[n][j];
			break;
		}else if (n <= 2 * i + 1){
			ret = 0;
			break;
		}else
			n-=(2*i+1);
	}
	cout << fixed << setprecision(9) << ret << endl;
}

int main(){
	int testCase; cin >> testCase;
	for (int o=1; o<=testCase; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
