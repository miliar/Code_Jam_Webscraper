#include <iostream>
#include<math.h>
//freopen("A_large_practice.in","r",stdin);
//freopen("m.out","w",stdout);
int main()
{
  long int t,arr[10],num,n,m,i,j,k,flag;
  std::cin>>t;
  for(i=0;i<t;i++)
 { std::cin>>num;
   k=0;n=num; m=1;
    if(num==0)
     {
          std::cout<<"case #"<<(i+1)<<": "<<"INSOMNIA \n";
          continue;
     }

   while(k!=10)
   { n= num*m;
     m++;
     do
     {  flag=0;
         for (j=0;j<k;j++)
        {
          if(arr[j] == n%10)
          {
             flag=1;
             break;
          }
        }
         if(flag ==0)
            { arr[k]= n%10;
              k++;
            }
         n/=10;
      }while(n%10!=0 || n/10!=0);
     }
    std::cout<<"case #"<<(i+1)<<": "<<num*(m-1)<<"\n";

}
return 0;
}
