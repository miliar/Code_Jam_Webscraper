#include <iostream>
#include <stdio.h>
#include <string>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>
#include <map>
// #include <unordered_map>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <climits>
#include <limits.h>
 
#define MOD 1000000007 
 
typedef long long LL;
 
using namespace std;
 
LL gcd(LL u, LL v)
{
	return (v != 0)?gcd(v, u%v):u;
}

int main()
{
	int t;
	cin>>t;		
	for(int tc=1;tc<=t;tc++)
	{
		LL n;
		scanf("%lld", &n);

		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n", tc);		
			continue;
		}

		LL num = 0;
		set<int> digits;
		while(digits.size() != 10)
		{
			num+=n;
			LL temp = num;
			while(temp!=0)
			{
				int r = temp%10;
				if(digits.count(r) == 0)//not in set
					digits.insert(r);
				temp/=10;
			}
		}

		printf("Case #%d: %lld\n", tc,num);		
	}

	return 0;
}
