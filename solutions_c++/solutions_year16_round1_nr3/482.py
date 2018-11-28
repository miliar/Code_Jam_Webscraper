#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <string>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>

#define inf 1000000007
#define pii pair<int,int>
#define pip pair<int,pii>
#define pll pair<long long,long long>
#define pif pair<int,double>
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back
#define maxn 50500

typedef long long ll;
using namespace std;

int f[maxn];
int last[maxn];
int cyc[maxn];
int fim[maxn];

main(){

	int T, cur = 0;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){

		int n;
		scanf("%d",&n);

		for(int i=0;i<n;i++){
			scanf("%d",f+i), f[i]--;
		}

		int ans = 0;
		int c2 = 0;

		for(int i=0;i<n;i++){
			cur++;
			int len = 0, at = i;
			while(last[at] != cur){
				last[at] = cur;
				at = f[at];
				len++;
			}
			cyc[i] = len;
			fim[i] = at;
			if(at != i)
				continue;
			ans = max(ans,len);
			if(len == 2)
				c2++;
		}

		for(int i=0;i<n;i++)
			if(cyc[i] == 2){
				assert(fim[i] == i);
				assert(cyc[f[i]] == 2);
				assert(fim[f[i]] == f[i]);
				int u = 0;
				for(int j=0;j<n;j++){
					if(fim[j] == i && cyc[j] > u)
						u = cyc[j];

				}
				c2 += u-2;
			}

		for(int i=0;i<n;i++)
			assert(cyc[i] > 1);

		printf("Case #%d: %d\n",t,max(c2,ans));

	}

}
