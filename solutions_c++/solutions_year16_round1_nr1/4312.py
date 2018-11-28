#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
 int t,i,j;
 char st,lt;
 string a,b;
 freopen( "A-large(1).in", "r", stdin );
 freopen( "outputr2q1lg.out", "w", stdout );

 cin>>t;

 i=0;
 while(i<t)
 {
     cin>>a;
     b=a[0];
     st=a[0];
     lt=a[0];
     for(j=1;a[j]!='\0';j++)
     {
         if(st<=a[j])
          {
            b=a[j]+b;
            st=a[j];
         }
         else
         {
              b=b+a[j];
              lt=a[j];
         }

     }
 cout<<"Case #"<<i+1<<": "<<b<<"\n";

i++;
}
}
