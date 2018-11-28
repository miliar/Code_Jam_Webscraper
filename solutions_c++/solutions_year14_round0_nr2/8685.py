#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;




ifstream in("input.txt");
ofstream of("output.txt");

 
int main()
{FILE *fd;
 fd=fopen("output.txt", "w");
 int N;
 in>>N;
double X;
 double F;
double C;
 for(int qwerty=0;qwerty<N;qwerty++)
 {
         
         
         
         
         
  double contb=2;
 
  in>>C;
  in>>F;
  in>>X;

 double tempmax=X/2;
 double conts1=tempmax;
 double conts=0;
  while(conts1<=tempmax)
  
  {tempmax=conts1;
   conts+=C/contb;
   contb+=F;
   conts1=(X/contb)+conts;
  } 

 fprintf(fd,"%s","Case #");
 fprintf(fd,"%d",qwerty+1);
 fprintf(fd,"%s",": ");
 fprintf(fd,"%.7f", tempmax);
 fprintf(fd,"%s","\n"); 
 }

}  
                 
    
 
