#include <cstdio>
#include <sstream>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <iterator>
#include <climits>

#define READ(x)		freopen(x,"r",stdin)
#define WRITE(x)	freopen(x,"w",stdout)

#define REP(i, n)	for(int i=0;i<n;i++)
#define REPN(i,n)	for(int i=1;i<=n;i++)
#define SET(i,n)	memset(i,n,sizeof(i))

#define MAX			100050
#define INF			1e9
#define EPS			1e-9
#define MOD			1000000007

#define pb			push_back
#define cl			clear

using namespace std;

typedef long long 		ll;
typedef unsigned long long	ull;
typedef double			db;

char str[MAX];

int main() {
    READ("B-large.in");
    WRITE("B-large.out");
	int tc, cas=1;
	scanf("%d", &tc);
	while(tc--){
        scanf("%s", str);
        int n = strlen(str), ret = 0;
        REP(i, n-1) if(str[i] != str[i+1]) ret++;
        if(str[n-1] == '-') ret++;
        printf("Case #%d: %d\n", cas++, ret);
	}
	return 0;
}
