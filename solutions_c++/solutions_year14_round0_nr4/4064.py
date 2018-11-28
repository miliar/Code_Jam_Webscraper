
#include <iostream>
#include <stdio.h>
#include <cstring>
#include <algorithm>
#include <cstdlib>

#define LEN 1024
using namespace std;
double naomi[LEN],ken[LEN];
int main()
{
   	freopen("3L.in","r",stdin);
    freopen("3Lres.txt","w",stdout);
	int T;
	scanf("%d",&T);
	cerr<<T<<endl;
	for(int c = 1;c<=T;c++)
	{
		int N; 
		scanf("%d",&N);
		// cerr <<N<<endl;
		// printf("n: %d\n",n);
		for(int i = 0 ;i < N;i++)
		{
			scanf("%lf", &naomi[i]);
		}
		for(int i = 0 ;i < N;i++)
		{
			scanf("%lf",&ken[i]);
		}
		sort(naomi, naomi+N);
		sort(ken, ken+N);

		int nWin = 0;
		int inde = N - 1;
		// cerr<<"Ken: ";
		for(int i =N-1; i>=0;i--)
		{
			if(inde <0)
				break; 
			if(naomi[inde] > ken[i])
			{
				nWin++;
				inde--;
			}
			// cerr<<ken[i]<<" ";
			// printf("%d ",ken[i]);
		}
		// cerr<<endl;
		// puts("");
		inde = N - 1;
		int kWin = 0;

		// cerr<<"Naomi: ";
		for(int i =N-1; i>=0;i--)
		{
			if(inde <0)
				break; 
			if(ken[inde] > naomi[i])
			{
				kWin++;
				inde--;
			}
			// cerr<<naomi[i]<<" ";
		}
		// cerr<<endl;
		printf("Case #%d: %d %d\n",c, nWin, N - kWin);
	}

	return 0;
}