#include <algorithm>
#include <bitset>
#include <cmath> 
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <utility>
#include <vector>
#define PB push_back
#define MP make_pair
#define LB lower_bound
#define UB upper_bound
#define FT first
#define SD second
#define VI vector<int> 
#define MII map<int,int>
#define SI set<int>
#define rep(i, n) for (int i = 0; i < n; i++)
typedef long long LL;
typedef long double LD;
const int INF = 0x7FFFFFFF;
const LL LINF = 0x7FFFFFFFFFFFFFFFll;

using namespace std;

LL base[100];

int main(){

	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	
	int casenum;
	LL ans[100];
	int ansn;
	LL k, s, c;
	scanf("%d", &casenum);
	for (int z = 1; z <= casenum; z++){
		cin >> k >> c >> s;
		c--;
		if ((c + 1) * s < k){
			printf("Case #%d: IMPOSSIBLE\n", z);
			continue;
		}
		base[0] = 1;
		ansn = 0;
		memset(ans, 0, sizeof ans);
		for (int i = 1; i <= c; i++) base[i] = base[i - 1] * k;
		for (int i = 1; i <= k; i += c + 1){
			for (int j = i; j <= i + c; j++){
				if (j > k) break;
				ans[ansn] += (j - 1) * base[c - j + i];
			}
			ans[ansn] ++;
			ansn++;
		}
		printf("Case #%d:", z);
		for (int i = 0; i < ansn; i++) printf(" %lld", ans[i]);
		printf("\n");
	}

 	fclose(stdin);
 	fclose(stdout);
	
}