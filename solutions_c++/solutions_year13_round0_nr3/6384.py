#include<stdio.h>
#include<conio.h>
#include<math.h>

int main()
{
    int cases,bawah,atas,iterasi,temp1,temp2,count,nilai;
    int j,bukan,absolutNO;
    int tester[1000];
    scanf("%i\n",&cases);
    for(int i=1;i<=cases;i++)
    {
            nilai=0;
            scanf("%i %i%*c",&bawah,&atas);
            for(iterasi=sqrt(bawah);iterasi<=sqrt(atas);iterasi++)
            {
                    bukan=absolutNO=0;                                  
                    count=0;
                    temp1=iterasi;                                  
                    while(temp1>0)
                    {
                                 temp2=temp1%10;
                                 tester[count]=temp2;
                                 temp1/=10;
                                 count++;
                    } 
                    for(j=0;j<count;j++)
                    {
                                 if(tester[j]!=tester[count-1-j]) bukan=1,j=count;       
                    }
                    if(bukan==0)
                    {
                                
                                 count=0;
                                 temp1=iterasi*iterasi;        
                                 while(temp1>0)
                                 {
                                         temp2=temp1%10;
                                         tester[count]=temp2;
                                         temp1/=10;
                                         count++;
                                 } 
                                 for(j=0;j<count;j++)
                                 {
                                         if(tester[j]!=tester[count-1-j]) absolutNO=1,j=count;       
                                 } 
                                 if(absolutNO==0 && bawah<=iterasi*iterasi && atas>=iterasi*iterasi)
                                 {
                                                 nilai++;
                                 }
                    }             
            }       
            printf("Case #%i: %i\n",i,nilai);
    }
}    
