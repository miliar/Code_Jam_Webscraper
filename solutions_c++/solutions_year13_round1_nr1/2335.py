#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;



int main()
{
	FILE * fin;
    FILE * fout;


	fin=fopen("A-small.in","r");
	fout=fopen("A-small.out", "w");

	
    unsigned long long r = 0;
    unsigned long long  t = 0;
    long double r1 = 0;
    long double t1 = 0;
    
    long double D = 0;
    long double sqD = 0;
    long double x = 0;
    double sol = 0;
    
	int iter=0;

	printf("%d", sizeof(long long));
	fscanf(fin,"%d\n", &iter);
	
	printf("%d\n", iter);

	
	for(int j=0;j<iter;j++) {
            
      fscanf(fin, "%llu %llu\n", &r, &t);
      //printf("%llu %llu\n", r, t);
      
      long long sum = 0;
      unsigned long long i=0;
      for (; ;i++)
      {
          sum += 2*r+1;
          r +=2;
          
          if(sum>t)
          break;
          
          
      }
      
     //printf("Sol %llu\n", i);
 
     	    
	 fprintf(fout,"Case #%d: %llu\n", j+1, i);
	 
	}

    system("PAUSE");
	fclose(fin);
	fclose(fout);

	return 0;
}

