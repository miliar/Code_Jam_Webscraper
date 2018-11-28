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

			int b,n;
			scanf("%d%d",&b,&n);
			
			for(int i=0;i<b;i++)
				scanf("%d",v+i);

			long long low = 0, up = 100000000000000000LL;

			while(low != up){

				long long mid = (low+up)/2;

				long long u = b;

				for(int i=0;i<b;i++)
					u += mid/v[i];

				if(u >= n)
					up = mid;
				else
					low = mid+1;

			}

			debug("low = %lld\n",low);
			long long a = 0;
			for(int i=0;i<b;i++){
				a += low/v[i];
				if(low%v[i])a++;
			}
			debug("a %lld\n",a);

			int ans = 0;

			for(int i=0;i<b;i++) if(low%v[i] == 0){
				a++;
				if(a == n) ans = i+1;
			}

			printf("Case #%d: %d\n",t,ans);

		}

}
			
					
