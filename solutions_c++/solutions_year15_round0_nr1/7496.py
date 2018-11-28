#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

int main()
	{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for (int qq=1;qq<=100;qq++) 
  		{
		printf("Case #%d: ", qq);
//		scanf("%lf",&x);
//	 	printf("%.7lf", time+couldwin);

		int length;
		scanf("%i", &length);
		int audience = 0;
		int tneed = 0;

		char string[length+1]; 
				scanf("%s",string);
		for (int w=0; w < length + 1; w++)
			{
			int cneed = 0;
			int i = string [w] - '0';
			if (w == 0)
				{
				audience = audience + i;
				continue;
				}
			if (w <= audience)
				{
				audience = audience + i;
				continue;
				}
			else
				{
				cneed = w - audience;
				tneed = tneed + cneed;
				audience = audience + cneed + i;
				}
			}
		printf("%i", tneed);
		printf("\n");
		}
	return 0;
	}
