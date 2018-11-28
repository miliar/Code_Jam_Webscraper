#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<limits.h>
#include<iostream>
#include<conio.h>

#define MOD 1000000007

/*	string to int

		vector<int>vec;
		stringstream ss(str); // space seperated string
		while(ss)
		{
			int x;
			ss>>x; // string to integer
			vec.push_back(x);
		}
*/

/*
sort(vec.begin(),vec.end(),std::greater<int>()); // sort by decreasing order
*/

using namespace std;

double N[1004];
double K[1004];
double KD[1004];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int n,t;
    scanf("%d",&t);

	for(int test=1;test<=t;test++)
	{
		int war=0,dwar=0;
		scanf("%d",&n);

		for(int i=0;i<n;i++)
		scanf("%lf",&N[i]);
		
        for(int i=0;i<n;i++)
		{
			scanf("%lf",&K[i]);
			KD[i]=K[i];
		}

		sort(K,K+n);
		sort(N,N+n);
		sort(KD,KD+n);
/*
		printf("\n");
        for(int i=0;i<n;i++)
		printf("%.3f ",N[i]);

		printf("\n");
        for(int i=0;i<n;i++)
		printf("%.3f ",K[i]);
*/
		int i=0;
		int j=0;
		
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(K[j]>N[i])
				{
					K[j]=-1;
					break;
				}
			}
			
			if(j==n)
			war++;
		}

		// dwar

		for(i=0;i<n;i++)
		{
			for(j=n-1;j>=0;j--)
			{
				if(N[i]>KD[j]&&KD[j]!=-1)
				break;
			}
		
			if(j==-1) // N[i] is not greater than any
			{
				for(int j=n-1;j>=0;j--)
				if(K[j]!=-1)
				{
					K[j]=-1;
					break;
				}
			}
		
			else
			{
				for(int k=0;k<=j;k++)
				{
					if(KD[k]!=-1)
					{
						j=k;
						break;
					}
				}
				
				KD[j]=-1;
				dwar++;

			}
		}
		
		printf("Case #%d: %d %d\n",test,dwar,war);

	}

    return 0;
}
