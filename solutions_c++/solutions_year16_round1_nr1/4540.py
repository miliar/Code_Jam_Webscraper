#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("A-small-attempt0 (1).in");
    ofstream out("salidapa.out");
    string s,h;
    int i,j,k,t,caso;





in>>t;
for(caso=1;caso<=t;caso++)
  {
s="";
h="";
fflush(stdin);
    in>>s;

    k=s.length();




    for(i=0;i<k;i++)
    {
      if(i==0)
      {
          h[0]=s[0];
      }
      else
      {
          if(s[i]>=h[0])
          {
             for(j=i;j>0;j--)
             {
                 h[j]=h[j-1];
             }
             h[0]=s[i];

          }
          else
          {
              h[i]=s[i];
          }
      }
    }
    out<< "Case #"<<caso<<": ";
    for(j=0;j<k;j++)
    {
        out<<h[j];
    }
    out<<endl;
}

    in.close();
    out.close();
    return 0;
}
