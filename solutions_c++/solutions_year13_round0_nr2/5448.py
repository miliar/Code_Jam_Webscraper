#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;



int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("B.out","wt",stdout);
	
	int n;
	scanf("%d",&n);
	
	for(int ii=1 ; ii<=n ; ++ii)
	{
		int N,M;
		scanf("%d",&N);
		scanf("%d",&M);
		
		int Mat[N][M];
		int TMat[N][M];
		for(int n = 0 ; n < N; ++n)
		{
			for(int m = 0 ; m < M ; ++m)
			{ int in;
				scanf("%d",&in);
				Mat[n][m] = in;
				TMat[n][m] = -1;
			//	printf("%d ",Mat[n][m]);
			}
			printf("\n");
		}
		
		for(int n = 0 ; n < N; ++n)
		{
			int max = Mat[n][0];
			for(int p = 1 ; p < M ; p++)
			{	if(max < Mat[n][p])
					max = Mat[n][p];
		    }
			//	printf("min %d\n", min);
			for(int m = 0 ; m < M ; ++m)
			{   		    
				if(max <= Mat[n][m])
					TMat[n][m]= 0; 
			//	printf(" ,%d -- %d , ",Mat[n][0],Mat[n][m])	;
			}
		//	printf("\n");
	    }
		for(int m = 0 ; m < M; ++m)
		{
			int max = Mat[0][m];
			for(int p = 1 ; p < N ; p++)
			{
			 if(max < Mat[p][m])
				max = Mat[p][m];
		    }
		//	printf("min %d\n", min);	
			for(int n = 0 ; n < N; ++n)
			{
				if(max <= Mat[n][m])
					TMat[n][m]= 0;
			//	printf(" ,%d -- %d , ",Mat[0][m],Mat[n][m])	;	
			}	
		//	printf("\n");
	    }
	    
		int flag = 1;	
	    for(int n = 0 ; n < N; ++n)
		{
			for(int m = 0 ; m < M ; ++m)
			{
				if(TMat[n][m] != 0)
				{ 
					flag = 0;
					break;
				}
			//	printf("%d ",TMat[n][m]);
			}
		//	printf("\n");
		}
	    printf("Case #%d: %s\n", ii, flag>0?"YES":"NO");
	    
	}
	return 0;		
}
