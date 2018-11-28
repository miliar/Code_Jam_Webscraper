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

int n,m;
char a[111][111];
int minx[111], miny[111], maxx[111], maxy[111];
char useless;
bool flag;

int main(){

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int casenum, hh;
	scanf("%d", &casenum);
	for (int z = 1; z <= casenum; z++){
		scanf("%d%d", &n, &m);
		rep(i, n){
			miny[i] = INF;
			maxy[i] = -1;
		}
		rep(i, m){
			minx[i] = INF;
			maxx[i] = -1;
		}
		rep(i, n){
			scanf("%c", &useless);
			rep(j, m){
				scanf("%c", &a[i][j]);
				if (a[i][j] != '.'){
					minx[j] = min(minx[j], i);
					miny[i] = min(miny[i], j);
					maxx[j] = max(maxx[j], i);
					maxy[i] = max(maxy[i], j);
				}
			}
		}
		hh = 0;
		flag = true;
		rep(i, n){
			//printf("miny: %d maxy: %d\n", miny[i], maxy[i]);
			//printf("minx: %d maxx: %d\n", minx[i], maxx[i]);
			rep(j, m){
				if ((a[i][j] != '.') && (minx[j] == maxx[j]) && (miny[i] == maxy[i])){
					flag = false;
				}
				else{
					if ((a[i][j] == '<') && (miny[i] == j)) hh++;
					if ((a[i][j] == '>') && (maxy[i] == j)) hh++;
					if ((a[i][j] == '^') && (minx[j] == i)) hh++;
					if ((a[i][j] == 'v') && (maxx[j] == i)) hh++;
				}
			}
		}
		if (flag) printf("Case #%d: %d\n", z, hh);
		else printf("Case #%d: IMPOSSIBLE\n", z);
	}

 	fclose(stdin);
 	fclose(stdout);
	
}