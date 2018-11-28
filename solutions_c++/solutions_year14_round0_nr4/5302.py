#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;



int minBlacklist(bool* b,int len)
{
	for(int i=0;i<=len-1;i++ )
	{
		if(b[i])return i;
	}	

	return -1;	
}



int maxBlacklist(bool* b,int len)
{
	for(int i=len-1;i>=0;i-- )
	{
		if(b[i])return i;
	}	

	return -1;	
}








int main()
{
	int t;
	cin>>t;

	for(int i=1;i<=t;i++)
	{

		int n;
		cin>>n;

		double N[n],K[n];

		bool A[n],B[n];

		
		for(int j=0;j<n;j++)
		{
			cin>>N[j];
		}
		
		for(int j=0;j<n;j++)
		{
			cin>>K[j];
		}
		
		for(int j=0;j<n;j++)
		{
			A[j]=true;
			B[j]=true;
		}	

		int war_naomi = 0;

		for(int j=0;j<n;j++)
		{
			bool c = true;
			int min_index =0;
		
				double min = 10;
		
			for(int k=0;k<n;k++)
			{
				
				if(K[k]>N[j] && B[k] && K[k]<min)
				{

					c = false;
					min  = K[k];
					min_index = k;
				}

		
			}	
			if(!c)
			{
				B[min_index]=false;	
			}
			A[j] = false;
	
			if(c)
			{
				war_naomi+=1;
			}
		}	






		sort(K,K+n);
		sort(N,N+n);

		for(int j=0;j<n;j++)
		{
			A[j]=true;
			B[j]=true;
		}	

		int deceit_naomi = 0;
		
		int j=0;
		for(;j<n;j++)
		{
			if(K[minBlacklist(B,n)]<N[j])
			{
				deceit_naomi+=1;
				B[minBlacklist(B,n)]=false;
			}

			else
			{
				B[maxBlacklist(B,n)]=false;
			}

		}	

		deceit_naomi+= n-j;


		printf("Case #%d: %d %d\n",i,deceit_naomi,war_naomi);

	}	

}