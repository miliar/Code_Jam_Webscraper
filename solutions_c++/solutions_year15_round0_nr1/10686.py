#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  int t,k,smax,c,d,b,i;
  char a;
  ifstream input;
  input.open ("A-small-attempt1.in" , ios::in);
  ofstream output;
  output.open ("output2.in",ios::out);
  if (input.is_open())
  {
      input>>t;
      for(k=1;k<=t;k++)
      {
          d=0;
          c=0;
          input>>smax;
        for(i=0;i<=smax;i++)
            {
                input>>a;
                b=a-48;
                if(i!=0 && c<i && b!=0)
                {
                    d=d+i-c;
                    c=c+d+b;
                }
                else if(i==0)
                c+=b;
                else
                c+=b;
            }
        output<<"Case #"<<k<<": "<<d<<endl;
      }
  }

  else cout << "Unable to open file";
  input.close();
  output.close();
  return 0;
}
