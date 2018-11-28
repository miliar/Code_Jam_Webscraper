/*************************************************************************

       Author:            palayutm
       Created Time :     Sat 28 May 2016 10:43:28 PM CST

       File Name:         b.cc
       Description:       new style, new life

 ************************************************************************/
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define PB push_back
#define SIZE(x) (int)x.size()
#define clr(x,y) memset(x,y,sizeof(x))
#define MP(x,y) make_pair(x,y)
#define ALL(t) (t).begin(),(t).end()
#define FOR(i,n,m) for (int i = n; i <= m; i ++)
#define ROF(i,n,m) for (int i = n; i >= m; i --)
#define RI(x) scanf ("%d", &(x))
#define RII(x,y) RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;

const ll mod = 1e9+7;
const ll LINF = 1e18;
const int INF = 1e9;
const double EPS = 1e-8;

/**************************************END************************************/

double dp[205][205];
double a[205];

double cal (vector<double> vec){
	clr (dp, 0);
	dp[0][0] = 1;
	int n = SIZE (vec);
//	FOR (i, 0, SIZE (vec)-1){
//		cout << vec[i] << " ";
//	}
//	cout << endl; 
	FOR(i, 1, n){
		double tt = vec[i-1];
		FOR (j, 0, i){
			int k = i-j;
			if (j == 0){
				dp[j][k] = dp[j][k-1]*tt;
				//cout << j << " " << k << endl;
				//cout << dp[j][k] << endl;
			}else if (k == 0){
				dp[j][k] = dp[j-1][k] *(1-tt);
			}else{
				dp[j][k] = dp[j-1][k] * (1-tt) + dp[j][k-1] * tt;
			}
		}
	}
//	cout << dp[1][0] << endl;
	return dp[n/2][n/2];
}

int main (){
	int T;
	cin >> T;
	FOR (cas, 1, T){
		int n, k;
		cin >> n >> k;
		FOR (i, 1, n){
			cin >> a[i];
		}
		double ans = 0;
		FOR (i, 0, (1<<n)-1){
			int cnt = 0;
			vector<double> vec;
			FOR (j, 0, n-1){
				if((1<<j)&i){
					cnt ++;
					vec.PB (a[j+1]);
				}
			}
			if (cnt == k){
				ans = max(ans, cal(vec));
			}
		}
		printf ("Case #%d: %.8f\n", cas, ans);
	}
}

