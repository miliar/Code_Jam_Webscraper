#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char LL[200];
int k;
bool check(int a,int b)
{
	int o=0;
	for(int i=a;i<=b;i++)
	{
           char c=LL[i];
	   if(!(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'))
	   {
		   o++;
		   if(o==k)
			   return true;

	   }
	   else
	   {
		   o=0;
	   }
	}
	return false;
	  
}
int main()
{
int tc,ii=1,count,l;
cin>>tc;
while(ii<=tc)
{
	cin>>LL>>k;
	l=strlen(LL);
	count=0;
	for(int i=0;i<l;i++)
		for(int j=i+k-1;j<l;j++)
			if(check(i,j))
				count++;
	printf("Case #%d: %d\n",ii,count);
	ii++;
}
}
