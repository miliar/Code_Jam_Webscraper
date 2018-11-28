#include<stdio.h>
#include "stdafx.h"
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
typedef long long ll;
bool isp(ll a)
{
	vector<int>vec;
	for(;;)
	{
		if(a==0)
		{
			break;
		}
		vec.push_back(a%10);
		a/=10;
	}
	for(int i=0;i<vec.size();i++)
	{
		if(vec[i]!=vec[vec.size()-1-i])
		{
			return false;
		}
	}
	return true;
}
ll ans[39]={
1
,4
,9
,121
,484
,10201
,12321
,14641
,40804
,44944
,1002001
,1234321
,4008004
,100020001
,102030201
,104060401
,121242121
,123454321
,125686521
,400080004
,404090404
,10000200001
,10221412201
,12102420121
,12345654321
,40000800004
,1000002000001
,1002003002001
,1004006004001
,1020304030201
,1022325232201
,1024348434201
,1210024200121
,1212225222121
,1214428244121
,1232346432321
,1234567654321
,4000008000004
,4004009004004};
//void calc()
//{
//	for(ll i=1;i<=10000000;i++)
//	{
//		if(isp(i))
//		{
//			if(isp(i*i))
//			{
//				ans.push_back(i*i);
//			}
//		}
//	}
//}
int main()
{
	FILE *fr=fopen("c-large-1.in","r");
	FILE *fw=fopen("out.txt","w");
	int test;
	fscanf(fr,"%d",&test);
	//calc();
	for(int i=0;i<test;i++)
	{
		ll a,b;
		fscanf(fr,"%lld%lld",&a,&b);
		int low1=lower_bound(ans,ans+39,a)-ans;
		int low2=lower_bound(ans,ans+39,b+1)-ans;
		fprintf(fw,"Case #%d: %d\n",i+1,low2-low1);
	}
}