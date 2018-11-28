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

int f[1010];

main(){

		int te;
		scanf("%d",&te);
		for(int t=1;t<=te;t++){

			int u;
			cin >> u;

			for(int i=0;i<=u;i++){
				char ch;
				scanf(" %c",&ch), ch -= '0';
				f[i] = ch;
			}

			for(int i=0;i<=1000;i++){

				int v = i;
				int ok = 1;
				for(int j=0;j<=u;j++){
					if(v < j && f[j] != 0) ok = 0;
					if(v >= j) v += f[j];
				}
				if(ok){
					printf("Case #%d: %d\n",t,i);
					break;
				}
			
			}

		}

}
		
				
