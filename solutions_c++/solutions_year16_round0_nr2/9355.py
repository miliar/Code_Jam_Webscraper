#include<stdio.h>
#include<string.h>
 
  int main(void)
 {
 	
 	  int m,n,test,flag,length;
 	  char pancakes[101];
 	   scanf("%d",&test);
 	   for(m=0;m<test;m++)
 	      {
             scanf("%s",&pancakes);
             length= strlen(pancakes);
             flag=0;
             for(n=0;n<length-1;n++)
               {
               	     if(pancakes[n]!=pancakes[n+1])
               	       flag++;
                      
               	    
			   }
			   	     if(pancakes[n]== '-')
			   	     flag++;
			   	     
						  printf("Case #%d: %d\n",m+1,flag);               	    
			  	   	 
		}
 	
 	
 	return 0;
 }
