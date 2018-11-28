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

double a[1010];
double b[1010];

int foi[1010];

main(){

		int te;
		scanf("%d",&te);

		for(int t=1;t<=te;t++){

			memset(foi,0,sizeof(foi));

			int n;
			scanf("%d",&n);

			for(int i=0;i<n;i++)
				scanf("%lf",a+i);
			for(int i=0;i<n;i++)
				scanf("%lf",b+i);

			sort(a,a+n);
			sort(b,b+n);

			int ans1 = 0;

			for(int i=1;i<=n;i++){

				int ok = 1;

				for(int j=0;j<i;j++)
					if(a[n-i+j] < b[j])
						ok = 0;

				if(ok)
					ans1 = i;

			}

			int ans2 = 0;

			for(int i=0;i<n;i++){

				int last = n-1;
				while(foi[last])
					last--;

				if(a[i] > b[last]){
					ans2++;
					int k = 0;
					while(foi[k])
						k++;
					foi[k] = 1;
					continue;
					}

				while(last != -1 && b[last] > a[i])
					last--;

				last++;

				while(foi[last])
					last++;

				foi[last] = 1;

			}

			printf("Case #%d: %d %d\n",t,ans1,ans2);

		}

	}
				


			
