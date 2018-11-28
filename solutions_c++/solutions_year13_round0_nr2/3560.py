#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#define INF 1000000000
#define INFll 1000000000000000000ll
#define LD long double
#define LL long long
#define Vi vector<int>
#define VI Vi::iterator
#define Si set<int>
#define SI Si::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Li list<int>
#define LI Li::iterator
#define pb push_back
#define mp make_pair
using namespace std;

int n, m, a[111][111], p[111], q[111];

string solve(){
	scanf("%d%d", &n, &m);
	memset(p, 0, sizeof(p));
	memset(q, 0, sizeof(q));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++){
			scanf("%d", &a[i][j]);
			p[i] = max(p[i], a[i][j]);
			q[j] = max(q[j], a[i][j]);
		}
	
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (a[i][j] != min(p[i], q[j]))
				return "NO";
	return "YES";
}

int main(){
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
		printf("Case #%d: %s\n", i, solve().c_str());
	return 0;
}






