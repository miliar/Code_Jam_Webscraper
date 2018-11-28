#include <iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;

int d,p[1002];


int main()
{
    ifstream f("in");
    ofstream g("out");
   int t;
   f>>t;


   for(int test=1;test<=t;test++)
   {
       f>>d;
       int no_consumate=0;
       int no_magic=0;
        int maxi=0;
       for(int i=0;i<d;i++)
       {
           f>>p[i];
            if(maxi<p[i])
                maxi=p[i];
       }

       int bestest=10000;
       for(int no_c=1;no_c<=maxi;no_c++)
       {

            no_magic=0;
           for(int i=0;i<d;i++)
           {

               int no_w=p[i]/no_c;
               if(p[i]%no_c==0)
               {

                   no_w--;
               }
               no_magic+=no_w;

           }
           if(bestest>no_magic+no_c)
           {
                bestest=no_magic+no_c;
           }
       }
       g<<"Case #"<<test<<": "<<bestest<<"\n";
   }


    return 0;
}
