#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{

    freopen("output.txt","w",stdout);
     freopen("input.txt","r",stdin);

   int a[10];


   int n;
   while(cin>>n)
   {



    for(int i=1;i<=n;i++)
       {
            for(int i=0;i<=9;i++)
    a[i]=0;


            int k=1;
           int m,aa;
           cin>>m;
           aa=m;

           if(m==0)
           {
               cout<<"Case #"<<i<<": INSOMNIA\n";
               continue;
           }
           int count=0;
           while(1)
           {
               int number=aa;

               while(aa)
               {
                int pos=aa%10;
               aa=aa/10;
               if(a[pos]==0)
               {
                    a[pos]=1;
               count++;
               }
               }

               if(count==10)
               {
                   cout<<"Case #"<<i<<": "<<number<<endl;
                   break;

               }
               k++;
               aa=m*k;

           }
       }
   }

    return 0;
}
