#include <cstdio>
#include <cmath>

void bitPlus(bool (&B)[32], unsigned long long size)
{
	bool carry;
	for(unsigned long long i = 1 ; i < size - 1 ; i++)
	{
		carry = false;
		if(B[size - i - 1] == 1)
		{
			B[size - i - 1] = 0;
			carry = true;
		}
		else
		{	B[size - i - 1] = 1;	}
	
		if(carry == false)
		{	break;	}
	}
}

unsigned long long bitInterpret(bool (&B)[32], unsigned long long size, unsigned long long interpret)
{
	unsigned long long R = 0;
	for(unsigned long long i = 0 ; i < size ; i++)
	{	R += (B[size - i - 1]) ? pow(interpret, i) : 0;	}
printf("%llu\n", R);
	return R;
}

unsigned long long findDivisor(unsigned long long num)
{
	for(unsigned long long i = 2 ; i <= (unsigned long long)sqrt(num) ; i++)
	{
		if(num % i == 0)
		{	return i;	}
	}
}

unsigned long long primeCheck(unsigned long long num)
{
    unsigned long long rootNum = (unsigned long long) sqrt(num);
    unsigned long long div = 0;
    unsigned long long value = 0;
    for(div = rootNum; num % div; div--);
    if(div == 1) value = 1;
    else value = 0;
    
	return value;
}

int main()
{
	unsigned long long T, N, J;
	unsigned long long P, i, j, k;
	bool bitString[32];
	unsigned long long interpreted[9];
	unsigned long long divisors[9];
	FILE *fin, *fout;
	fin = fopen("C-input.txt", "r");
	fout = fopen("C-output.txt", "w");
	
	fscanf(fin, "%llu", &T);
	fscanf(fin, "%llu %llu", &N, &J);
	
	for(i = 0 ; i < N ; i++)
	{	bitString[i] = 0;	}
	bitString[0] = 1;
	bitString[N - 1] = 1;
	fprintf(fout, "Case #1:\n");
	while(J)
	{
		P = 0;
		for(i = 2 ; i <= 10 ; i++)
		{	interpreted[i - 2] = bitInterpret(bitString, N, i);	}
		for(i = 2 ; i <= 10 ; i++)
		{	P += primeCheck(interpreted[i - 2]);	}
		printf("P = %llu\n", P);
		if(P == 0)
		{
			J--;
			for(i = 2 ; i <= 10 ; i++)
			{	divisors[i - 2] = findDivisor(interpreted[i - 2]);	}
			fprintf(fout, "%llu ", interpreted[8]);
			for(i = 2 ; i <= 10 ; i++)
			{	fprintf(fout, "%llu ", divisors[i - 2]);	}	
			fprintf(fout, "\n");
		}
		printf("%llu \n", interpreted[8]);
		if(bitInterpret(bitString, N, 2) == pow(2, N) - 1)
		{	break;	}
		else
		{	bitPlus(bitString, N);	}
	}
	return 0;
}