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

main(){

		int te;
		scanf("%d",&te);
		for(int t=1;t<=te;t++){

			int x,r,c;
			cin >> x >> r >> c;

			printf("Case #%d: ",t);

			if(x >= 8){
				printf("RICHARD\n");
				continue;
			}

			if(x >= 2*r+1){
				printf("RICHARD\n");
				continue;
			}

			if(x >= 2*c+1){
				printf("RICHARD\n");
				continue;
			}

			if(x == 1){
				printf("GABRIEL\n");
				continue;
			}

			if(x >= r+c-1 && r >= 2 && c >= 2){
				printf("RICHARD\n");
				continue;
			}

			if((r*c)%x){
				printf("RICHARD\n");
				continue;
			}

			if(c > r) swap(c,r);

			int ok = 0;

			for(int i=0;i<=x-r;i++){
				int foi = 0;
				int outro = x - r - i;
				for(int j=i;j+outro<c;j++){
					int u = (j) * r - i;
					int t = r*c - u - x;
					if(u%x == 0 && t%x == 0) foi = 1;
				}
				if(foi == 0) ok = 1, debug("! %d\n",i);
			}

			if(x-c+1 > c) swap(c,r);			

			for(int i=0;i<=x-r;i++){
				int foi = 0;
				int outro = x - r - i;
				for(int j=i;j+outro<c;j++){
					int u = (j) * r - i;
					int t = r*c - u - x;
					if(u%x == 0 && t%x == 0) foi = 1;
				}
				if(foi == 0) ok = 1, debug("!! %d\n",i);
			}
			

			if(ok){
				printf("RICHARD\n");
				continue;
			}
			printf("GABRIEL\n");

		}

}
