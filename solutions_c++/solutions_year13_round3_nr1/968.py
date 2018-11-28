#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;
int absint(int a)
{
	return a>0 ? a:-a;
}
bool juge(char c)
{
	return (!(c=='e'||c=='a'||c=='i'||c=='o'||c=='u'));
}
bool f[1000000];
	int pre[1000000];
int main()
{
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		string str;
		int n;
		cin>>str>>n;
		memset(f,false,sizeof(bool)*1000000);
		int nowlen=0;
		int prei=-1;
		for(int i=0;i<str.size();i++)
		{
			if(juge(str[i]))
			{
				nowlen++;
				if(nowlen>=n)
				{
					f[i]=true;
					pre[i]=prei;
					prei=i;
				}
			}
			else
			{
				nowlen=0;
			}
		}

		long long sum=0;
		int p=0;
		int cal=0;
		while(!f[p])
		p++;
		if(p<str.size())
		{
			sum+=p-n+2;
			cal=p-n+2;
		}
		p++;
		for(;p<str.size();p++)
		{
		   if(!f[p])
			   sum+=cal;
		   else
		     {
				 if(f[p-1])
					 cal+=1;
				 else
				 {
					 cal+=p-pre[p];
				 }
				  sum+=cal;
		      }
		}
		cout<<"Case #"<<k<<": "<<sum<<"\n";

	}

	return 0;
}