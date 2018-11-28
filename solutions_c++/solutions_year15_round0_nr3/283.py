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

char str[maxn];
int v[maxn];

int M[5][5] = {
	0,0,0,0,0,
	0,1,2,3,4,
	0,2,-1,4,-3,
	0,3,-4,-1,2,
	0,4,3,-2,-1,
};

int mt(int a,int b){
	int sig = 1;
	if(a < 0)a = -a, sig *= -1;
	if(b < 0)b = -b, sig *= -1;
	int ret = M[a][b];
	return ret*sig;
}

main(){

		int te;
		scanf("%d",&te);
		for(int t=1;t<=te;t++){

			int len;
			long long k;
			cin >> len >> k;
			scanf(" %s",str);

			for(int i=0;i<len;i++){
				if(str[i] == 'i') v[i] = 2;
				if(str[i] == 'j') v[i] = 3;
				if(str[i] == 'k') v[i] = 4;
			}

			int val = 1;

			for(int i=0;i<len;i++)
				val = mt(val,v[i]);

			int u = 1;
			for(int i=0;i<k%4;i++)
				u = mt(u,val);

			printf("Case #%d: ",t);

			if(u != -1){
				printf("NO\n");
				continue;
			}

			int cur = 0;
			u = 1;
			
			for(int i=0;i<min(20LL,k);i++)
				for(int j=0;j<len;j++){

					u = mt(u,v[j]);
					if(cur == 0 && u == 2){
						u = 1;
						cur = 1;
					}
					else if(cur == 1 && u == 3){
						u = 1;
						cur = 2;
					}

				}

			if(cur == 2)
				printf("YES\n");
			else
				printf("NO\n");

		}

}
