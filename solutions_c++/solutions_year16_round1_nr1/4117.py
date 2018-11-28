#include"stdio.h"
#include "stdlib.h"
#include "string.h"

void  program_algo_str(int len,char read_str[],char out_str[])
{
  int loop;int start_index =1000,end_index = 1000;
  char temp_loop[2000]={0};
  temp_loop[start_index] = read_str[0];
  for(loop=1;loop<len;loop++)
  {
    if(temp_loop[end_index]>=read_str[loop])// append in end
    {
      end_index++;
      temp_loop[end_index]=  read_str[loop];
      
    }
    else // coming string is greater
    {
       if( temp_loop[start_index]<=read_str[loop])
       {
         start_index--;
         temp_loop[start_index] = read_str[loop];
         
       }// coming string greater than last one but less than start one
       else
       {
               end_index++;
               temp_loop[end_index]=  read_str[loop];
               
       }
    }
  
  }
  
  memcpy(&out_str[0],&temp_loop[start_index],len);     

} 

void main_func_handler_string()
{
  FILE *in_fp= NULL;
  FILE *out_fp = NULL;
  int no_tc=0,loop=0;
  
  // program specific data
  char read_str[1002],out_str[1002];
  int len =0;
    
// intialize file pointer for input and output
  in_fp = fopen("A-large_string.in","r");
  out_fp = fopen("outputs_string_large.txt","w"); 
  
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
     fscanf(in_fp,"%s\n",read_str);
     len = strlen(read_str);
     program_algo_str(len,read_str,out_str);     
     fprintf(out_fp,"Case #%d: %s\n",loop,out_str);
     memset(out_str,0,1000);
                   
   }
      
   /// close input file close output file
   fclose(in_fp);
   fclose(out_fp);                           
}

int main()
{
  main_func_handler_string();
  system("PAUSE");
}
