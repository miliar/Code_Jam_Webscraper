#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <map>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <climits>
#include <set>
using namespace std;

int cakes[1009];
priority_queue<int> bfTimes;
int aa[7][7][7][7][7][7][7][7][7];
int bfSol(int bef,int cake[10])
{
	// if(bef+ *max_element(cake.begin(), cake.end())==5)
	// {
	// 	for (int i = 0; i < cake.size(); ++i)
	// 	{
	// 		printf("%d ",cake[i] );
	// 	}
	// 	printf("\nheree=>%d\n", bef);
	// }
	// printf("heree\n");
	if(aa[cake[1]][cake[2]][cake[3]][cake[4]][cake[5]][cake[6]][cake[7]][cake[8]][cake[9]]!=0)
		return aa[cake[1]][cake[2]][cake[3]][cake[4]][cake[5]][cake[6]][cake[7]][cake[8]][cake[9]];
	int mx=0;
	// for(int i= 0; i<10;i++)
	// 	printf("%d \n",cake[i] );
	// printf("heree\n");
	for(int i = 9;i>0;i--)
		if(cake[i]!=0)
		{
			mx=i;
			break;
		}
		// printf("%d\n", mx);
	// bfTimes.push(-(bef+ mx));
	// return;
	aa[cake[1]][cake[2]][cake[3]][cake[4]][cake[5]][cake[6]][cake[7]][cake[8]][cake[9]]=(bef+ mx);
	if(mx<=3)
		return (bef+ mx);
	for(int i=9;i>0;i--)
	{
		if(cake[i]!=0)
		{
			for(int j=1;j<=i/2;j++)
			{
				int cake2[10];
				for(int k=0;k<10;k++)
					cake2[k]=cake[k];
				// 
				cake2[i-j]+=cake2[i];
				cake2[j]+=cake2[i];
				cake2[i]=0;
				cake2[i-j]=min(6,cake2[i-j]);
				cake2[j]=min(6,cake2[j]);
				aa[cake[1]][cake[2]][cake[3]][cake[4]][cake[5]][cake[6]][cake[7]][cake[8]][cake[9]] = min(bfSol(bef+cake[i],cake2),
					aa[cake[1]][cake[2]][cake[3]][cake[4]][cake[5]][cake[6]][cake[7]][cake[8]][cake[9]]);
			}
		}
	}
	// printf("heree2\n");
	return aa[cake[1]][cake[2]][cake[3]][cake[4]][cake[5]][cake[6]][cake[7]][cake[8]][cake[9]];
	// for(int i = 0;i<cake.size();i++)
	// {
	// 	for (int j = 1; j < cake[i]/2; ++j)
	// 	{
	// 		vector<int> cake2(cake);
	// 		cake2[i]-=j;
	// 		cake2.push_back(j);
	// 		bfSol(bef+1,cake2);
	// 	}
	// }

}
int main()
{
	int t;cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		while(!bfTimes.empty())
			bfTimes.pop();
		memset(aa,0,sizeof(aa));
		memset(cakes,0,sizeof(cakes));
		priority_queue<int> times;
		int d;cin>>d;
		int cake[10];
		memset(cake,0,sizeof(cake));
		for(int i=0;i<d;i++)
		{
			int foo;scanf("%d",&foo);
			cakes[foo]++;
			cake[foo]++;
		}

		bfSol(0,cake);
		// int alreadyDone=0;
		// for(int i=1000;i>0;i--)
		// {
		// 	if(cakes[i]!=0)
		// 	{
		// 		// printf("i=%d ==> %d\n",i, i+alreadyDone);
		// 		times.push(-(i+alreadyDone));
		// 		if(i%2)
		// 		{
		// 			alreadyDone++;
		// 			for(int j=1;j<i;j++)
		// 				cakes[j]=cakes[j+1];
		// 		}
		// 		else
		// 		{ 
		// 			cakes[i/2]+=2*cakes[i];
		// 			alreadyDone+=cakes[i];
		// 		}
		// 	}
		// }
		// printf("Case #%d: %d\n",tc,-times.top() );
		printf("Case #%d: %d\n",tc,aa[cake[1]][cake[2]][cake[3]][cake[4]][cake[5]][cake[6]][cake[7]][cake[8]][cake[9]] );
	}
	return 0;
}