#include<iostream>
#include<stdio.h>
using namespace std;
char str[1000010];
int main()
{
	int n;
	int t;
//	freopen("abc.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	cin>>t;
	long long int req=0;
	long long int clap=0;
	int cas=0;
	while(t--)
	{
		cas++;
		req=0;
		clap=0;
		cin>>n;
		cin>>str;
		clap+=str[0]-'0';
		for(int i=1;i<=n;i++)
		{
			if(clap>=i)
			{
				clap+=(str[i]-'0');
				
			}
			else
			{
				if(str[i]-'0'>0)
				{
				req+=(i-clap);
				clap=clap+(i-clap)+(str[i]-'0');
			    }
			}
		}
	   cout<<"Case #"<<cas<<": "<<req<<endl;
	}
	return 0;
}
