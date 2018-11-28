#include <cstdio>
#include <cstdlib>
#include <cmath>

#define CODEI 1
#define CODEJ 2
#define CODEK 3
#define ONE 4
using namespace std;

int divide(int result, int leftSide)
{
	int absRes = fabs(result);
	int absLeft = fabs(leftSide);
	int resSign = result < 0? -1 :1;
	int leftSign = leftSide < 0? -1 :1;
	int sign = leftSign * resSign;
	switch(absRes)
	{
		case  ONE:
			if (absLeft == ONE)
				return sign * ONE;
			else
				return sign * absLeft * -1;

		case CODEI:
			if (absLeft == ONE)
			 	return sign * absRes;
			if (absLeft == CODEI)
				return sign *  ONE;
			if (absLeft == CODEJ)
				return sign *  CODEK;
			if (absLeft == CODEK)
				return sign * -1 * CODEJ;
		case CODEJ:
			if (absLeft == ONE)
			 	return sign * absRes;
			if (absLeft == CODEI)
				return sign * CODEK * -1;
			if (absLeft == CODEJ)
				return sign * ONE ;
			if (absLeft == CODEK)
				return sign * CODEI;
		case CODEK:
			if (absLeft == ONE)
			 	return sign * absRes;
			if (absLeft == CODEI)
				return sign * CODEJ;
			if (absLeft == CODEJ)
				return sign * CODEI * -1;
			if (absLeft == CODEK)
				return sign * ONE ;
	}
}
int mult(int first, int second)
{
	int sign = first*second;
	if (sign > 0)
		sign = 1;
	else 
		sign = -1;


	first = fabs(first);
	second = fabs(second);
	switch(first)
	{
		case  ONE:
			return sign * second;
		case CODEI:
			if (second == ONE)
			 	return sign * second;
			if (second == CODEI)
				return sign * ONE * -1;
			if (second == CODEJ)
				return sign * CODEK;
			if (second == CODEK)
				return sign * CODEJ * -1;
		case CODEJ:
			if (second == ONE)
			 	return sign * second;
			if (second == CODEI)
				return sign * CODEK * -1;
			if (second == CODEJ)
				return sign * ONE * -1;
			if (second == CODEK)
				return sign * CODEI;
		case CODEK:
			if (second == ONE)
			 	return sign * second;
			if (second == CODEI)
				return sign * CODEJ;
			if (second == CODEJ)
				return sign * CODEI * -1;
			if (second == CODEK)
				return sign * ONE * -1;
	}
}
int solve(void)
{
	int count;
	int multiply;
	scanf("%d %d", &count, &multiply);
	int total = count*multiply;
	int * vals = new int[total];
	int * prec = new int[total];
	char tmp;
	for (int i = 0; i < count;++i)
	{
		scanf(" %c",&tmp );
		int value;
		if (tmp == 'i')
			value = CODEI;
		if (tmp == 'j')
			value = CODEJ;
		if (tmp == 'k')
			value = CODEK;
		for (int j = i; j < total; j+=count)
		{
			vals[j] = value;
		}
	}
	prec[0] = vals[0];
	for (int i = 1; i < total; ++i)
	{
		prec[i] = mult(prec[i-1], vals[i]);
	}
	bool solved = false;
	for (int i = 0; i < total; ++i)
	{
		for (int j = i + 1; j < total; ++j)
		{
			if (prec[i] == CODEI && divide(prec[j], prec[i]) == CODEJ && divide(prec[total-1], prec[j]) == CODEK)
			{
				solved = true;
				break;
			}
		}
		if (solved == true)
			break;
	}
	/*
	for (int i = 0; i < total; ++i)
	{
		printf("%d ", prec[i]);
	}
	printf("\n");
	*/
	return solved;
}

int main(void)
{
	int count;
	scanf("%d", &count);
	for (int i = 0; i < count;++i)
	{
		printf("Case #%d: ",i+1);
		if (solve() == true)
			printf("YES\n");
		else
			printf("NO\n");
	}
	
}