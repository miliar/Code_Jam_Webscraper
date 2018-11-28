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

using namespace std;

int main() 
{
  int testCase, index = 1, n = 0;
  int sMax;
  int total,add;
  int prev;
  char count,space;
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  scanf("%d", &testCase);

  for (index=1;index<=testCase;index++) 
  {
	 total = 0;
	 prev = 0;
	 add = 0;

    printf("Case #%d: ", index);
	scanf("%d", &sMax);
	space=getchar();

	if (sMax == 0)
	{
		count=getchar();
		add = 0;			
	}
	else
	{		
		for(int i=1; i<=(sMax+1); ++i)
		{
			count=getchar();
			count = count - '0';
			total += count;
			if (i>total)
			{
				add+= (i -total);	
				total+= (i -total);
			}
		}
	}
	
	 printf("%d\n", add);
  }   
  return 0;
}
