#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <map>
using namespace std;
#define Submit
long long bit[] ={
	1LL,
	4LL,
	9LL,
	121LL,
	484LL,
	10201LL,
	12321LL,
	14641LL,
	40804LL,
	44944LL,
	1002001LL,
	1234321LL,
	4008004LL,
	100020001LL,
	102030201LL,
	104060401LL,
	121242121LL,
	123454321LL,
	125686521LL,
	400080004LL,
	404090404LL,
	10000200001LL,
	10221412201LL,
	12102420121LL,
	12345654321LL,
	40000800004LL,
	1000002000001LL,
	1002003002001LL,
	1004006004001LL,
	1020304030201LL,
	1022325232201LL,
	1024348434201LL,
	1210024200121LL,
	1212225222121LL,
	1214428244121LL,
	1232346432321LL,
	1234567654321LL,
	4000008000004LL,
	4004009004004LL
};

int main()
{
#ifdef Submit
	freopen("D:\\test.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
#endif
	int t,times = 1;
	long long n,i,A,B;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%lld %lld" ,&A, &B);
		int cnt1,cnt2;
		cnt1 = cnt2 = 0;
		for(i = 0; i < 39; i++)
		{
			if(bit[i] < A)
			{
				cnt1++;
			}	
		}

		for(i = 0; i < 39; i++)
		{
			if(bit[i] <= B)
			{
				cnt2++;	
			}
		}
		printf("Case #%d: %d\n", times++, cnt2-cnt1);
	}
	return 0;
}