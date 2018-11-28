#include<stdio.h>
#include<iostream>
#include<cstring>
using namespace std;
int T,smax;
char *s;
int main()
{
		cin>>T;
		int i,j,k=0;
		for(i=0;i<T;i++)
		{
			cin>>smax;
			s=new char[smax+1];
			cin>>s;
			
			
			int total=0,difference=0;	
			for(j=0;j<=smax;j++)
			{
				k=s[j]-'0';
				if(total<=j)
				{
						int n=j-total;
						difference+=n;
						total+=n;
				}
				total+=k;
				if(total>=smax)
					break;
				 
			}
			cout<<"Case #"<<i+1<<": "<<difference<<endl;
				//code to print the output here

		}
		return 0;
}
