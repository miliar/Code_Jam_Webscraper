/* 

Google Code Jam 2014 
Problem B. Cookie Clicker Alpha

Autor: Jhonatan Ríchard Raphael
University: UNICAMP
Country: Brazil 

Solution: Simulation until to be worth buying. There are some cuts for optimization.
Time Complexity: ?
*/


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

#include <iostream>
#include <algorithm>

using namespace std;

/*

		- fazer uns cortes no começo do alg

*/


int main()
{
	int t,a;
	assert(scanf("%d",&t));

//-----------------------------------------------------------------------------------------

	double c,f,x;
	double time,rate,wait,buy;

	for(a=1;a<=t;a++)
	{
		assert(scanf("%lf %lf %lf",&c,&f,&x));
	
		time = 0;
		rate = 2.0;
		wait = time + x/rate;
		buy = time + (c/rate) + (x/(rate+f));

		while (buy < wait)	// enquanto valer a pena comprar do que esperar
		{
			time += c/rate;		//adiciona o tempo até comprar
			rate += f; 			// atualiza o novo rate

			wait = time + x/rate;					// calcula o novo tempo se apenas esperar com o rate atual
			buy = time + c/rate + (x/(rate+f));		// calcula o novo tempo de espera com uma fazenda nova
		}
		printf("Case #%d: %.7lf\n",a,wait);
	}
	return 0;
}
