#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;
#define LL long long
int n,m;
int pal(int num)
{
	int i,j,k;
	if(num/10==0)	return 1;
	int x=num,t=0;
	while(x)
	{
		k=x%10;
		x/=10;
		t=t*10+k;
	}
	if(num==t)
		return 1;
	else
		return 0;
}
int square(int num)
{
	int a=sqrt(double(num));
	if(a*a==num&&pal(a))
		return 1;
	else
		return 0;
}
int solve()	
{
	int i,j,k;
	int ans=0;
	for(int num=n;num<=m;num++)
	{
		if(pal(num)&&square(num))
		{	
			ans++;
		}
	}
	return ans;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("bp.txt","w",stdout);
	int i,j,k;
	int t,cas;
	cin>>t;
	//fin>>t;
	for(cas=1;cas<=t;cas++)
	{
		cin>>n>>m;
		int res=solve();				
		printf("Case #%d: %d\n",cas,res);	

	}
	
	return 0;	
}
