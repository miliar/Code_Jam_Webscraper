#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>

/*


Problem

Little John likes palindromes, and thinks them to be fair (which is a fancy word for nice). A palindrome is just an integer that 
reads the same backwards and forwards - so 6, 11 and 121 are all palindromes, while 10, 12, 223 and 2244 are not (even though 
010=10, we don't consider leading zeroes when determining whether a number is a palindrome).

He recently became interested in squares as well, and formed the definition of a fair and square number - it is a number that is 
a palindrome and the square of a palindrome at the same time. For instance, 1, 9 and 121 are fair and square (being palindromes 
and squares, respectively, of 1, 3 and 11), while 16, 22 and 676 are not fair and square: 16 is not a palindrome, 22 is not a 
square, and while 676 is a palindrome and a square number, it is the square of 26, which is not a palindrome.

Now he wants to search for bigger fair and square numbers. Your task is, given an interval Little John is searching through, 
to tell him how many fair and square numbers are there in the interval, so he knows when he has found them all.
Solving this problem

Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has 1 Small input and 2 Large inputs. 
Once you have solved the Small input, you will be able to download any of the two Large inputs. As usual, you will be able to 
retry the Small input (with a time penalty), while you will get only one chance at each of the Large inputs.
Input

The first line of the input gives the number of test cases, T. T lines follow. Each line contains two integers, A and B - 
the endpoints of the interval Little John is looking at.
Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number 
of fair and square numbers greater or equal to A and smaller or equal than B.
Limits
Small dataset

1 ≤ T ≤ 100.
1 ≤ A ≤ B ≤ 1000.
First large dataset

1 ≤ T ≤ 10000.
1 ≤ A ≤ B ≤ 10^14.
Second large dataset

1 ≤ T ≤ 1000.
1 ≤ A ≤ B ≤ 10^100.
Sample

Input

Output

3
1 4
10 120
100 1000
Case #1: 2
Case #2: 0
Case #3: 2


*/


using namespace std;



int rango[2];

FILE *escribir = fopen("C:\\Proyecto Program 2\\output.txt", "w");


int elevar(int exp)
{
	int resul = 1;
	if (exp == 0)
		return 1;

	for (int i = 1; i <= exp; i++)
	{
		resul *= 10;
	}
	return resul;
}


int getPotencias(int num)
{
	int aux = num;
	int pots = 0;

	while (aux > 9)
	{
		aux = aux / 10;
		pots++;
	}
	return pots;
}


int palindromear(int num)
{
	int numPalindromo = 0;
	int desc = num;
	int tumama = num;
	int pot = getPotencias(num);
	//printf("%d", pot);

	/*
	1-----
	tumama = 

	*/

	while (desc != 0)
	{		
		tumama = desc % 10;
		numPalindromo += (elevar(pot)*tumama);
		pot--;
		desc = desc / 10;
	} 
	return numPalindromo;
}

bool estaLleno()
{
	if (rango[0] && rango[1])
		return true;
	return false;
}

void introducir(int x)
{
	if (x >= 0)
	{
		if (!rango[0])
			rango[0] = x;
		else if (!rango[1])
			rango[1] = x;
	}
}

void vaciar()
{
	rango[0] = NULL;
	rango[1] = NULL;
}

void buscarPalindromos(int caso)
{
	int encontrados = 0;

	//printf("En [%d-%d] existen: ", rango[0], rango[1]);
	for (int i = rango[0]; i <= rango[1]; i++)
	{
		/*
		-- Chequear si EL es palindromo
		-- Chequear si es cuadrado
		-- Chequear si su raiz es palindromo
		*/
		if ( (i == palindromear(i)) /* Chequear si EL es palindromo */
			&& (sqrt(i)*sqrt(i) == i) /* Chequear si es cuadrado */
			&& (sqrt(i) == palindromear(sqrt(i)))) /* Chequear si su raiz es palindromo */
		{
			//printf("%d, ", i);
			encontrados++;
		}
	}
	//printf(" que son JUSTOS Y PALINDROMOS.\n");
	fprintf(escribir, "Case #%d: %d\n", caso, encontrados);

	vaciar();
}

void leerInfo()
{
	FILE *archivo;
	archivo = fopen("C:\\Proyecto Program 2\\Test.txt", "r");

	int numDeCasos;
	int num;

	if (archivo)
	{
		fscanf(archivo, "%d", &numDeCasos);
		for (int i = 1; i <= numDeCasos; i++)
		{
			while (!estaLleno())
			{
				fscanf(archivo, "%d", &num);
				introducir(num);
			}
			buscarPalindromos(i);
		}
	}
	fclose(archivo);
}


void main()
{
	leerInfo();
	fclose(escribir);
}
