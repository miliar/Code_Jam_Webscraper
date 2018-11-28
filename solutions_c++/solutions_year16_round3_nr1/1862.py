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
# define EPS 1e-10

//# define INT_MAX 2147483647   
//# define INT_MIN (-2147483647 - 1)    
# define LL_MAX  9223372036854775807i64        
# define LL_MIN  (-9223372036854775807i64 - 1)
# define PI 3.14159265358979323846

using namespace std;
typedef long long                  ll;
typedef pair<long long, long long> pll;
typedef pair<int, int>             pii;
typedef pair<double, int>          pdi;
typedef pair<double, double>       pdd;
typedef pair<string, string>       pss;
typedef unsigned long long         ull;

int T, N, P[33];

set<pii> st;
vector<char> ans;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	//Work_It_Harder_Make_It_Better_Do_It_Faster_Makes_Us_Stronger;

	scanf("%d", &T);
	rep(_t, 0, T){
		scanf("%d", &N);
		st.clear();
		ans.clear();
		rep(i, 0, N){
			scanf("%d", P + i);
			st.insert({ -P[i], i });
		}
		while (!st.empty()){
			if ((*st.begin()).first == 0) break;
			if (st.size() == 3){
				if (st.begin()->first == -1 && (++st.begin())->first == -1 && (++(++st.begin()))->first == -1){
					ans.push_back('A' + st.begin()->second);
					ans.push_back(' ');
					st.erase(st.begin());
					continue;
				}
			}
			if (st.size() == 2){
				if (st.begin()->first == -2 && (++st.begin())->first == -1){
					pii s = *(++st.begin());
					ans.push_back('A' + st.begin()->second);
					ans.push_back(' ');
					ans.push_back('A' + st.begin()->second);
					ans.push_back('A' + s.second);
					ans.push_back(' ');
					st.clear();
					continue;
				}
			}
			if (st.size() == 1){
				auto b = st.begin();
				pii f = *b;
				if ((-f.first) >= 2){
					st.erase(st.begin());
					if (f.first + 2 != 0) st.insert({ f.first + 2, f.second });
					ans.push_back('A' + f.second);
					ans.push_back('A' + f.second);
					ans.push_back(' ');
				}
				else{
					st.erase(st.begin());
					if (f.first + 1 != 0)st.insert({ f.first + 1, f.second });
					ans.push_back('A' + f.second);
					ans.push_back(' ');
				}
			}
			else{
				auto b = st.begin();
				pii f = *b;
				pii s = *(++b);
				if (-f.first - (-s.first) >= 2 && (-f.first) >= 2){
					st.erase(st.begin());
					if(f.first + 2 != 0) st.insert({ f.first + 2, f.second });
					ans.push_back('A' + f.second);
					ans.push_back('A' + f.second);
					ans.push_back(' ');
				}
				else{
					st.erase(st.begin());
					st.erase(st.begin());
					if (f.first + 1 != 0)st.insert({ f.first + 1, f.second });
					if (s.first + 1 != 0)st.insert({ s.first + 1, s.second });
					ans.push_back('A' + f.second);
					ans.push_back('A' + s.second);
					ans.push_back(' ');
				}
			}
		}
		printf("Case #%d: ", _t + 1);
		rep(i, 0, ans.size()){
			printf("%c", ans[i]);
		}
		printf("\n");
	}
	

	//WaitMyDear WaitMyDear
	return 0;
}