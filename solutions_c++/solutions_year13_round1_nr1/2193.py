//Coded by Dange Laxmikant
#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<stack>
#include<algorithm>
#include<string>
#include<cstdio>
#include<queue>
#define pi 3.14159
typedef long long ll;
using namespace std;
 
int main()
{
	int T,i=1,j;
	ll c,d,r,t;
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>r>>t;
		c=0;
		d=0;
		for(j=0;j<t;j=j+2)
		{
			c=c+(((r+j+1)*(r+j+1)-(r+j)*(r+j)));
			if(c>t)
				break;
			else
				d++;
		}
		cout<<"Case #"<<i<<":"<<" "<<d<<"\n";
	}
	return 0;
}
