#include <iostream>
#include<fstream>
#include<string>
using namespace std;

int maxShy;
int main()
{
    ifstream f("in");
    ofstream g("out");
   int t;
   f>>t;

   for(int i=1;i<=t;i++)
   {
       f>>maxShy;
       string s;
       f>>s;
       int tOva=0;
       int reqF=0;
       for(int j=0;j<=maxShy;j++)
       {
           //cout<<tOva<<" "<<reqF<<" \n";
           if(tOva<j)
           {
                reqF+=j-tOva;
                tOva+=j-tOva;
           }
           tOva+=(int)(s[j]-48);
       }
       g<<"Case #"<<i<<": "<<reqF<<"\n";
   }


    return 0;
}
