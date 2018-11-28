#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>//deque<int> b;
#include <algorithm>//std::sort sort(b.begin(),b.end());
#define gc getchar_unlocked

using namespace std;

int arrcheck(long long int a[])
{
	int x=0;
	while(x<10)
	{
		if(a[x]!=-1)
		{
			return 1;
		}
		x++;
	}
	return 0;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
	long long int cases,ans,c=1,n,a[10];
	cin>>cases;
	while(c<=cases)
	{
		ans=0;
		long long int x=0;
		while(x<10)
		{
			a[x]=x;
			x++;
		}
		cin>>n;
		long long int part,temp=n,i=2;
		while(arrcheck(a) && temp!=0)
		{
			while(temp>0)
			{
				part=temp%10;
				if(a[part]!=-1)
				{
					a[part]=-1;
				}
				temp=temp/10;
				//cout<<part<<" ";
			}
			temp=n*i;
			ans=temp;
			i++;
		}
		if(ans!=0)
		{
			cout<<"Case #"<<c<<": "<<ans-n<<"\n";
		}
		else
		{
			cout<<"Case #"<<c<<": "<<"INSOMNIA\n";
		}
		c++;
	}
}