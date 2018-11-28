#include<iostream>
#include<cstdio>
using namespace std;
int cases,r,t;

int main()
{      scanf("%d",&cases);
       int m=1;
       int k=0;
       while(cases--)
       {    scanf("%d",&r);
            scanf("%d",&t);
            k=0;
            
            int p=2*r+1;
            while(t>=p)
            {                   
                 k++;
                 t-=p;
                 p+=4;
            }
            printf("Case #%d: %d\n",m,k);
            m++;
       }
      // system("pause");
}                   
      
