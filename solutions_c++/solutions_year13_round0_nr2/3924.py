#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <queue>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back

#define epr(...) fprintf(stderr, __VA_ARGS__

const int maxn = 1000;
const int inf = 1e9;

int a[maxn][maxn];
int b[maxn][maxn];


int main(){
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int t, n, m, val;
    bool flag;
    scanf("%d", &t);
    for(int tt = 0; tt < t; tt++){
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; i++)
	    for(int j = 0; j < m; j++)
		scanf("%d", &a[i][j]);
	for(int i = 0; i < n; i++)
	    for(int j = 0; j < m; j++)
		b[i][j] = 100;
	
	for(int i = 0; i < n; i++){
	    val = -1;
	    for(int j = 0; j < m; j++)
		val = max(a[i][j], val);
	    for(int j = 0; j < m; j++)
		b[i][j] = min(b[i][j], val);
	}
	
	for(int j = 0; j < m; j++){
	    val = -1;
	    for(int i = 0; i < n; i++)
		val = max(a[i][j], val);
	    for(int i = 0; i < n; i++)
		b[i][j] = min(b[i][j], val);
	}
	flag = 1;
	for(int i = 0; i < n; i++)
	    for(int j = 0; j < m; j++)
		if (a[i][j] != b[i][j])
		    flag = 0;
	if (flag)
	    printf("Case #%d: YES\n", tt + 1);
	else
	    printf("Case #%d: NO\n", tt + 1);
    }
    
    return 0;
}