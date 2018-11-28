/* Aniket Kumar */
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <stack>
#include <queue>
#include <cmath>
#include <unistd.h>
#include <algorithm>
#include <vector>
#include <map>
#include <climits>
#include <set>

using namespace std;

#define V(a) vector<a>
#define pi pair<int,int>
#define ull unsigned long long
#define ill long long
#define F(i,a,n) for(i=(a);i<(n);++i)
#define RP(i,n) F(i,0,n)
#define SUM(v, s, i) RP(i, v.size()){ s += v[i];}
#define MP(a, b) make_pair(a, b)
#define fs first
#define se second
#define S(x) scanf("%d",&x)
#define SL(x) scanf("%lld",&x)
#define SZ(x) (x.size())
#define PB(a) push_back(a)
#define dbug(i,size,x) F(i,0,size){cout<<x[i]<<" ";} cout<<endl

int dp[1003][1003];

int main()
{
	freopen("B-large.in","r",stdin);
 	freopen("B-large.out","w",stdout); 	

 	int ar[1003];

 	int i, j, t, cs, n, k, mx;

 	int cst, tmp;

 	F(i, 1, 1001) {

 		F(j, 1, 1001) {

 			if (j >= i) {
 				break;
 				//dp[i][j] = 0;
 			} else {
 				//dp[i][j] = 1 + dp[(i + 1) / 2][j] + dp[i / 2][j];

 				dp[i][j] = 100000000;

 				F(k, 1, i) {
 					dp[i][j] = min(dp[i][j], 1 + dp[k][j] + dp[i - k][j]);
 				}
 			}
 			
 		}
 	}

 	S(t);

 	F(cs , 1, t + 1) {
 		S(n);

 		mx = 0;

 		F(i, 0, n) {
 			S(ar[i]);

 			if (ar[i] > mx) {
 				mx = ar[i];
 			}
 		}

 		cst = 100000000;

 		F(i, 1, mx + 1) {

 			tmp = 0;

 			F(j, 0, n) {
 				tmp += dp[ar[j]][i];
 			}

 			tmp += i;

 			if(tmp < cst) {
 				cst = tmp;
 			}

 		}

 		printf("Case #%d: %d\n", cs, cst);
 		

 	}



	return 0;
}

