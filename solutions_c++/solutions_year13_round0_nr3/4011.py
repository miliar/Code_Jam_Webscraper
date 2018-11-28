#include <stdio.h>
#include <assert.h>
char str[100];
inline bool isPalin(long long int n)
{
	if(n<0)
		assert(0);
	if(n==0)
		return 1;
	long long int nCopy=n;
	str[0] = nCopy%10+'0';
	int len=1;
	while(nCopy/=10)
	{
		str[len++]=nCopy%10+'0';
	}
	for (int i = 0; i < len/2; ++i)
	{
		if(str[i] != str[len-i-1])
			return false;
	}
	return true;
}
static const int arrLen = 39;
static const long long int arr[] = {	
	1,
	4,
	9,
	121,
	484,
	10201,
	12321,
	14641,
	40804,
	44944,
	1002001,
	1234321,
	4008004,
	100020001,
	102030201,
	104060401,
	121242121,
	123454321,
	125686521,
	400080004,
	404090404,
	10000200001,
	10221412201,
	12102420121,
	12345654321,
	40000800004,
	1000002000001,
	1002003002001,
	1004006004001,
	1020304030201,
	1022325232201,
	1024348434201,
	1210024200121,
	1212225222121,
	1214428244121,
	1232346432321,
	1234567654321,
	4000008000004,
	4004009004004
};
int main(int argc, char const *argv[])
{
	int t=0;
	scanf("%d\n", &t);
	for(int i=0; i<t; i++)
	{
		long long int start=0, end=0;
		scanf("%lld %lld\n", &start, &end);
		int sIdx=0, eIdx=arrLen-1;
		while(arr[sIdx] < start)
			sIdx++;
		while(arr[eIdx] > end)
			eIdx--;
		printf("Case #%d: %d\n", i+1, eIdx-sIdx+1);
	}
	return 0;
}