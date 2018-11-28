#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <limits>
#include <cstring>

using namespace std;

vector<double> Naomi,Ken;
int main()
{
	int T,N;
	scanf("%d",&T);
	for(int t = 1;t<=T;t++)
	{	
		scanf("%d",&N);
		Naomi.resize(N);
		Ken.resize(N);
		for(int i = 0;i<N;i++)
			scanf("%lf",&Naomi[i]);
		for(int i =0;i<N;i++)
			scanf("%lf",&Ken[i]);
		
		sort(Naomi.begin(),Naomi.end());
		sort(Ken.begin(),Ken.end());
		// for(int i= 0;i<N;i++)
		// 	printf("N = %lf ",Naomi[i] );
		// printf("\n");
		// for(int i= 0;i<N;i++)
		// 	printf("K = %lf ",Ken[i] );
		int dwScore = 0,wScore = 0;
		// for(int i=0;i<N;i++)
		// {
		// 	if(Naomi[i] > Ken[N-1-i])
		// 		dwScore++;
		// 	if(Naomi[i] > Ken[i])
		// 		wScore++;
		// }

		int i =0,j=0;
		while(i<N && j<N)
		{
			if(Naomi[i] < Ken[j])
			{
				wScore++;
				i++;
				j++;
			}
			else
			{
				while(j<N && Naomi[i]>Ken[j])
					j++;
			}
		}
		wScore = N-wScore;
		// for(int k = 0;k<N;k++)
		// {
		// 	if(Naomi[k] > Ken[N-1-k])
		// 		dwScore++;
		// }
		int st = 0,end =N-1;
		i = 0;
		while(i < N && st<=end)
		{
			if(Naomi[i] > Ken[st])
			{
				st++;
				dwScore++;

			}
			else
				end--;
			i++;
		}
		printf("Case #%d: %d %d\n",t,dwScore,wScore );

	}	
	return 0;
}