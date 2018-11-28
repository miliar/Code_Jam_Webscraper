#include"stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"


int is_prime(unsigned long long num)
{
    unsigned long long k = 1, a = 0, b = 0;
    unsigned long long sr;
    switch((int)num)
        {
        case 1: return 0;
        case 2: return 1;
        case 3: return 1;
        case 4: return 0;
        case 5: return 1;
        case 6: return 0;
        case 7: return 1;
    }

    if (num % 2 == 0) return 0;
    if (num % 3 == 0) return 0;
    sr = (long) sqrt(num);
    while (b < sr) {
        a = (6 * k) - 1;
        b = (6 * k) + 1;
        if (num % a == 0)
            return 0;
        if (num % b == 0)
            return 0;
        k += 1;
    }
    return 1;
}

unsigned long long int find_divisor(unsigned long long num)
{
  unsigned long long int i=0;
  for (i = 2; i < num; i++)
  { 
//if (num % i == 0&&i*i!=num)
  //  cout << i << num/i << endl;
   if(num % i == 0)
   break;
  }
  return i;
}

int code_to_convert_and_check(unsigned long long int num,unsigned long long int res[9],char bi_array[32])
{
  unsigned long long int temp_num,loop_mult=0;
  int i=0,j=0,result = 1,loop=0;// 0 result means no conversion found
  while(num>0) 
  { 
    bi_array[i]= num%2;     
    num = num/2;
    i++; 
  }
 // base 2 and 10 inclusive
 
 for (loop = 2; loop <=10;loop++)
 {
   temp_num = 0;// reset for every use
   loop_mult = loop;
   if(bi_array[0]==1)
   temp_num +=1;
   
   for(j=1;j<i;j++)
   {
     temp_num += bi_array[j] *loop_mult; // onversion to decimal
     loop_mult *=loop;
   }
   
   if(is_prime(temp_num)== 0)// if not prime don't store deivisor and break
   {
     res[loop-2]= find_divisor(temp_num);
   }
   else
   {
     result = 0;
     break;
   } 
 }
 
 return result;
}


void main_func_handler()
{
  FILE *in_fp= NULL;
  FILE *out_fp = NULL;
  int no_tc=0,loop=0;
  
  // program specific varaible read 
   int val_n=0,val_j=0,j_count=0,print_count=0; 
   unsigned long long pnum,result[9],start_loop=0; 
   char b_arr[35]={0};
// intialize file pointer for input and output
  in_fp = fopen("C-small-attempt0.in","r");
  out_fp = fopen("output_jam_coint_attempt_0.txt","w"); 
  if(in_fp == NULL)
   {
       printf("\n Error no input file ");
       return;    
   }
 
 // read first line to know no of tc  
  // read no of TC
  fscanf(in_fp,"%d\n",&no_tc);
  
   // run loop for the no. of TC
   for(loop=1;loop<=no_tc;loop++)
   {
      fscanf(in_fp,"%d %d\n",&val_n,&val_j); 
      fprintf(out_fp,"Case #%d:\n",loop);
      j_count =1;// reset
      pnum = (long long int)pow(2,(val_n)); 
      for(start_loop = pnum/2;(start_loop<pnum)&&(j_count<=val_j);start_loop++)
     { 
       memset(b_arr,0,35*sizeof(char));
       if((start_loop%2)==0)
        ;
       else 
       {
         if (code_to_convert_and_check(start_loop,result,b_arr))
         {
           j_count++;
           
           for(print_count=0;print_count<val_n;print_count++)
           fprintf(out_fp,"%d",b_arr[val_n-1-print_count]);

           // write to file
           fprintf(out_fp,"  %llu %llu %llu %llu %llu %llu %llu %llu %llu \n",
                  result[0],result[1],result[2],result[3],result[4],result[5],
                  result[6],result[7],result[8]);
           
         }
       }
     }
                           
   }
   
   fclose(in_fp);
   fclose(out_fp);
   
}

int main()
{
  main_func_handler();
  system("PAUSE");
}
