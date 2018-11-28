#include <cstdio>  
#include <cstring>  
#include<stdio.h>
#include<iostream>
#include<queue>
#include<stack>
#include <algorithm>  
using namespace std ;  
int arr[100000];
int main()
{
int testcase;
int n,xes;
int i,j;
freopen("abc.txt","r",stdin);
freopen("out.txt","w",stdout);
	scanf("%d",&testcase);
	for(xes=0;xes<testcase;xes++)
	{
		cin>>n;
		
		for(j=0;j<n;j++)
		 {
		   cin>>arr[j];
	    }
		int bitval=arr[0];
		j=1;
		while(j<n)
		{
			if(arr[j]>bitval)
			bitval=arr[j];
			j++;
		}
		int mval1=bitval,summation;
		for(i=1;i<bitval+1;i++)
		{
			summation=i;
			for(j=0;j<n;j++)
			{
				if(arr[j]>i)
				{
					   if(arr[j]%i==0)
						summation+=((arr[j]/i)-1);
					else 
						summation+=arr[j]/i;
				}
 
			}
			mval1=min(mval1,summation);	
		}
		int r=mval1;
		printf("Case #%d: %d\n",xes+1,r);
	}
	//system("PAUSE");
	return 0;
}
