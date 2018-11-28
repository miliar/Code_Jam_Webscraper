#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
 #define MAX(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; })
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define NUMBEROFFAIR 39
long long int values[NUMBEROFFAIR]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int binarySearch(long long int key)
{
	int start=0;
	int  end=NUMBEROFFAIR;
	
	
	while(start<=end)
	{
		int mid=(start+end)/2;
		//printf("mid:%d\n",mid);
		if(values[mid]==key)
			return mid;
		else if(key>values[mid])
			start=mid+1;
		else
			end=mid-1;
			
	}
	return start;
}
int main ()
{
	int T;
	long long int A,B;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	//while(T--)
	{
		scanf("%lld %lld",&A,&B);
		int countOFFair=0;
		int startIndex=binarySearch(A);
		//printf("starting at :%d",startIndex);
		while(startIndex < NUMBEROFFAIR && values[startIndex]<=B )
		{
			countOFFair++;
			startIndex++;
		}
		printf("Case #%d: %d\n",(i+1),countOFFair);
	}
	
}
