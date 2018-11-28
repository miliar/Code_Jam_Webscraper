#include<bits/stdc++.h>
using namespace std;
int main()
{
   freopen("ci.txt","r",stdin);
   freopen("cou.txt","w",stdout);
   long long n=1,f,i,S,j;
   long long str;
   cout << "Case #1:\n";
   while(n<=50)
   {
       n++;
       for(j=1; j<=10; j++)
       {
           cin>> S;
           if(j==1)
           {
               cout << S<< " ";
           }
           else
           {
                 for(i=2; i*i<=S; i++)
               {
                   if(S%i==0)
                   {
                       cout << S/i << " ";
                       break;
                   }
               }
           }

       }
       cout << endl;
   }
}
