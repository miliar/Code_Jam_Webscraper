#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>
#include<algorithm>
#include<memory>
#include<map>
#include<queue>
using namespace std;

int main()
{
	freopen("mayank.out","wt",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
	
	int s;
	cin>>s;
	string p;
	cin>>p;
	int a[s+2];
	for(int i=0;i<=s;i++)
	{
		a[i]=p[i]-48;
		//cout<<a[i]<<" ";
	}
	cout<<"Case #"<<tc<<": ";
	if(s==0)
	{
		cout<<"0"<<endl;
	}
	else
	{
		int count=0,count2=0;
		for(int i=0;i<=s;i++)
		{
			if(i==0)
			{
				if(a[0])
				count+=a[0];
			}
			else
			{
			  if(i>count && a[i]>0)
			  {
			  	int k=i-count;
				count2+=k;
				count=count+a[i]+k;
				//cout<<i<<" "<<count2<<" "<<count<<endl;
				}	
				else
				{
				
				count+=a[i];
				//cout<<i<<" "<<count<<endl;
				}
			}
		}
		cout<<count2<<endl;
	}
	

	}
return 0;
}

