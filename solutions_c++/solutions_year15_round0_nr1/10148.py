#include <stdlib.h>
#include<stdio.h>
using namespace std;
int arr[10];
/*void func(int b,int s)
  {int i,j;

   for(i=0,j=s;i<=s;i++,j--)
   {
           arr[j]=b%10;
    b=b/10;

   }



}*/



int main()
{
   int T,fren;
   int Smax;
   int i,sum;
   char S[7];
   //int b=atoi(S);
   scanf("%d",&T);
   while(T--)
   {
       fren=0,sum=0;
       scanf("%d",&Smax);
//fflush(stdin);
   scanf("%s",&S);
   //int b=atoi(S);
   int d;
   //if(S[0]==48)
    //fren+=1;
//func(b,Smax);
//printf("%d",b);
   for(i=0;i<Smax;i++)
   {d=(int)S[i]-48;

    sum=sum+d;
   // printf("%d %d\n",sum,i+1);
    if(sum<i+1)
    {fren+=1;
    sum=sum+1;
    }
   }
   printf("%d",fren);
   }

}
