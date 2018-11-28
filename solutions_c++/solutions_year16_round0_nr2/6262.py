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

void FlipCakes(int value, char * cakes)
{	
	int  i;	
	for (i = 0; i < value; ++i)
	{
		if (cakes[i] == '+')
			cakes[i] = '-';
		else
			cakes[i] = '+';
	}
}

int main() 
{

	
  int testCase, index = 1, size;
  char input[100], cakes[100];
 
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  scanf("%d", &testCase);

  for (index=1;index<=testCase;index++) 
  {
    printf("Case #%d: ", index);
	scanf("%s", &input);	

	for(int i = 0; i < 100; ++i)
		cakes[i] = '+';

	size = strlen(input);

	for (int i = 0; i < size; ++ i)
	{		
		cakes[i] = input[i];
	}	
		
	for(int i=0; i<=10000; ++i)
	{	
		int resp = 1;

		for(int j = 0; j < 100; ++j)
		{
			if(cakes[j] == '-')
			{
				resp = 0;
				break;
			}
		}

		if(resp == 1)
		{
			printf("%d\n", i);
			break;
		}

		for(int t = 1; t <= size; ++t)
		{
			if (cakes[t-1] != cakes[t])
			{
				FlipCakes(t, cakes);
				break;
			}
		}

	}		 
	
  }   
  return 0;
}
