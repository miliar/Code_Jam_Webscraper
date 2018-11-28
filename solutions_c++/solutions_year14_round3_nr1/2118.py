#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("A-small-attempt4.in");
    ofstream out("sal.out");
    int64_t p,q,t,i,r,dos,d[42];
    char chi;
    d[0]=1;
    for(i=1;i<=41;i++)
    {
        d[i]=d[i-1]*2;
    }
    in>>t;
    for(i=1;i<=t;i++)
    {
        dos=0;
    in>>p>>chi>>q;

    while(q%2==0)
    {
        dos=dos+1;
        q=q/2;
    }
    if(p%q==0)
    {
     p=p/q;
     if(p>d[dos-1])
     {
         r=1;
     }
     else
     {
         r=0;
         while(p>d[r+1])
         {
             r++;
         }
  r=dos-r;

     }
        out<<"Case #"<<i<<": "<<r<<endl;
    }
    else
    {
        out<<"Case #"<<i<<": "<<"impossible"<<endl;
    }


    }
    in.close();
    out.close();
    return 0;
}
