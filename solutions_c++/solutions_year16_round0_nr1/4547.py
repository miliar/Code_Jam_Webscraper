#include"stdio.h"
#include "stdlib.h"

unsigned long long prog_algo_solver(unsigned int num)
{
  unsigned long long res = 0,temp_num;//insomania
  unsigned int i=1;
  int arr_digit[10]={0};// digit counter
  int all_digit_count = 10,temp=0;// digit check if all digit has been used
  if (num==0)
  return res;
  //run loop until all digit count
  while(all_digit_count!=0)
  {
    temp_num = i*num;
    res = temp_num; // save result
    while(temp_num!=0)
    {
     temp = temp_num%10;
     arr_digit[temp]++;
     if (arr_digit[temp]==1)
     all_digit_count --;
     temp_num = temp_num/10;
   }
    // increment i for next num 
    i++;
  }
// return result
return res;
}


void main_func_handler()
{
  FILE *in_fp= NULL;
  FILE *out_fp = NULL;
  int no_tc=0,loop=0;
  
  // program specific varaible read 
  unsigned int num=0;
  unsigned long long res=0;  
// intialize file pointer for input and output
  in_fp = fopen("A-large.in","r");
  out_fp = fopen("output_weird_large.txt","w"); 
  if(in_fp == NULL)
   {
       printf("\n Error no input file ");
       return;    
   }
 
 // read first line to know no of tc  
  // read no of TC
  fscanf(in_fp,"%d",&no_tc);
  
   // run loop for the no. of TC
   for(loop=1;loop<=no_tc;loop++)
   {
      fscanf(in_fp,"%u",&num);                      
      res = prog_algo_solver(num);
      printf("\n the res val is %llu",res);
      
      if (res==0)
      fprintf(out_fp,"Case #%d: %s\n",loop,"INSOMNIA"); 
      // print in file
      else 
      fprintf(out_fp,"Case #%d: %llu\n",loop,res);                         
   }
   
}


int main()
{
  main_func_handler();
  system("PAUSE");
}
