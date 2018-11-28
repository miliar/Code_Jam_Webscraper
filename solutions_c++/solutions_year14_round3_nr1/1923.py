#include <iostream>
#include <stdio.h>
#include <utility>
#include <algorithm>
#include <string>
#include <math.h>
//#define LOCAL
#define rep(i,x,y) for(int i=x;i<=y;++i)
#define dep(i,x,y) for(int i=x;i>=y;--i)
using namespace std;
int main()
{
	#ifdef LOCAL
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int num,den;
		scanf("%d/%d",&num,&den);
		double den2=log(den)/log(2);
		if(den2-int(den2)!=0)
			cout<<"Case #"<<i+1<<": "<<"impossible"<<endl;
		else
		{
			int j=0;
			while(1/pow(2,j)>double(num)/double(den))
				j++;
			//if(j==2) cout<<"Case #"<<i+1<<": "<<1<<endl;
			//else
				cout<<"Case #"<<i+1<<": "<<j<<endl;
		}
	}
	return 0;
}
