#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>
#include<math.h>
using namespace std;
long long arr[]={ 1 , 4 , 9 , 121 , 484 , 10201 , 12321 , 14641 , 40804 , 44944 , 1002001 , 1234321 , 4008004 , 100020001 , 102030201 , 104060401 , 121242121 , 123454321 , 125686521 , 400080004 , 404090404 , 10000200001 , 10221412201 , 12102420121 , 12345654321 , 40000800004 , 1000002000001 , 1002003002001 , 1004006004001 , 1020304030201 , 1022325232201 , 1024348434201 , 1210024200121 , 1212225222121 , 1214428244121 , 1232346432321 , 1234567654321 , 4000008000004 , 4004009004004 };	
int T;
long long A,B,counter;
int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int CASE=1 ; CASE<=T ; CASE++)
	{
		counter=0;
		scanf("%lld %lld",&A,&B);
		for(int i=0 ; i<39 ; i++)
		{
			if(arr[i]>=A && arr[i]<=B)
				counter++;
		}
		printf("Case #%d: %lld\n",CASE,counter);
	}
	return 0;
}