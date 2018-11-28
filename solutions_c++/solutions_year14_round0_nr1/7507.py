//IN THE NAME OF GOD
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <fstream>
#include <utility>
#include <sstream>
#include <list>
#include <iomanip>
#include <functional>
#include <deque>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <complex>
#include <climits>
#include <cctype>
#include <cassert>
#include <bitset>
#include <limits>
#include <numeric>

//#pragma comment(linker, "/STACK:1024000000,1024000000")

using namespace std;

#define timestamp(x) printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
#define INF 100000000
#define pii pair < int , int >
#define MP make_pair
#define MOD 1000000007
#define EPS 1e-9
#define LL long long
#define MAXN 200000+10
#define bug cout<<"!!!!!!!!!!!!!!!!!";

int memo[30][30][500];
int n, k;

int REC(int p, int alpha, int sum){
	if (p == n || sum > k ){
		if (sum == k) return memo[p][alpha][sum] = 1;
		return memo[p][alpha][sum] = 0 ;
	}
	if (~memo[p][alpha][sum]) return memo[p][alpha][sum];
	int res = 0;
	for (int i = alpha + 1 ; i <= 26 ; i++){
		res += REC(p + 1, i , sum + i );
	}
	return memo[p][alpha][sum] = res;
}

int main()
{
	ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("i.txt", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t, tc = 1 , frow , srow , tmp ;
	vector < int > state1, state2 , res ;
	scanf("%d", &t);
	while (t--){
		state1.clear(), state2.clear() , res.clear() ;
		scanf("%d", &frow);
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				scanf("%d", &tmp);
				if (i + 1 == frow) state1.push_back(tmp);
			}
		}
		scanf("%d", &srow);
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				scanf("%d", &tmp);
				if (i + 1 == srow) state2.push_back(tmp);
			}
		}
		for (int i = 0; i < state1.size(); i++){
			for (int j = 0; j < state2.size(); j++){
				if (state1[i] == state2[j]){
					res.push_back(state1[i]);
				}
			}
		}
		if ((int)res.size() == 1) printf("Case #%d: %d\n", tc , res[0]);
		else if ((int)res.size() > 1) printf("Case #%d: Bad magician!\n", tc );
		else if ((int)res.size() < 1) printf("Case #%d: Volunteer cheated!\n", tc);
		tc++;
	}
	return 0;
}