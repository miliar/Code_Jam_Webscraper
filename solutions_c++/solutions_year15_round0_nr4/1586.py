#include <iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;

int x,r,c;

bool fits(int h,int w,int r, int c)
{
    if(h<w)
    {
        swap(h,w);
    }
    if(r<c)
    {
        swap(r,c);
    }
    return h<=r && w<=c;
}
int main()
{
    ifstream f("in");
    ofstream g("out");
   int t;
   f>>t;


   for(int test=1;test<=t;test++)
   {
       f>>x>>r>>c;

       bool ok=true;
       if(x==4 && r==2 && c==4)
        ok=false;
       if(x==4 && r==4 && c==2)
        ok=false;

       for(int h=1;h<=x && ok;h++)
       {
            int w=x+1-h;
           if(x>=7 || !fits(h,w,r,c) || (r+c<x) || ((r*c)%x)!=0)
           {

               ok=false;
           }
       }
       g<<"Case #"<<test<<": "<<(ok?"GABRIEL":"RICHARD")<<"\n";
   }


    return 0;
}
