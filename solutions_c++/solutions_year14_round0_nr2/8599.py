#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLEN 500

#define GETNEXT(buf,index)  {if(index==-1){index++}else{bool flag = true; \
		                    while(buf[index] == ' ' || flag)\
		                    { index++; flag &= buf[index] != ' ';}}} 

#define GETNEXTI(buf,index,val)  {if(index == -1) {index++;}else{bool flag = true; \
		                         while(buf[index] == ' ' || flag)\
		                         { index++; flag &= buf[index] != ' ';}}val=atoi(&buf[index]);} 
								 
#define GETNEXTD(buf,index,val)  {if(index == -1) {index++;}else{bool flag = true; \
		                         while(buf[index] == ' ' || flag)\
		                         { index++; flag &= buf[index] != ' ';}}val=atof(&buf[index]);} 

using namespace std;
typedef unsigned int UINT;
FILE* fp;

double ProcessTestCase()
{
    char buf[MAXLEN];
	fgets(buf, MAXLEN, fp);

   /*int i = -1;
	
	float C;
	GETNEXTD(buf,i,C)

	float F;
	GETNEXTD(buf,i,F)

	float X;
	GETNEXTD(buf,i,X)*/
	
	double time = 0;
	double rate = 2;
	
	char* pEnd;
	double C = strtod (buf, &pEnd);
	double F = strtod (pEnd, &pEnd);
	double X = strtod (pEnd, NULL);
	
	do {
	    double t1 = X / rate; // time taken with current rate
	    double t2 = (C / rate) + (X / (rate + F)); // time taken buying a farm
	    if(t1 > t2){
	        time += (C / rate);
		    rate += F;
	    } else {
	        time += (X /rate);
			break;
	    }
	  }
	  while (1);
    return time;
}

int main()
{
  fp = fopen("input.txt", "r");
  char buf[MAXLEN];
  fgets(buf, MAXLEN, fp);

  int T = atoi(buf);
  cout << endl;
  for(int i=1; i<=T; i++){
    //cout << "Case #" << i << ": " << ProcessTestCase() << endl;
	printf("Case #%d: %.7f \n",i,ProcessTestCase());
  }
  fclose(fp);

  return 0;
}
