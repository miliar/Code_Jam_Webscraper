#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;
int digit[10]={0};
int allvisit()
{
    for(int i=0;i<10;i++)
    {
        if(digit[i]==0)
            return 0;
    }
    return 1;
}

int main()
{
    FILE *f=fopen("C:\\Users\\Vishal\\Desktop\\output.txt","w");
   int t,tcp=0;
   cin>>t;
   while(t--)
   {
       int n,x,k;
       cin>>n;
       if(n==0)
        fprintf(f,"Case #%d: INSOMNIA\n",++tcp);
       else
       {
           x=n;
           k=1;
           memset(digit,0, 10*sizeof(int));
           while(!allvisit())
            {
           while(x!=0)
           {
               digit[x%10]=1;
               x=x/10;
           }
           x=++k*n;
            }
            fprintf(f,"Case #%d: %d\n",++tcp,(k-1)*n);
       }
   }
   return 0;
}
