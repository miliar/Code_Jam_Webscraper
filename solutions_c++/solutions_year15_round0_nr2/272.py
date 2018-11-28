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

int v[1010];

main(){

		int te;
		scanf("%d",&te);
		for(int t=1;t<=te;t++){

			int n;
			scanf("%d",&n);

			int qm = 0;

			for(int i=0;i<n;i++){
				scanf("%d",v+i);
				qm = max(qm,v[i]);
			}

			int ans = qm;

			for(int i=0;i<=qm;i++){

				int low = 1, up = 1000;
				while(low != up){
					int mid = (low+up)/2;
					int y = 0;
					for(int j=0;j<n;j++){
						y += v[j]/mid;
						if(v[j]%mid) y++;
					}
					if(y <= n+i)
						up = mid;
					else
						low = mid+1;
				}

				ans = min(ans,i+low);

			}

			printf("Case #%d: %d\n",t,ans);

		}

}
				
