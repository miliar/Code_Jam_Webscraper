#define maxar 124800
#define maxver 5000
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include<stdlib.h>
#include<map>

using namespace std;



long long circulos(long long r, long long t){
  long long i=r+1;
  long long sum=0;
  long long circuloss=0;
  while(true){
    sum+=pow(i,2)-pow(i-1,2);
    if(sum>t)break;   
    circuloss++; 
    i+=2;
  }
  return circuloss;
}
	

int main () {
	long long casos =0, r,t;
	scanf("%Ld",&casos);
	for(long long caso=1;caso<=casos;caso++){
	  scanf("%Ld %Ld",&r, &t);
	  printf("Case #%Ld: %Ld", caso, circulos(r,t));
	  printf("\n");
	}
return 0;
}


	
	
	

	
