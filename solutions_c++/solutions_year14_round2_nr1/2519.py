#include<stdio.h>
#include<iostream>
#include<iomanip>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<limits.h>
using namespace std;

int main()
{
	int t,n;
	scanf("%d",&t);
	int T=t;
	while(t--)
	{
		scanf("%d",&n);
		int flag=0;
		char **arr;
		arr=(char**)malloc(sizeof(char*)*n);
		for(int i=0;i<n;i++)
		{
			arr[i]=(char*)malloc(sizeof(char)*101);
			scanf("%s",arr[i]);
			if(i!=0)
			{
				string str1=arr[i];
				string str2=arr[i-1];
				 if(str1.compare(str2)!=0)
					flag=1;
			}
		}
		/*for(int i=0;i<n;i++)
			printf("%s\n",arr[i]);*/
		char *temp=arr[0];	
		int count=0,tcount=0;
		/*for(int i=1;i<n && flag>0;i++)
		{
			if(strlen(arr[i])<strlen(temp))
				temp=arr[i];
		}*/
		
		
			int j,k=0;
			for(j=0,k=0;j<(int)strlen(arr[0])&&k<(int)strlen(arr[1]);)
			{
				if(arr[0][j]==arr[1][k])
				{
					k++;
					j++;
					continue;
				}
				else if((j>0 && arr[0][j]==arr[0][j-1])|| (k>0 && arr[1][k]==arr[1][k-1]))
				{
					tcount++;
					if(arr[1][k]==arr[1][k-1])
						k++;
					if(arr[0][j]==arr[0][j-1])
						j++;
				}

				else 
				{
					tcount=-1;
					break;
				}
			}
			//printf("%d\n",tcount);
			
			while(k<(int)strlen(arr[1]))
			{
				if(arr[1][k]==arr[1][k-1])
					tcount++;
				else
				{
					tcount=-1;
					break;
				}
				k++;
			}
			while(j<(int)strlen(arr[0]))
			{
				if(arr[0][j]==arr[0][j-1])
					tcount++;
				else
				{
					tcount=-1;
					break;
				}
				j++;
			}
			if(tcount>count)
				count=tcount;
			tcount=0;
		
		if(flag==1 && count==0)
			printf("Case #%d: Fegla Won\n",T-t);
		else
			printf("Case #%d: %d\n",T-t,count);
	}
	return 0;
}
