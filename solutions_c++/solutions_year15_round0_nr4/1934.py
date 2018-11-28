#include <iostream>
#include <algorithm>
#define ll long long int
#include <fstream>
using namespace std;
ifstream in("input.in");
ofstream out("output.out");
int main()
{
  int t,i,j,X,R,C;
  in >> t;
  for(i = 1 ; i <= t ; i ++)
  {
      in >> X >> R >> C;
      out<<"Case #"<<i<<": ";
      switch(X)
      {
          case 1 : out<<"GABRIEL\n"; break;
          case 2 : if (R%2==0 || C%2==0) out << "GABRIEL\n"; else out <<"RICHARD\n"; break;
          case 3:  if ((R==2 && C==3) || (R==3 && C == 2) ||(R==3 && C == 3) ||(R == 3 && C == 4) ||(R == 4 && C == 3))
                   out <<"GABRIEL\n"; else out<<"RICHARD\n"; break;
         case 4: if ((R==3 && C == 4) ||(R==4 && C == 3) || (R==4 && C ==4)) out <<"GABRIEL\n"; else out<<"RICHARD\n"; break;

      }
  }
    return 0;
}
