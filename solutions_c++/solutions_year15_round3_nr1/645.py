#include<iostream>
#include<conio.h>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<stack>
#include<queue>
#include<cctype>
#include<iomanip>
using namespace std;
#define sz 10000000
#define ull unsigned long long
void solve()
{
	int r,c,w;
	cin>>r>>c>>w;
	if(r==1)
	{
		if(w==c)
		{
			cout<<w;
		return;
		}
		else
		{
			int x=c/w;
			int a1=w-1;
			int a2=c-x*w;
			if(a2>1)
			{
				a2=1;
			}
			cout<<x+(a2+a1);
		}	
	}	
	else
	{
//		cout<<"-----";
		if(w==c)
		{
			cout<<(w+r-1);
		}
		else
		{
			int x=0;
			for(int pp=0;pp<r;pp++)
			{
				x+=c/w;
//				cout<<"i"<<x<<endl;
			}
			int a1=w-1;
			int tp=c/w;
			int a2=c-tp*w;
			if(a2>1)
			{
				a2=1;
			}
//			cout<<"a2 a1"<<a2<<" "<<a1<<endl;
			cout<<x+(a2+a1);
		}
	}
}
int main()
{
	int test;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}
