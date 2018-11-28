#include<bits/stdc++.h>

#define pb(x) push_back(x);
#define gc getchar_unlocked
#define pc(x) putchar_unlocked(x);
#define inf 1<<30
#define ll long long   
using namespace std;

typedef pair<int,int> pii;

int abso(int a,int b)
{
	if(a<b)
		return b-a;
	else
		return a-b;
}

double power(double x,ll e)
{
	double temp;
	if(e==0)
		return 1;
	if(e%2==0)
	{
		temp=power(x,e/2);
		return temp*temp;
	}
	else
	{
		temp=power(x,e/2);
		return temp*temp*x;
	}
}

int flag;

int main()
{
	int t,ans;
	string str;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		ans=0;
		cin>>str;
		if(str[0]=='-')
		{
			flag=1;
			ans++;
		}
		else
			flag=0;
		for(int i=1;i<str.size();i++)
		{
			if(str[i]=='+')
			{
				flag=0;
				continue;
			}
			else
			{
				if(flag==0)
				{
					flag=1;
					ans+=2;
				}
				else
					continue;
			}	
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}
