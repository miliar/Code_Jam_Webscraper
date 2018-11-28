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

void SetNumbers(long value, char * numbers)
{
	char str[15] = {0};
	int len = 0, i, checkNumber;
	sprintf(str, "%ld", value);
	len = strlen(str);
	for (i = 0; i < len; ++i)
	{
		checkNumber = str[i] - '0';
		numbers[checkNumber] = '1';
	}
}

int main() 
{

	int N;
	long caseN;
  int testCase, index = 1;
  char numbers[10] = {0};
 
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  scanf("%d", &testCase);

  for (index=1;index<=testCase;index++) 
  {
	N = 0;

    printf("Case #%d: ", index);
	scanf("%d", &N);	

	if (N == 0)
	{
		printf("%s\n", "INSOMNIA");
	}
	else
	{	
		strcpy(numbers, "0000000000");
		
		for(int i=1; i<=10000; ++i)
		{
			caseN = N * i;
			SetNumbers(caseN, numbers);

			if(strcmp(numbers, "1111111111") == 0)
			{
				printf("%d\n", caseN);
				break;
			}
		}		 
	}
  }   
  return 0;
}
