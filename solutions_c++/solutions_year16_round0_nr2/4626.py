#include"stdio.h"
#include "stdlib.h"
#include "string.h"

void main_func_handler()
{
  FILE *in_fp= NULL;
  FILE *out_fp = NULL;
  int no_tc=0,loop=0;
  
  // program specific varaible read 
   char read_data[103]={0};
   int char_len = 0,count_step=0,temp_loop1=0;   
// intialize file pointer for input and output
  in_fp = fopen("B-large.in","r");
  out_fp = fopen("output_pancake_attempt_large.txt","w"); 
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
      fgets(read_data,103,in_fp); 
      char_len = strlen(read_data);
      //if(read_data[char_len-1]=='\n')
      //read_data[char_len-1]='\0';// remove new line 
      for(temp_loop1=1;temp_loop1<char_len;temp_loop1++)
      {
        // logic to check for same
        if((read_data[temp_loop1-1]!=read_data[temp_loop1])&&
           ((read_data[temp_loop1]== '+')||(read_data[temp_loop1]== '-')))
        {
           // different on need operation increase count
           count_step++;
        
        }                                                  
      
      }
      
      if(read_data[temp_loop1-1]=='\n')
      temp_loop1 = temp_loop1-2;
      else 
      temp_loop1 = temp_loop1 -1;
      
      if(read_data[temp_loop1]== '-')
      count_step++;
      
      fprintf(out_fp,"Case #%d: %d\n",loop,count_step);  
      //reset data
      count_step = 0;
      memset(read_data,103,sizeof(char));
   }
   fclose(in_fp);
   fclose(out_fp);
   
}   


int main()
{
  main_func_handler();
  system("PAUSE");
}
