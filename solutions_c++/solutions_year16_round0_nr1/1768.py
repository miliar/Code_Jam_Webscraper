#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
#define PB push_back
#define pii pair<int,int>
#define MP make_pair
#define sz size()
#define fi first
#define se second
using namespace std;
typedef long long ll;
int main()
{
	int t,i,j,k,cs,css;
	ll sm,tm;
	int n;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		cin>>n;
		cout<<"Case #"<<cs<<": ";
		if(n==0)
			cout<<"INSOMNIA\n";
		else
		{
			int a[10],ct=0;
			for(i=0;i<10;i++)a[i]=0;
			sm=0;
			while(1)
			{
				sm+=n;
				tm=sm;
				while(tm>0)
				{
					i=tm%10;
					tm/=10;
					if(a[i]==0)
					{
						a[i]=1;
						ct++;
					}
				}
				if(ct==10)break;
			}
			cout<<sm<<endl;
		}
	}
	return 0;
}
