#include<stdio.h>
#include<iostream>
#include<string.h>
#include<map>
using namespace std;
int main()
{
	FILE *w;
	w=fopen("bbbc.txt","w");
	int t,j,c=0,k;
	long int n,i,s;
	
	cin>>t;
	for(j=1;j<=t;j++)
	{
		c=0;
		map <int,int> m;
		cin>>n;
		if(n==0)
			fprintf(w,"Case #%d: INSOMNIA\n",j);
		else
		{
			for(i=1;i<=1000000;i++)
			{
				s=n*i;
				while(s!=0)
				{
					m[s%10]=1;
					s=s/10;
				}
				for(k=0,c=0;k<=9;k++)
				{
					if(m[k]==1)
					c++;
				}
				if(c==10)
				{
					fprintf(w,"Case #%d: %ld\n",j,n*i);					
					break;
				}
			}
		}
	
	}
	return 0;
}
