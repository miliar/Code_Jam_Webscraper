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
int bit[105],len;
void cut(__int64 n)
{
	len  = 0;
	while(n)
	{
		bit[len++] = n%10;
		n /= 10;
	}	
}

bool f()
{
	int i;
	for(i = 0; i <= len/2; i++)
	{
		if( bit[i] != bit[len-i-1])	return false;
	}
	return true;
}

int main()
{
	#ifdef Submit
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int t,times = 1;
	__int64 n,i,A,B;
	scanf("%d", &t);
	while(t--)
	{
		int cnt1,cnt2;
		cnt1 = cnt2 = 0;
		scanf("%I64d %I64d" ,&A, &B);
		for(i = 1; i*i < A; i++)
		{
			cut(i);
			if( f() )
			{
				cut(i*i);
				if(f())
				{
					cnt1++;
				}
			}	
		}
		for(i = 1; i*i <= B; i++)
		{
			cut(i);
			if( f() )
			{
				cut(i*i);
				if(f())
				{
					cnt2++;
				}
			}
			
		}
		printf("Case #%d: %d\n", times++, cnt2-cnt1);
	}
	return 0;
}