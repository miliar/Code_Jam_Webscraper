#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int T;
    scanf("%d",&T);//輸入總共幾個CASE 
    for(int t=1;t<=T;t++)
    {
        int *array;
        int n;
        scanf("%d",&n);//輸入害羞等級長度 
        array = new int [n+1];
        char str[n];
        scanf("%s",str);//輸入每個人的害羞等級 
        for(int i=0;i<=n;i++)//初始化 
        {      
           //array[i]=atoi(str);
           array[i]=int(str[i]- '0');
        }
   
        //每個人都去檢查 
        int M=0;//目前站起來的人數 
        int G=0; //還差多少人 
        for(int i=0;i<=n;i++)
        {   
           if(array[i]!=0){ 
               if(M >= i)//檢查是否有i個人站起來
               {         
                   M += array[i];  
               } 
               else{
                   G += i-M; //欠的人數 
                   M += array[i]+G;//先假裝有人站加進去 
               }
           }
        }   
        printf("Case #%d: %d\n",t,G);       
        delete [] array;
    }
    
    

    system("PAUSE");
    return 0;
}
