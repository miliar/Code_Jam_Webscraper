# define _CRT_SECURE_NO_WARNINGS
# include <unordered_map>
# include <functional>
# include <algorithm>
# include <iostream>
# include <iomanip>
# include <fstream>
# include <sstream>
# include <vector>
# include <string>
# include <bitset>
# include <cmath>
# include <queue>
# include <stack>
# include <ctime>
# include <set>
# include <map>
# include <string.h>
# include <limits.h>
# include <stdlib.h>
# include <stdio.h>

# define Work_It_Harder_Make_It_Better_Do_It_Faster_Makes_Us_Stronger 	ios::sync_with_stdio(0); cin.tie(0);
# define  rep(x, a, b) for(int (x) = (a); (x) <  int(b); ++(x))
# define repd(x, a, b) for(int (x) = (a); (x) >= int(b); --(x))
# define WaitMyDear cin.sync(); cin.get();
# define endl "\n"
# define INF 0x3F3F3F3F
# define y1 qwerty 
# define EPS 1e-6

# define LL_MAX  9223372036854775807i64        
# define LL_MIN  (-9223372036854775807i64 - 1)
# define PI 3.14159265358979323846

using namespace std;
typedef long long                  ll;
typedef pair<long long, long long> pll;
typedef pair<int, int>             pii;
typedef pair<double, double>       pdd;
typedef unsigned long long         ull;

int T;
ll n;
bool h[10];

inline bool check(){
	int c = 0;
	rep(i, 0, 10) c += h[i];
	return c == 10;
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	//Work_It_Harder_Make_It_Better_Do_It_Faster_Makes_Us_Stronger;

	scanf("%d", &T);
	rep(t, 0, T){
		memset(h, 0, sizeof h);
		scanf("%I64d", &n);
		if (n == 0){
			printf("Case #%d: INSOMNIA\n", t + 1);
			continue;
		}
		ll up = 1;
		ll last = n;
		int ans = 0;
		while (!check()){
			++ans;
			ll have = up * n;
			last = have;
			++up;
			while (have) {
				h[have % 10] = 1;
				have /= 10;
			}
		}
		printf("Case #%d: %I64d\n", t + 1, last);
	}


	WaitMyDear
	return 0;
}