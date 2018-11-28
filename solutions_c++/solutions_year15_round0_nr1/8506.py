#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;



int main( void) {
        int cases = 0, casen = 0 ,s = 0, i =0, k, result = 0;
        FILE *fin, *fout;
		int suma = 0;
		
		
       fin = freopen("in.in" , "r" , stdin);
       fout = freopen("out.out" , "w" , stdout);

		
       scanf("%d" , &cases);
       for (casen = 1; casen <= cases; casen++) {

		   fprintf(fout, "Case #%d: ", casen);
		   result = suma = 0;
		   scanf("%d" , &s);
		   for (i = 0; i <= s; i++) {
			  scanf("%1d" , &k);
			  if(suma >= i)
				 suma += k;
			  else {
				  result += i - suma;
				  suma += i - suma + k;
			  }
		   }
		   fprintf(fout, "%d\n", result);
       }

	
	

		

        return 0;
}
