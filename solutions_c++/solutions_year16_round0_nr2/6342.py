#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("B-large.in");
    ofstream out("salida.out");
    int t,i,tam,j,k,mov;
    string s;
    in>>t;
    for(i=1;i<=t;i++)
    {
        mov=0;
        in>>s;
        tam=s.length();
    for(j=0;j<tam;j++)
    {
      if(s[j]=='-')
      {
         k=j;
         while((s[k+1]=='-')&&(k<tam))
         {
             k++;
         }
         if(j==0)
         {
             mov=1;
         }
         else
         {
             mov+=2;
         }
         j=k;
      }
    }
out<<"Case #"<<i<<": "<<mov<<endl;
    }


    in.close();
    out.close();
    return 0;
}
