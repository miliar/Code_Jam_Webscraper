#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>
#include<algorithm>
#include<memory>
#include<map>
#include<queue>
#include<limits>
#include<iomanip>
#include<fstream>
using namespace std;

int main()
{
	freopen("1_large.in","r",stdin);
	freopen("1-olarge.out","wt",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		
		long long n;
		cin>>n;
		cout<<"Case #"<<tc<<": ";	
		if(n==0)
		cout<<"INSOMNIA"<<endl;
		else
		{
		long long m=n,i=1,ans;
		int count[10]={0},y=0;
		while(1)
		{
			m=n*i;
			while(m>0)
			{
				int a=m%10;
				count[a]=1;
				m/=10;
			}
			y=0;
			for(int l=0;l<10;l++)
			{
					if(count[l])
					y++;
			}
			if(y==10 || i==1000)
			{
				ans=n*i;
				break;
			}
			i++;
		}
		if(y==10)
		cout<<ans<<endl;
		else
		cout<<"INSOMNIA"<<endl;
		
		
		}
		
		
		
		//cout<<endl;
	}
	return 0;
}
