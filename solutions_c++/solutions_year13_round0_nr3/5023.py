#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define ASSERT(X) {if (!(X)) {printf("\n assertion failed at line %d\n",__LINE__);exit(0);}}

unsigned long long reverseInt(unsigned long long input)
{
	unsigned long long reversedNum = 0;

	unsigned long long input_long = input;

	while (input_long != 0)
	{
		reversedNum = reversedNum * 10 + input_long % 10;
		input_long = input_long / 10;
	}

	return (unsigned long long)reversedNum;
}

bool isPalindrom(unsigned long long nb)
{
	char buffer[102];
	_itoa(nb, buffer, 10);
	
	int digits = strlen(buffer);
	int halfDigits = digits / 2;

	for (int i = 0; i <= halfDigits; i++)
	{
		if (buffer[i] != buffer[digits - i - 1])
		{
			return false;
		}
	}

	return true;
}

unsigned long long checkNumber(unsigned long long nb, unsigned long long min, unsigned long long max)
{
	unsigned long long s = pow(nb,2);

	if ((s >= min) && (s <= max))
	{
		if (isPalindrom(s))
		{
			return s;
		}
	}
	return 0;
}

typedef struct
{
	unsigned long long min;
	unsigned long long max;
} interval;

interval t[10000];

unsigned long long answers[100000];
int nbAnswers = 0;

int main()
{
	freopen("C.in","r",stdin);
	freopen("C2.out","w",stdout);

	unsigned long long min, max;
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		scanf("%llu %llu",&min, &max);

		t[case_id - 1].min = min;
		t[case_id - 1].max = max;
	}

	min = 18446744073709551614;
	max = 0;

	for (int i = 0; i< testcase; i++)
	{
		if (t[i].min < min)
		{
			min = t[i].min;
		}

		if (t[i].max > max)
		{
			max = t[i].max;
		}
	}


	unsigned long long mins, maxs;
	char buffer[102];

	int minDigits, maxDigits;

	mins = sqrt(min);
	maxs = sqrt(max);

	_itoa(mins, buffer, 10);
	minDigits = strlen(buffer);
	_itoa(maxs, buffer, 10);
	maxDigits = strlen(buffer);

	for (int digits = minDigits; digits <= maxDigits; digits++)
	{
		//Nombre pair de digit
		if (digits % 2 == 0)
		{
			int halfDigits = (digits/2);
			for (unsigned long long i = pow(10, halfDigits - 1); i <= (pow(10, (halfDigits)) - 1); i++)
			{
				unsigned long long currNumbers = (i * pow(10, halfDigits)) + reverseInt(i);
					
				unsigned long long s = checkNumber(currNumbers, min, max);
				if (s != 0)
				{
					printf("%d\n", s);
					answers[nbAnswers] = s;
					nbAnswers++;
				}
			}
		}
		else
		{
			//Nombre impair de digit
			int halfDigits = (digits/2);
			for (unsigned long long i = pow(10, halfDigits - 1); i <= (pow(10, (halfDigits)) - 1); i++)
			{
				for (int j = 0; j<=9; j++)
				{
					unsigned long long currNumbers = (i * pow(10, halfDigits + 1)) + 
						(j * pow(10, halfDigits)) +
						reverseInt(i);

					unsigned long long s = checkNumber(currNumbers, min, max);

					if (s != 0)
					{
						printf("%d\n", s);
						answers[nbAnswers] = s;
						nbAnswers++;
					}
				}
			}
		}
	}

	for (int case_id=1;case_id<=testcase;case_id++)
	{
		int nbCaseAnswers = 0;
		
		for (int i = 0; i < nbAnswers; i++)
		{
			if ((answers[i] >= t[case_id - 1].min))
			{
				if (answers[i] <= t[case_id - 1].max)
				{
					nbCaseAnswers++;
				}
				//else
				//{
				//	break;
				//}
			}
		}

		printf("Case #%d: ",case_id);
		printf("%d\n", nbCaseAnswers);
		fflush(stdout);
	}
	
	return 0;
}
