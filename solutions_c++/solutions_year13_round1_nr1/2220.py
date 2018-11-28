#include <stdio.h>
#include <stdint.h>
#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;

int main() {

uint64_t i=0;
uint64_t r=1;
uint64_t t=1;

ifstream myFile;
myFile.open("input.txt");

int T=0;
myFile >> T;
printf("T is %d \n", T);
int count=0;

while (count != T){
    myFile >> r;
    myFile >> t;
    //printf(" r: %lu, t: %lu \n", r, t);
for(i=0;  ;i++)
{
   int64_t eq= 2*i*i + i*(2*r-1) -t;
   //printf("eq is %ld \n",eq);
   if(eq > 0) break;
}
 if(i == 0) i=0;
 else i=i-1;

 printf("Case #%d: %lu\n",count+1, i);
 count++;
}
return 0;
}
