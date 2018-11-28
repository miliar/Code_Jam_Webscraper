#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <stdlib.h>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    double c,f,x,tmp,r,sm,pt,t1,t2;
    in>>t;
    for(int t11=0;t11<t;t11++)
    {
       pt=0;
       sm=0;
       in>>c>>f>>x;
       r=2;
       while(pt!=x)
       {
           tmp=x/r;
           t1=c/r;
           t2=x/(r+f);
           if((t1+t2)<tmp)
           {
              r+=f;
              sm+=t1;
           }
           else
           {
               pt=x;
               sm+=tmp;
           }
       }
        out<<fixed;
       out<<"Case #"<<t11+1<<": "<<setprecision(7)<<sm<<endl;
    }
    return 0;
}
