#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <fstream>
#define F(x) cout<< #x " = "<<x<<endl;
#define A(x) static_cast<int>(ceil(sqrt(x)))
#define B(x) static_cast<int>(floor(sqrt(x)))

using namespace std;

inline bool isPal(long long a)
{

      stringstream ss;
      ss << a;
      string str = ss.str();
      long long p = str.size();
      for(long long i = 0;i<p/2;i++)
            if(str[i]!=str[p-i-1])
                  return 0;
      //F(a);
      return 1;
}

inline int brSPal(int donja, int gornja)
{
      donja = A(donja);
      gornja = B(gornja);
      int br = 0;
      int razlika = gornja - donja;
      for(int i=0;i<=razlika;i++)
      {
            long long kvadrat = i*i+2*i*donja+donja*donja,broj = donja+i;
            if(isPal(broj)&&isPal(kvadrat))
            {
                  br++;
                  //F(broj);
                  //F(kvadrat);
            }

      }
      return br;
}

int main()
{
    ifstream in("C-small-attempt0.in");
    ofstream out("test.out");

    int a=1,b=100000,brT = 1;

    in>>brT;

    for(int i=1;i<=brT;i++)
    {
          in>>a>>b;
          F(brSPal(a,b));
          out<<"Case #"<<i<<": "<<brSPal(a,b)<<endl;
    }

    in.close();
    out.close();
    return 0;
}
