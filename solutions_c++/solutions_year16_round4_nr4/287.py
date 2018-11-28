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
#define pfi pair<double,int>
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

#define pb push_back
#define maxn 210
#define max3(a,b,c) max(max(a,b),c)
#define mod 754754

#define put PutInt
#define send Send
#define get GetInt
#define receive Receive

typedef long long ll;
using namespace std;

char M[5][5];

int at[5][5];

int pi[5];

int mrk[5];

int bt(int pos,int n){

	if(pos == n)
		return 1;
	int foi = 0;
	int ret = 1;
	for(int i=0;i<n;i++)
		if(!mrk[i] && at[pi[pos]][i]){
			foi = 1;
			mrk[i] = 1;
			ret &= bt(pos+1,n);
			mrk[i] = 0;
		}
	if(foi == 0)
		return 0;
	return ret;
}

main(){

	int nt;
	scanf("%d",&nt);

	for(int t=1;t<=nt;t++){

		int n;
		scanf("%d",&n);

		for(int i=0;i<n;i++)
			scanf(" %s",M[i]);

		int ans = n*n;

		for(int i=0;i<(1<<(n*n));i++){

			int cand = 0;
			int cur = 0;
			for(int x=0;x<n;x++)
				for(int y=0;y<n;y++){
					if(M[x][y] == '1')
						at[x][y] = 1;
					else
						at[x][y] = 0;
					if(i & (1<<cur)){
						cand++;
						at[x][y] = 1;
					}
					cur++;
				}

			int ok = 1;
			for(int j=0;j<n;j++)
				pi[j] = j;
			do {
				memset(mrk,0,sizeof(mrk));
				if(bt(0,n) == 0) ok = 0;
			
			} while(next_permutation(pi,pi+n));
			if(ok){
				ans = min(ans,cand);
				//if(cand == 2){
					//debug("%d\n",i);
				//}
			}
		}

		printf("Case #%d: %d\n",t,ans);

	}

}
