#include<stdio.h>
#include<conio.h>

int main()
{
 
 float C,F,X;
 float max_time,next_max_time,temp;
 int flag,no_test_case;
 float result[110];
 FILE *f1,*f2;
 
       f1 = fopen("E:\\B-small-attempt2.in","r");
       f2=fopen("E:\\output_cookie_clicker.txt","w");
 
 //printf("\n Input \n \n");
 if(f1!=NULL && f2!=NULL)
 {
             
   fscanf(f1,"%d",&no_test_case);
   
    for(int count=1;count<=no_test_case;count++)
    {
         
         fscanf(f1,"%f %f %f",&C,&F,&X);
 
         max_time = X/2;
         next_max_time = (C/2 + X/(2+F));
         flag=1;
 
         while(next_max_time < max_time)
         {
                             max_time = next_max_time;
                             temp = C/2;
                             for(int i=1;i<=flag;i++)
                             {
                                     temp = temp + (C/(2+(F*i)));
                             }
                             next_max_time = temp + (X/(2+(F*(flag+1))));
                             flag++;
         }
         
         result[count] = max_time;
    }
 
    
 
    for(int count=1;count<=no_test_case;count++)
    {
       fprintf(f2,"Case #%d:  %.7f \n",count,result[count]); 
    }
 
 }
 else
     printf("\n OOPS!!! FILES COULDN'T BE OPENED...");

 fclose(f1); 
 fclose(f2); 
 getch();
 return 0;   
}
