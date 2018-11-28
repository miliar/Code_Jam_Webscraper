#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int T,N,war,decwar,k;
	double a[1001], b[1001], arr1[1001], arr2[1001];
	cin>>T;
	for(int i=0;i<T;i++)
	{
		war=0; 
        decwar=0;
		cin>>N;
		for(int j=0;j<N;j++)
		{
			cin>>a[j];
			arr1[j]=a[j];
		}
		for(int j=0;j<N;j++)
		{
			cin>>b[j];
			arr2[j]=b[j];
		}
		//War
		sort(a,a+N);
		sort(b,b+N);
		k=0;
		while(k<N)
		{
			int flag=0;
			for(int j=0;j<N;j++)
			{
				if(b[j]>a[k])
				{
					a[k]=b[j]=0;
					k++;
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				for(int j=0;j<N;j++)
				{
					if(a[j]!=0)
						war++;
				}
				break;
			}
		}
		//Deceitful war
		sort(arr1,arr1+N);
		sort(arr2,arr2+N);
		decwar=N;
		int j=0,k=0;
		while(j<N&&k<N)
		{
			if(arr1[j]<arr2[k])
			{
				decwar--;
				j++;
			}
			else if(arr1[j]>arr2[k])
			{
				j++;
				k++;
			}
		}
		printf("Case #%d: %d %d\n",i+1,decwar,war);
	}
	return 0;
}
