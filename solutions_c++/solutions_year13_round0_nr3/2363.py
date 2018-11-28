// FairAndSquare.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//using GMP library
#include <gmp.h>


char *listFairAndSquare[48] = 
{
"1",
"4",
"9",
"121",
"484",
"10201",
"12321",
"14641",
"40804",
"44944",
"1002001",
"1234321",
"4008004",
"100020001",
"102030201",
"104060401",
"121242121",
"123454321",
"125686521",
"400080004",
"404090404",
"10000200001",
"10221412201",
"12102420121",
"12345654321",
"40000800004",
"1000002000001",
"1002003002001",
"1004006004001",
"1020304030201",
"1022325232201",
"1024348434201",
"1210024200121",
"1212225222121",
"1214428244121",
"1232346432321",
"1234567654321",
"4000008000004",
"4004009004004",
"100000020000001",
"100220141022001",
"102012040210201",
"102234363432201",
"121000242000121",
"121242363242121",
"123212464212321",
"123456787654321",
"400000080000004"
};

#include <iostream>

using namespace std;

//bool isPalindromes(unsigned int i, char *str)
//{
//	bool bResult = true;
//	for(unsigned int j=0; (j<(i/2) && bResult); j++)
//	{
//		if(str[j] != str[i-j-1])
//			bResult = false;
//	}
//	return bResult;
//}
//
//bool isSquare(unsigned int i)
//{
//	bool bResult = true;
//}
//
//unsigned int min(unsigned int x, unsigned int y) 
//{
//		return x<y?x:y;
//}
//
//int nbPalUntilMU(char * str)
//{
//	unsigned int Result = 0;
//	unsigned int len = strlen(str);
//	len--;
//	len--;
//	Result = len/2;
//	Result = sqrt((double) ResuZlt);
//	Result += (min(3, len/2) * (len/2));
//
//	return Result;
//}
//
//
//int nbPalUntilQ(char * str)
//{
//	unsigned int Result = 0;
//	unsigned int len = strlen(str);
//	len--;
//	len--;
//	Result = len/2;
//	Result = sqrt((double) Result);
//		cout << "res: "<< Result << endl;
//	Result += (min(3, len/2) * (len/2));
//		cout << "res: "<< Result << endl;
//
//	return Result;
//}
//
//int nbPalUntil(char * str)
//{
//	unsigned int Result = 0;
//	unsigned int len = strlen(str);
//	len--;
//	Result = len/2;
//	Result = sqrt((double) Result);
//		cout << "res: "<< Result << endl;
//	Result += (min(3, len/2) * (len/2));
//		cout << "res: "<< Result << endl;
//
//	return Result;
//}

int main(int argc, char* argv[])
{
	unsigned int T;
	char strMin[100];
	char strMax[100];

	cin >> T;
	
	unsigned int result;
	mpz_t A;
	mpz_t B;
	mpz_t tmp;

	mpz_t list[48];
	for(unsigned int i=0; i<48; i++)
	{
		mpz_init_set_str(list[i], listFairAndSquare[i], 10);
	}

	for(unsigned int i=0; i<T; i++)
	{
		cin >> strMin;
		cin >> strMax;

		mpz_init_set_str(A, strMin, 10);
		mpz_init_set_str(B, strMax, 10);

		unsigned int min;
		unsigned int max;
		
		result = 0;
		
		for(max=0; max<48; max++)
		{
			if(mpz_cmp(B, list[max]) < 0 )
			{
				break;
			}
			result++;
		}
		
		for(min=0; min<48; min++)
		{
			if(mpz_cmp(A, list[min]) <= 0 )
			{
				break;
			}
			result--;
		}

		cout << "Case #" << (i+1) << ": "<< result << endl;

		mpz_clear(A);
		mpz_clear(B);
	}

	for(unsigned int i=0; i<48; i++)
	{
		mpz_clear(list[i]);
	}

	return 0;
}

