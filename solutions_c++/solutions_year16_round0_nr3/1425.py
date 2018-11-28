//Pham Huu Canh
//
//Algorithm:
//Complexity:
//AC:

#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

#define max64 9223372036854775807LL
#define max32 2147483647
#define maxty 1001001001
#define max16 32767
#define EPS 1e-8
#define ll long long
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define PQ priority_queue
#define LB lower_bound
#define UB upper_bound
#define fi first
#define se second
#define timmax(x, y)    ((x) > (y) ? (x) : (y))
#define timmin(x, y)    ((x) < (y) ? (x) : (y))
#define fori(i, n)      for((i) = 0; (i) < (n); (i)++)
#define ford(i, n)      for((i) = (n-1); (i) >= 0; (i)--)
#define fore(i, v)      for(typeof(v.begin()) i = v.begin(); i != v.end(); i++)
#define repi(i, a, b)   for((i) = (a); (i) <= (b); (i)++)
#define repd(i, a, b)   for((i) = (a); (i) >= (b); (i)--)
#define all(tmpv)      tmpv.begin(), tmpv.end()

#define fii "c_large.inp"
#define foo "c_large.out"
#define MOD 1000000007
#define inf 1000111000111000111LL

using namespace std;

typedef pair<int, int> II;
typedef vector<int> VI;

char s[105];
int p[15][105];
int g[15] = {1, 1, 3, 2, 5, 2, 7, 2, 9, 2, 11};
int need;

void dfs(int idx, int n, int val[]){
	if (need == 0)	return;
	if (idx > n){
		repi(idx, 2, 10)	if (val[idx] % g[idx])	return;
		printf("%s", s);
		repi(idx, 2, 10)	printf(" %d", g[idx]);
		printf("\n");
		need--;
		return;
	}
	
	int temp[15], i;
	repi(i, 2, 10)	temp[i] = (val[i] + p[i][idx]) % g[i];
	s[idx] = '1';
	if (need)	dfs(idx+1, n, temp);
	s[idx] = '0';
	if (need)	dfs(idx+1, n, val);
}

void input(){
	int itest, ntest;
	int n, i, j;
	int val[15];
	
	scanf("%d", &ntest);
	repi(itest, 1, ntest){
		printf("Case #%d:\n", itest);
		scanf("%d %d", &n, &need);
		
		s[0] = '1';
		s[n-1] = '1';
		s[n] = 0;
		
		repi(i, 2, 10){
			p[i][0] = 1;
			repi(j, 1, n)	p[i][j] = (p[i][j-1] * i) % g[i];
		}
		
		repi(i, 2, 10)	val[i] = (p[i][0] + p[i][n-1]) % g[i];
		dfs(1, n-2, val);
	}
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen(fii,"r",stdin);
        freopen(foo,"w",stdout);
    #endif

    input();

    return 0;
}

