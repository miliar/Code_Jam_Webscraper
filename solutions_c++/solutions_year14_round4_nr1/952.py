#include <iostream>
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
 
#define INF (1<<30)
#define pii pair<int,int>
#define pll pair<long long,long long>
#define eps 1e-9
 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

using namespace std;

int v[10100];
int mrk[10100];

main(){

		int t;
		scanf("%d",&t);

		for(int te=1;te<=t;te++){

			printf("Case #%d: ",te);

			memset(mrk,0,sizeof(mrk));

			int n,k;
			scanf("%d%d",&n,&k);

			for(int i=0;i<n;i++)
				scanf("%d",v+i);

			sort(v,v+n);
			int ans = 0;

			for(int i=n-1;i>=0;i--){

				if(mrk[i])
					continue;
					
				int t = -1;

				for(int j=0;j<i;j++)
					if(!mrk[j] && v[j] + v[i] <= k)
						t = j;

				if(t+1)
					mrk[t] = 1;

				ans++;

			}

			printf("%d\n",ans);
			

		}

}
