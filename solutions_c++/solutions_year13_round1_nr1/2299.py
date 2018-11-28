#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;


FILE *fin, *fout; 


 long calc( long r,  long t)
{
    /*double c= (4*r^2) - (4*r)+1 + (8*7/22);
    c= sqrt(c);
    c= c+1- (2*r);
    c=c/2;*/
    int c =0;
    double l = t;
    long i=0;
    //printf("\nr= %ld and t= %ld \n", r ,t );
    
    //printf ("\n");
    i =r;
    while(l>=0)
    {
     l= l-((1.0 + (2*i)));
     //printf ("\n%f" ,l);
     i+=2;
    }
    i-=2;
        return ((i-r)/2);
    }


void solution(char *input, char *output)
{
    fin = fopen(input,"r");
    fout = fopen(output,"w+");
    long r=0;
    long t=0;
    int cases=0;
    fscanf(fin,"%d\n",&cases);
   
    
    
    for(int k=0;k<cases;k++)
    {
        fscanf(fin,"%ld",&r);
        fscanf(fin,"%ld",&t);
        long min =  calc(r,t);
        fprintf(fout,"Case #%d: %ld\n",k+1,min);
     
              
    } // Exit the For loop taking inputs
    fclose(fin);
    fclose(fout);
} // Exit solution

int main ()
{
    //solution("Input.txt", "Output.txt");
   // getchar();
   solution("A-small-attempt1.in","Output.txt");
   //getchar();
    return 0;
}
