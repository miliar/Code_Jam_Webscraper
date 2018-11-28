#include<cstdio>
#include<iostream>
#include<cassert>
#include<cctype>
#include<cfloat>
#include<climits>
#include<cstring>
#include<bitset>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
int ar[1009],temp[1009]={0},te[10];
bool ispalin(int n)
{
	int i,j;
	i=-1;
	//cout<<n<<"--";
	while(n>0)
	{
		te[++i]=n%10;
		n=n/10;
	}
	//for(j=0;j<=i;j++)
	//{
	//cout<<te[j]<<" ";
	//}
	//cout<<endl;
	for(j=0;j<=i;j++)
	{
		if(te[j]!=te[i-j])
			return false;
	}
	return true;
}



void init()
{
	int i,j;
	for(i=1;i<1009;i++)
	{
		if(ispalin(i))
		{
			//cout<<i<<endl;
			temp[i]=1;
		}
	}
	//cout<<"-----sq-"<<endl;
	for(i=0;i<1009;i++)
	{
		if(temp[i]==1&&(i*i)<1009&&ispalin(i*i))
		{
			ar[i*i]=1;
			//cout<<i*i<<endl;
		}
	}
}

void disp()
{
	for(int i=0;i<1009;i++)
	{
		if(ar[i]==1)
			cout<<i<<endl;
	}
}

int main()
{
	int t,i,j,k,a,b,counti;
	init();
	k=0;
	//disp();
	scanf("%d",&t);
	while(t--)
	{
		counti=0;
		++k;
		scanf("%d %d",&a,&b);
		for(i=a;i<=b;i++)
		{
			if(ar[i]==1)
			{
				//cout<<i<<endl;
				counti++;
			}
		}
		printf("Case #%d: %d\n",k,counti);
	}
	return 0;
}
