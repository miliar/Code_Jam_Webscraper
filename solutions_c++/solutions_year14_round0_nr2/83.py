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

main(){

		int te;
		scanf("%d",&te);

		for(int t=1;t<=te;t++){

				double c,f,x;
				scanf("%lf%lf%lf",&c,&f,&x);

				double ans = 9999999999.0f;
				double tt = 0;
				double v = 2;
				
				for(int i=0;i<=x;i++){

					ans = min(ans, tt + x/v);

					tt += c/v;
					v += f;

					}

				printf("Case #%d: %.8lf\n",t,ans);

			}

	}
