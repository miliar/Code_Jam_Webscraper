#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;


FILE *fin, *fout; 


void solution(char *input, char *output)
{
     unsigned long long a[100];
     int count=0;
     for(unsigned long long i=1 ; i< 10000000;i++)
	  {
	    unsigned long long  n, reverse = 0, temp;
		   temp = i;
		 
		   while( temp != 0 )
		   {
		      reverse = reverse * 10;
		      reverse = reverse + temp%10;
		      temp = temp/10;
		   }
		 
		   if (i == reverse )	
           {
                   temp = i*i;
		           reverse = 0;
        		   while( temp != 0 )
        		   {
        		      reverse = reverse * 10;
        		      reverse = reverse + temp%10;
        		      temp = temp/10;
        		   }
                  
                   if ((i*i) == reverse )	
                   {
                   // printf("Palindrome is :: %llu, count = %d , root = %llu\n", reverse, count, i);
                    a[count++] = reverse;
                   }
           } 	   
	  }
    fin = fopen(input,"r");
    fout = fopen(output,"w+");
    int T;
    fscanf(fin,"%d\n",&T);
   
    for(int k=0;k<T;k++)
    {
        unsigned long long low =0;
        unsigned long long high = 0;
        short total = 0;       
        fscanf(fin,"%llu %llu\n",&low, &high);
        for(int j=0 ; j< count ; j++)
        {
           if(a[j]> high )
              break;
           if(a[j]>= low && a[j]<= high)
           {
              //printf("Palindrome is :: %llu  \n", a[j]);
              total++;
           }
        }
       // printf("\n\n");
        fprintf(fout,"Case #%d: ", k+1);
        fprintf(fout,"%d\n", total--);
       //fprintf(fout,"%d\n", found);
    } // Exit the For loop taking inputs
    fclose(fin);
    fclose(fout);
} // Exit solution

int main ()
{
    solution("C-large-1.in", "Output.txt");
   // getchar();
    return 0;
}
