#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <fstream>

using namespace std;

/*

Introduction

Cookie Clicker is a Javascript game by Orteil, where players click on a picture of a giant cookie. Clicking on the giant cookie gives them cookies. They can spend those cookies to buy buildings. Those buildings help them get even more cookies. Like this problem, the game is very cookie-focused. This problem has a similar idea, but it does not assume you have played Cookie Clicker. Please don't go play it now: it might be a long time before you come back.
Problem

In this problem, you start with 0 cookies. You gain cookies at a rate of 2 cookies per second, by clicking on a giant cookie. Any time you have at least C cookies, you can buy a cookie farm. Every time you buy a cookie farm, it costs you C cookies and gives you an extra F cookies per second.

Once you have X cookies that you haven't spent on farms, you win! Figure out how long it will take you to win if you use the best possible strategy.
Example

Suppose C=500.0, F=4.0 and X=2000.0. Here's how the best possible strategy plays out:

    You start with 0 cookies, but producing 2 cookies per second.
    After 250 seconds, you will have C=500 cookies and can buy a farm that produces F=4 cookies per second.
    After buying the farm, you have 0 cookies, and your total cookie production is 6 cookies per second.
    The next farm will cost 500 cookies, which you can buy after about 83.3333333 seconds.
    After buying your second farm, you have 0 cookies, and your total cookie production is 10 cookies per second.
    Another farm will cost 500 cookies, while you can buy after 50 seconds.
    After buying your third farm, you have 0 cookies, and your total cookie production is 14 cookies per second.
    Another farm would cost 500 cookies, but it actually makes sense not to buy it: instead you can just wait until you have X=2000 cookies, which takes about 142.8571429 seconds.

Total time: 250 + 83.3333333 + 50 + 142.8571429 = 526.1904762 seconds.

Notice that you get cookies continuously: so 0.1 seconds after the game starts you'll have 0.2 cookies, and π seconds after the game starts you'll have 2π cookies.
Input

The first line of the input gives the number of test cases, T. T lines follow. Each line contains three space-separated real-valued numbers: C, F and X, whose meanings are described earlier in the problem statement.

C, F and X will each consist of at least 1 digit followed by 1 decimal point followed by from 1 to 5 digits. There will be no leading zeroes.
Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of seconds it takes before you can have X delicious cookies.

We recommend outputting y to 7 decimal places, but it is not required. y will be considered correct if it is close enough to the correct number: within an absolute or relative error of 10-6. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.
Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ C ≤ 500.
1 ≤ F ≤ 4.
1 ≤ X ≤ 2000.
Large dataset

1 ≤ C ≤ 10000.
1 ≤ F ≤ 100.
1 ≤ X ≤ 100000.
Sample

Input
  	
Output
 

4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

	

Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762



*/


long double cookiesPerSecond;
long double farmPrice;
long double farmExtraCookies;
long double cookiesToWin;

long double myCookies = 0.0;

int nroCasos2;

FILE *escribir2 = fopen("D:\\Google Code Jam 2014\\Problema 2\\output.txt", "w");

long double calcularTiempoComprando()
{
	long double tiempoParaComprar = farmPrice/cookiesPerSecond;
	long double tiempoEsperandoTrasComprar = cookiesToWin/(cookiesPerSecond+farmExtraCookies);

	return tiempoParaComprar + tiempoEsperandoTrasComprar;
}

long double getTiempoParaComprar()
{
	return farmPrice/cookiesPerSecond;
}

long double calcularTiempoEsperando()
{
	return cookiesToWin/cookiesPerSecond;
}

long double jugar()
{
	long double tiempoTotal = 0.0;

	while (myCookies < cookiesToWin)
	{
		long double tiempoComprando = calcularTiempoComprando();
		long double tiempoEsperando = calcularTiempoEsperando();

		if (tiempoComprando < tiempoEsperando)
		{
			long double tcompra = getTiempoParaComprar();
			
			tiempoTotal += tcompra;
			myCookies = cookiesPerSecond * tcompra;

			cookiesPerSecond += farmExtraCookies;
		}
		else
		{
			tiempoTotal += tiempoEsperando;
			myCookies += cookiesPerSecond * tiempoEsperando;
		}
		
	}
	printf("Tiempo total: %.7f\n", tiempoTotal);
	//system("PAUSE");

	return tiempoTotal;
}

void leer()
{
	FILE *archivo = fopen("D:\\Google Code Jam 2014\\Problema 2\\B-large.in", "r");
	
	if (archivo)
	{
		fscanf(archivo, "%d", &nroCasos2);

		for (int i = 0; i < nroCasos2; i++)
		{
			fscanf(archivo, "%Lf", &farmPrice);
			fscanf(archivo, "%Lf", &farmExtraCookies);
			fscanf(archivo, "%Lf", &cookiesToWin);
			cookiesPerSecond = 2.0;
			myCookies = 0.0;

			//printf("Precio: %.7f\nExtraCookiesPerFarm: %.7f\nWin: %.7f\n\n\n\n", farmPrice, farmExtraCookies, cookiesToWin);

			fprintf(escribir2, "Case #%d: %.7f\n", (i+1), jugar());
		}
	}

	fclose(archivo);
}

void main()
{
	leer();
	fclose(escribir2);
	//system("pause");
}