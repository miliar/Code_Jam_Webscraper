#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int k,l;
int n,t,i,c,b[1000];
char a[1000];
main (){
       scanf("%d",&k);
    for(l=1;l<=k;l++){
        t=0;
gets(a);
       for(n=strlen(a)-1;n>=0;n--){
          if(a[n]=='+')
               i=0;
               else
               i=1;

               i+=t;
               if(i%2==1)
           t++;
                   }
 b[l]=t;
    }
    for(l=1;l<=k;l++)
        cout<<"Case #"<<l<<": "<<b[l]<<endl;
}
