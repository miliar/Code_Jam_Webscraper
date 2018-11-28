#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
void check(char val[],long long int len,long long int num);
int main(void)
{
    freopen("large.in","r",stdin);
   freopen("she.txt","w",stdout);
	long long int T;
	scanf("%lld",&T);
	if(T>=1 && T<=100)
	{
		char val[105];
		long long int num=1;
		while(T--)
		{
			//int count=1;
			cin>>val;
			long long int len;
			len=strlen(val);
			check(val,len,num);
			num++;
			//cout<<len<<endl;
		}
	}
	return 0;
}
void check(char val[],long long int len,long long int num)
{
  long long int i=0,j,count=0;
	while(i<=len-1)
	{
		if(val[i]!=val[i+1] &&val[i+1]!='\0')
		{
			if(val[i]=='+')
			{
			  for(j=0;j<=i;j++)
		     	{
				 val[j]='-';
			   }
			   count++;
			   i=0;	
			}
			else
			{
			  for(j=0;j<=i;j++)
		     	{
				val[j]='+';
			   }
			   i=0;	
			   count++;
			}
			
		}
		else
		{
			i++;
		}
	}
	if(val[0]=='-')
	count++;
	printf("Case #%lld: %lld\n",num,count);
	//cout<<count<<endl;
}

