#include<iostream>
#include<string.h>
using namespace std;
int a[26];
int isclear()
{
	for(int i=0;i<26;i++)
	{
	
	if(a[i]>=1)
	return 1;
}
	return 0;
}
int main(){
	
	int n,t,i,j,d[10];string s;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		for(j=0;j<10;j++)
	   {
	   	d[j]=0;
	   }
	   for(j=0;j<26;j++)
	   {
	   	a[j]=0;
	   }
		cin>>s;
		for(j=0;j<s.length();j++)
		{
		a[s[j]-'A']++;
		}
	
		if(a[25]>=1)
		{
			while(a[25]!=0)
			{
			a[4]--;
			a[14]--;
			a[17]--;
			a[25]--;
			d[0]++;
		}
		}
		if(a[23]>=1)
		{
			while(a[23]!=0)
			{
			a[8]--;
			a[18]--;
			a[23]--;
			
			d[6]++;
		}
			
		}
		if(a[20]>=1)
		{
			while(a[20]!=0)
			{
			a[17]--;
			a[14]--;
			a[5]--;
			a[20]--;
			d[4]++;
		}
		}
		if(a[6]>=1)
		{
		while(a[6]!=0)
			{
			a[6]--;
			a[4]--;
			a[8]--;
			a[7]--;
			a[19]--;
			d[8]++;
		}
	}
	   if((a[22]>=1))
	   {
	   	while(a[22]!=0)
			{
			a[22]--;
			a[19]--;
			a[14]--;
			
			d[2]++;
		}
	   }
	   int flag=isclear();
	   if(flag==1)
	   while(flag==1)
	   {
	   
	   if(a[14]>=1&&a[13]>=1&&a[4]>=1)
	   {
	   	a[14]--;
	   	a[13]--;
	   	a[4]--;
	   	d[1]++;
	   }
	   if(a[19]>=1&&a[7]>=1&&a[17]>=1&&a[4]>=2)
	   {
	   	a[19]--;
	   	a[7]--;
	   	a[17]--;
	   	a[4]-=2;
	   	d[3]++;
	   }
	   if(a[5]>=1&&a[8]>=1&&a[21]>=1&&a[4]>=1)
	   {
	   	a[5]--;
	   	a[8]--;
	   	a[21]--;
	   	a[4]--;
	   	d[5]++;
	   }
	   if(a[18]>=1&&a[4]>=2&&a[21]>=1&&a[13]>=1)
	   {
	   	a[18]--;
	   	a[4]-=2;
	   	a[21]--;
	   	a[13]--;
	   	d[7]++;
	   }
	   if(a[13]>=2&&a[8]>=1&&a[4]>=1)
	   {
	   	a[13]-=2;
	   	a[8]--;
	   	a[4]--;
	   	d[9]++;
	   }
	   flag=isclear();
}
cout<<"Case #"<<i<<": ";
	   for(j=0;j<10;j++)
	   {
	   	if(d[j]>=1)
	   	{
	   		while(d[j]!=0)
	   		{
	   			cout<<j;
				   d[j]--;
	   		}
	   	}
	   }
	   
	   }
	}
	
