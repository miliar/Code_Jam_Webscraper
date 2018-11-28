#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <string>
#include <list>
#include <vector>
#include <map>

using namespace std;

#define PI 3.1415926535897932384626433832795
#define eps 0.0000001

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A_large.out", "w", stdout);

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int T;
	scanf("%d",&T);

	for(int x = 1; x<=T; x++)
	{
		long long r, t;
		scanf("%lld %lld",&r,&t);

		int result = 0;
		
		while(true)
		{
			long long mainArea = 2*r+1;
			if(mainArea<=t)
			{
				result++;
				t-=mainArea;
			}
			else break;
			r+=2;
		}
		printf("Case #%d: %d\n",x,result);
	}
}