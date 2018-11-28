#include<stdio.h>
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#define tr(c,i)    for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
using namespace std;
int palindrome_fun(long long  int check_p)
{
	long long int x = check_p;
	long long int y=0;
	while(x)
	{
		y = y*10 + x%10;
		x/= 10;
	}
	if(check_p==y)
		return 1;
	return 0;
}
int main()
{
	int T;
	scanf("%d",&T);
	int i;
	int Case=1;
	int l=0;
	long long int pal;
	/*for(i=0;i<=10000000;i++)
	  {
	  if(palindrome_fun(i))
	  {
	  pal=i;
	  pal*=pal;
	  if(palindrome_fun(pal))
	  {
	  Fair_Sqr[l]=pal;
	  l++;
	  }
	  }
	  }*/

	long long int Fair_Sqr[]={0,1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
	while(T--)
	{
		long long int A,B;
		int final_count=0;
		scanf("%lld%lld",&A,&B);
		for(i=0;i<40;i++)
		{
			if(Fair_Sqr[i]>=A && Fair_Sqr[i]<=B)
			{
				final_count++;
			}
		}
		printf("Case #%d: %d\n",Case,final_count);
		Case++;
	}
	return 0;
}

