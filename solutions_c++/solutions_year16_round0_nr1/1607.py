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

#define fii "a_large.inp"
#define foo "a_large.out"
#define MOD 1000000007
#define inf 1000111000111000111LL

using namespace std;

typedef pair<int, int> II;
typedef vector<int> VI;

bool vis[15];
void danhdau(int x){
	do{
		vis[x%10] = true;
		x /= 10;
	}
	while (x != 0);
}

bool ktra(){
	int i;
	fori(i, 10)	if (!vis[i])	return false;
	return true;
}

void input(){
	int itest, ntest, n, i;
	
	scanf("%d", &ntest);
	repi(itest, 1, ntest){
		printf("Case #%d: ", itest);
		scanf("%d", &n);
		if (n == 0)	printf("INSOMNIA\n");
		else{
			fori(i, 10)	vis[i] = false;
			danhdau(n);
			int res = n;
			while (!ktra()){
				res += n;
				danhdau(res);
			}
			printf("%d\n", res);
		}
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

