#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
        freopen( "input.txt", "r", stdin );
       	freopen( "output.txt", "w", stdout );

    int t;
    cin>>t;
    int cn=0;
    while(t--)
    {
              double c,f,x,t=0,co=0,ft=0,t1,t2,sum=2;
              bool val=true;
              cin>>c>>f>>x;
              while(val)
              {
                         
                         t1=x/sum;
                         t2=(c/sum)+(x/(sum+f));
                         if(t1<t2)
                         {
                                  t+=t1;
                                  val=false;
                         }
                         else
                         {
                         t+=c/sum;
                         sum+=f;
                         
                         
                         }
                                     
              }
              
              
              
              cn++;
              printf("Case #%d: %.7f\n",cn,t);
                                     
    }
}
