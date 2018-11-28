#include <iostream>
#include<stdio.h>
using namespace std;

int check(int base[], int r)
{
    int cont=0;
    for(int i=0; i<10; i++)
    {
        if(base[i]>=1)
        {
            cont++;
        }

    }
    if(cont==10)
        r=1;
    else
        r=0;

    return r;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("solution-large.out", "w", stdout);
   int t, n, aux, cont=1, exp, res, timebomb, dig, num;
   int r;
   cin>>t;

   if(t>=1 && t<=100)
   {
       while(t--)//cada caso
       {
          cin>>n;
          exp=1;
          timebomb=1000000;
          int base[10]={0,0,0,0,0,0,0,0,0,0};
          r=0;
          if(n>=0 && n<=1000000)
          {

               while( timebomb!=0)
               {
                    num=exp*n;

                    aux=num;
                   while(aux>0)
                   {
                       dig=aux%10;
                       base[dig]++;
                       r=check(base, r);
                       aux=aux/10;
                   }
                   if(r==1)
                   {
                       res=num;
                       break;
                   }

                    exp++;
                    timebomb--;
               }

          }
          if(r==1)
            cout<<"Case #"<<cont<<": "<<res<<endl;
          else
            cout<<"Case #"<<cont<<": "<<"INSOMNIA"<<endl;

          cont++;

       }
   }

    fclose(stdout);
    return 0;

}
