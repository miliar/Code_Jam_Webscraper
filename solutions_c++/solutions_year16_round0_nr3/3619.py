

#include <cstdio>
#include "stdafx.h"
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <conio.h>

using namespace std;
typedef long long LL;
int T,N,J;
long long sum = 0, num = 0, number = 0, max = 0,i=0,prime_add=0,sqr=0;
int binary[32],binary_l[32],divi[32];
int count_J=0,j=0;


void main() {
	//FILE *fin = freopen("C-small-attempt0.in", "r", stdin);
	//assert(fin != NULL);
	FILE *fout = freopen("C-small.out", "w", stdout);
	
	
	cin >> T;
	for (int t = 1; t <= T; t++)
	{

		cin >> N >> J;
		cout << "Case #" << t << ":\n";
		num = pow(2, N - 1) + 1;
		max = pow(2, N);
		do
		{	
			number = num;
			i = 0;
			//erase
			/*for (int k = 0; k < 32; k++)
			{
				binary[k] = 0;
				divi[k] = 0;
			}*/
			//dec to bin
			while (number != 0)
			{
				binary[i++] = number % 2;
				number /= 2;
			}
			
			/*binary[0] = 1;
			binary[1] = 0;
			binary[2] = 0;
			binary[3] = 0;
			binary[4] = 1;
			binary[5] = 1;*/
			// base 2 to 10
			for (j = 2; j <= 10; j++)
			{
				i = 0;
				sum = 0;
				do
				{
					sum += binary[i] * (powl(j, i));
					i++;
				} while (i < N);
				i = 2;
				prime_add = 1; 
				sqr = (sqrtl(sum));
				while (((sum%i) != 0) && (i <= sqr))
				{
					i = i + prime_add++;
				}
				if ((i) <= (sum / 2))
				{
					divi[j] = i;
				}
				else
				{
					break;
				}

			}
			if (j==11)
			{
				
				for (int r = N; r>0; r--)
					cout << binary[r-1];
				for (int r = 2; r <= 10; r++)
					cout << "\t" << divi[r];
				cout << "\n";
				count_J++;
			}
			
			if (count_J == J)
				break;
			num += 2;
		} while (num < max);

		
	}	
		
	
	//_getch();
	exit(0);
}