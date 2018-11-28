#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long t;
	FILE *ip,*op;
	ip=fopen("input.in","r");
	if(ip==NULL)
	{
		cout<<"ERROR!!";
		exit(0);
	}
	op=fopen("output1.in","w");
	if(op==NULL)
	{
		cout<<"ERROR!!";
		exit(0);
	}
	fscanf(ip,"%lld",&t);
	char str[1000],temp;
	long long m=1;
	while(t--)
	{   
	    long long i,c=1,x;
	    fscanf(ip,"%s",&str);
		i=0;
		temp=str[0];
		i=1;
		while(i<strlen(str))
		{
			if(str[i]==temp)
			   i++;
		    else
		      {
		      	c++;
		      	temp=str[i];
			  }
		}
		 x=strlen(str);
		 if(str[x-1]== '+')
		  c=c-1;
		else if(str[x-1]=='-')
		  c=c;
		fprintf(op,"Case #%lld: %lld\n",m,c);
		m++;
	}
}
