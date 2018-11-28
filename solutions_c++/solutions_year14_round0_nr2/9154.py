#include <fstream>
#include <iostream>
#include <stdio.h> 
#include <stdlib.h>
using namespace std;

int main ()
{
   ifstream infile; 
   infile.open("inputCookieClicker.txt"); 
   
   FILE * pFile;
   pFile = fopen ("outputCookieClickerAlpha.txt","w");
   
   int cases;
   infile >> cases;
   
   double C, F, X;
      
   for(int i=0; i<cases;i++){
   	   infile >> C >> F >> X;
   	   
	   double production = 2;
       int farms = 0;
       double actualCookies = 0;
       double seconsTotProduction = 0;   
	   double sec = seconsTotProduction + (X/production);  
	   double beforeSecProd = (seconsTotProduction + (X/production)) +1; 
	   
	   while (beforeSecProd > sec){
			//Producing cookies to buy a farm   
	        seconsTotProduction = seconsTotProduction + (C/production);
	        actualCookies = actualCookies + C;
				
		    //buying a farm if actualCookies = C (farm cost)
		    if(actualCookies >= C){
		      	actualCookies = actualCookies - C;
		        farms ++;
		        production = production + F;					       
		    }
		    beforeSecProd = sec;
	        sec = seconsTotProduction + (X/production);
       }
	   fprintf(pFile,"%s%d%s %.7f\n", "Case #",i+1,": ",beforeSecProd);
   }   	
	
   // closing the opened file.
   infile.close();  
   
   fclose(pFile); 
   
   system("PAUSE");
   
   return 0;
   cin.get();
}
