#include<iostream>
#include<stdio.h>
#include<string.h> 
long long int sum,i,T,x,c;
char a[10000];
using namespace std;
main()
{
      FILE *fp;
      fp=fopen("out4.txt","w");
      cin>>T;
      c=T;
      while(T--)
      {
                cin>>a;
                x=strlen(a);
                i=(x-1);
                if(a[i]=='-')
                sum=1;
                if(a[i]=='+')
                sum=0;
                for(i;i>0;i--)
                {
                                    if(a[i]!=a[i-1])
                                    sum++;
                }                                    
                fprintf(fp,"Case #%d: ",(c-T));
                fprintf(fp,"%d\n",sum);
      }
             return 0;
}
