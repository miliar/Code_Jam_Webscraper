#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

#define inf (9999999999999999LL)
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define eps 1e-8
 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back	
#define mod 1000000007
#define maxn 10100

using namespace std;

int v[maxn];

main(){

		int te;
		scanf("%d",&te);
		for(int t=1;t<=te;t++){

			int n;
			scanf("%d",&n);

			int a1=0, a2=0, m = 0;

			scanf("%d",v);
			for(int i=1;i<n;i++){
				scanf("%d",v+i);
				a1 += max(0,v[i-1]-v[i]);
				m = max(m,v[i-1]-v[i]);
			}

			for(int i=0;i<n-1;i++)
				a2 += min(m,v[i]);

			printf("Case #%d: %d %d\n",t,a1,a2);

		}

}
				
