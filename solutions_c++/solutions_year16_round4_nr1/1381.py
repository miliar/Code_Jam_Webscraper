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

string calc(int x, int n, int &r, int &p, int &s){
	if (n == 0){
		r = (x == 0);
		p = (x == 1);
		s = (x == 2);
		if (x == 0) return "R";
		else if (x == 1) return "P";
		else return "S";
	}
	int a, b, c;
	string s1 = calc(x, n - 1, r, p, s);
	string s2 = calc((x + 2) % 3, n - 1, a, b, c);
	r += a;
	p += b;
	s += c;
	if (s1 < s2) return s1 + s2;
	else return s2 + s1;
}

int m, n, r, p, s;
int main(){

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int casenum;
	string ans;
	scanf("%d", &casenum);
	for (int z = 1; z <= casenum; z++){
		scanf("%d%d%d%d", &n, &r, &p, &s);
		bool flag = false;
		for (int i = 0; i < 3; i++){
			int rr, pp, ss;
			ans = calc(i, n, rr, pp, ss);
			if ((rr == r) && (pp == p) && (ss == s)){
				flag = true;
				break;
			}
		}
		printf("Case #%d: ", z);
		if (flag){
			printf("%s", ans.c_str());
		}
		else{
			printf("IMPOSSIBLE");
		}
		printf("\n");
	}

 	fclose(stdin);
 	fclose(stdout);
	
}