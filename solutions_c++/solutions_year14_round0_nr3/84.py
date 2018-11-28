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

char ans[55][55];

int dp[55][55][330];

int get(int l,int qm,int f){

	if(l == 0 && f == 0)
		return 0;

	if(l == 0)
		return -2;

	if(f < 0)
		return -2;

	if(dp[l][qm][f]+1)
		return dp[l][qm][f];

	if(l == 1 && f > qm)
		return -2;
	if(f == 1)
		return -2;

	if(f == 0)
		return 0;

	if(qm <= 1)
		return -2;

	int ret = -2;

	for(int i=2;i<=qm;i++)
		if(get(l-1,i,f-i) != -2)
			ret = i;

	return dp[l][qm][f] = ret;

}

main(){

		int te;
		scanf("%d",&te);

		for(int t=1;t<=te;t++){

			int n,m,k;
			scanf("%d%d%d",&n,&m,&k);
			debug("%d %d %d\n",n,m,k);

			memset(dp,-1,sizeof(dp));

			for(int i=0;i<n;i++)
				for(int j=0;j<m;j++)
					ans[i][j] = '*';

			printf("Case #%d:\n",t,n,m,k);

			int f = n*m-k;
			int F = f;
			int imp = 0;

			if(f >= 2*(m+n) - 4){

				for(int i=0;i<n;i++)
					ans[i][0] = ans[i][1] = '.';
				for(int i=0;i<m;i++)
					ans[0][i] = ans[1][i] = '.';

				f -= 2*(m+n)-4;

				for(int i=2;i<n;i++)
					for(int j=2;j<m && f;j++)
						ans[i][j] = '.', f--;

				ans[0][0] = 'c';
				

			}

			
			else {
					debug("%d %d %d\n",n,m,k);
					for(int k=2;k<=n;k++)
						if(2*k <= f && get(m-2,k,f-2*k) != -2){

							debug("! k=%d\n",k);

							for(int i=0;i<k;i++)
								ans[i][0] = ans[i][1] = '.';

							f -= 2*k;
							debug("f=%d\n",f);
							int x = k;

							for(int j=2;j<m;j++){
								x = get(m-j,x,f);
								debug("x=%d\n",x);
								for(int i=0;i<x;i++)
									ans[i][j] = '.', f--;
			
							}
								

							goto end;
						}


					for(int k=2;k<=m;k++)
						if(2*k <= f && get(n-2,k,f-2*k) != -2){

							debug("@ k=%d\n",k);

							for(int i=0;i<k;i++)
								ans[0][i] = ans[1][i] = '.';

								f -= 2*k;
								int x = k;

								for(int i=2;i<n;i++){
									x = get(n-i,x,f);
									for(int j=0;j<x;j++)
										ans[i][j] = '.', f--;
									}


							goto end;
						}

					
				
					imp = 1;
				
				}

			if(imp == 0 && n*m != 1)
				assert(f == 0);

			end:
			ans[0][0] = 'c';

			f = F;

			if(n == 1){

				imp = 0;
				memset(ans,'*',sizeof(ans));
				for(int i=0;i<f;i++)
					ans[0][i] = '.'; 
				ans[0][0] = 'c';
				

				}

			if(m == 1){

				imp = 0;
				memset(ans,'*',sizeof(ans));
				for(int i=0;i<f;i++)
					ans[i][0] = '.';
				ans[0][0] = 'c';

			}

			if(f == 1){
				imp = 0;
				memset(ans,'*',sizeof(ans));
				ans[0][0] = 'c';
			}

			if(imp){
				printf("Impossible\n");

				for(int i=2;i<f;i++)
					if(f%i == 0)
						debug("f=%d n=%d m=%d\n",f,n,m);

			}
			else
				for(int i=0;i<n;i++){
					for(int j=0;j<m;j++)
						printf("%c",ans[i][j]);
					printf("\n");
				}


		}

}
				
