//#ifdef QWERTYUIOP
#include <stdio.h>

FILE *in = fopen("input", "r");
FILE *out= fopen("output","w");

int palindrom(int a)
{
	int p10;
	for(p10 = 10; p10 <= a * 10; p10*=100)
	{
		a *= 10;
		a += (a / p10) % 10;
	}
	return a;
}
int palindrom2(int a)
{
	int p10;
	for(p10 = 100; p10 <= a * 10; p10*=100)
	{
		a *= 10;
		a += (a / p10) % 10;
	}
	return a;
}

bool e_palindrom(long long a)
{
	long long p10_1 = 1, p10_2 = 1;

	while(p10_1 <= a)
		p10_1 *= 10;
	p10_1 /= 10;

	while(p10_1 > p10_2)
	{
		if((a / p10_1) % 10 != (a / p10_2) % 10)
			return false;
		p10_1 /= 10;
		p10_2 *= 10;
	}
	return true;
}

int result()
{
	long long a, b;
	fscanf(in, "%lli %lli", &a, &b);

	int i, pali, nrsol = 0;
	int put10 = 10;
	long long patrat;

	for(i = 1; i <= 10000; i++)
	{
		if(i == put10)
		{
			put10 *= 100;
			i *= 10;
		}
		//123 -> pali = 12321
		pali = palindrom2(i);

		patrat = pali;
		patrat = patrat * patrat;

		if(patrat < a)
			continue;
		if(patrat > b)
			break;

		if(e_palindrom(patrat))
			nrsol++;
	}

	for(i = 1; i <= 10000; i++)
	{
		//123 -> pali = 12321
		pali = palindrom(i);

		patrat = pali;
		patrat = patrat * patrat;

		if(patrat < a)
			continue;
		if(patrat > b)
			break;

		if(e_palindrom(patrat))
			nrsol++;
	}

	return nrsol;
}

int main()
{
	int T, TC;
	fscanf(in, "%i", &T);
	for(TC = 1; TC <= T; TC++)
	{
		fprintf(out, "Case #%i: %i\n", TC, result());
	}
}

//#endif
