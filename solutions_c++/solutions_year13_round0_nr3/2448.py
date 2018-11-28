#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	unsigned long long int A[]={1,121,4,484,9,10201,1002001,12321,1234321,14641,40804,4008004,44944,100020001,
	10000200001,102030201,10221412201,104060401,121242121,12102420121,123454321,12345654321,125686521,400080004,40000800004,
	404090404,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,
	1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
	int t;
	scanf("%d",&t);
	for( int p=0; p<t; p++)
	{
		long long int m,n,count=0;
		cin>>m>>n;
		for( int i=0; i<39; i++)
		{
			if(A[i]>=m && A[i]<=n)
			{
				count++;
				//cout<<A[i]<<endl;
			}
		}
		printf("Case #%d: %d\n",p+1,count);
	}
}
