#include<stdio.h>
#include<iostream>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<utility>
#define PB push_back
#define MP make_pair
#define LL long long int
#define sc(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
using namespace std;
int main()
{
	int ans,t,i,j,n,k,temp,a,arr[20];
	sc(t);
	for(k=1;k<=t;k++)
	{
		for(i=1;i<=16;i++)
		arr[i] = 0;
		
		sc(a);
		for(i=1;i<=4;i++)
		{
			if(i == a)
			{
				for(j=1;j<=4;j++)
				{
					cin>>temp;
					arr[temp]++;
				}
				
			}
			else
			{
				for(j=1;j<=4;j++)
				{
					cin>>temp;
				}
			}
		}
		
		sc(a);
		for(i=1;i<=4;i++)
		{
			if(i == a)
			{
				for(j=1;j<=4;j++)
				{
					cin>>temp;
					arr[temp]++;
				}
				
			}
			else
			{
				for(j=1;j<=4;j++)
				{
					cin>>temp;
				}
			}
		}
		
		ans = 0;
		for(i=1;i<=16;i++)
		{
			if(arr[i] == 2)
			{
				temp = i;
				ans++;
			}
		}
		
		if(ans == 0)
		{
			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
		}
		else if(ans == 1)
		{
			cout<<"Case #"<<k<<": "<<temp<<endl;
		}
		else
		{
			cout<<"Case #"<<k<<": Bad magician!"<<endl;
		}
	}	
	return 0;
}

