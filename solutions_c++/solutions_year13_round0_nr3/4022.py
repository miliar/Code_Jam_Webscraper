#include <stdio.h>
#include <stdint.h>
#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;

int main() {

uint64_t i=0;
uint64_t temp=0;
uint64_t r=0;
uint64_t tempo=0;


uint64_t A=1;
uint64_t B=10000000;

ifstream myFile;
myFile.open("input.txt");

int T=0;
myFile >> T;
int count=0;
int main_count=0;

while (count != T){
    main_count=0;
    myFile >> A;
    myFile >> B;
    //printf(" A: %lu, B: %lu \n", A, B);
for(i=sqrt(A); i <= sqrt(B) ;i++)
{
   r=0;
   temp=i;
   while(temp>0)
   {
     r=r*10;
     r=r+temp%10;
     temp=temp/10;
   }
   if(i==r)
   {
      r=0;
      temp=tempo=i*i;
      if(( temp < A ) || (temp > B)) continue;
      while(temp>0)
      {
        r=r*10;
        r=r+temp%10;
        temp=temp/10;
      }
      if(tempo == r) 
       //printf("Case #: %lu-->%lu \n", i, tempo);
       //printf("Case #%d: %lu \n",count, tempo);
       main_count++;
   }
}
 printf("Case #%d: %d\n",count+1, main_count);
 count++;
}
return 0;
}
