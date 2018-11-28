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
char str[111];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	//Work_It_Harder_Make_It_Better_Do_It_Faster_Makes_Us_Stronger;

	scanf("%d", &T);
	gets(str);
	rep(t, 0, T){
		gets(str);
		ll ans = 0;
		int l = strlen(str);
		int i = 0;
		bool bad = 0, good = 0;
		while (1){	
			while (i < l && str[i] == '-'){
				if (good){
					ans++;
					good = 0;
				}
				++i;
				bad = 1;
			}
			while (i < l && str[i] == '+'){
				if (bad){
					ans++;
					bad = 0;
				}
				++i;
				good = 1;
			}
			if (i == l){
				if (bad)++ans;
				break;
			}
		}
		printf("Case #%d: %I64d\n", t + 1, ans);
	}
	


	WaitMyDear
	return 0;
}