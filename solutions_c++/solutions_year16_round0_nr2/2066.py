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

int getans(string s, int len, int x){
	/*cout << s << endl;
	cout << len << endl;
	cout << x << endl;*/
	int delta = 0;
	//char ss[111] = "";
	if (len == 0) return 0;
	if (s[len - 1] == '+'){
		if (x == 0){
			delta = 1;
			x = 1;
		}
	}
	else{
		if (x == 1){
			delta = 1;
			x = 0;
		}
	}
	return getans(s, len - 1, x) + delta;
}

char s[111];

int main(){

	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int casenum, ans;
	scanf("%d", &casenum);
	gets(s);
	for (int z = 1; z <= casenum; z++){
		gets(s);
		ans = getans(s, strlen(s), 1);
		printf("Case #%d: %d\n", z, ans);
	}

 	fclose(stdin);
 	fclose(stdout);
	
}