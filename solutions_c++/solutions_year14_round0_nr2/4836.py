#include <iostream>
#include <stdio.h>
#include <vector>
#include <cmath>

#define INPUT "A.in"
#define OUTPUT "A.out"

long double GCook;
long double tempototal;


void function(long double c, long double f, long double x, bool farm)
{
	
	if(farm==true)
		GCook += f;

	long double tempfinal,tempfazenda;
	
	tempfinal = x / GCook;
	tempfazenda = c / GCook;


	if(tempfinal < tempfazenda + (x/(GCook+f))){
		tempototal += tempfinal;
	}
	else{
		tempototal += (c / GCook);
		function(c,f,x,true);
	}

	

}

int main()
{

   int cases;

   freopen(INPUT,"r",stdin);
   freopen(OUTPUT,"w", stdout);


   std::cin >> cases;


	for(int i=0;i<cases;++i)
	{
	
	   GCook = 2.0;
	   tempototal = 0.0;
	   

	   long double c, f, x;

	   std::cin >> c;
	   std::cin >> f;
	   std::cin >> x;

	   function(c,f,x,false);

	   printf("Case #%d: %.7Lf\n",i+1, tempototal);



	}

   
   return 0;

}
