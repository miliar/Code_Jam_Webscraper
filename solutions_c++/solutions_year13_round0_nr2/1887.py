#include <cstdio>
#include <string>
#include <memory.h>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <iomanip>
 
using namespace std;
 
#define forn(i,n) for (int i = 0; i < int(n); i++)
#define pb push_back
#define mp make_pair

typedef long long li;
 
template <typename T> T sqr(const T &x) {
	return x * x;
}
                                    
const int INF = 1e9;                                      
const long double EPS = 1e-9;
const long double PI = acos(-1.0);
const int N = 20002;

bool check(const vector <vector <int> > &a, int x, int y, int n, int m){
	bool ok1 = true, ok2 = true;
	for(int i = 0; i < n; i++){
		if(a[i][y] > a[x][y]){
			ok1 = false; 
			break;
		}
	}
	for(int j = 0; j < m; j++){
		if(a[x][j] > a[x][y]){
			ok2 = false;
			break;
		}
	}
	return ok1 || ok2;
}
		
int main() {
	//freopen("input.txt", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	forn(c, t){
		int n, m;
		scanf("%d%d", &n, &m);
		vector <vector <int> > a(n, vector <int> (m));
		forn(i, n)
			forn(j, m){
				scanf("%d", &a[i][j]);
			}
		bool ok = true;
		for(int i = 0; i < n; i ++){
			if(!ok)
				break;
			for(int j = 0; j < m; j++){
				if(!check(a, i, j, n, m)){
					ok = false;
					break;
				}	
			}
		}
		if(ok)
			printf("Case #%d: YES\n", c + 1);
		else 
			printf("Case #%d: NO\n", c + 1);
	}	
   	return 0;
}