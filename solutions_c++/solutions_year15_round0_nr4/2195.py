#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
using namespace std;

int main()
{
  ifstream in;
  in.open("in.txt");
  ofstream out;
  out.open("out.txt");
  int P, X, Y, T;
  in >> T;

  for (int k = 1; k <= T; k++)
  {
    in >> P >> X >> Y;
    if(P <= 1) 
    {
        out << "Case #" << k << ": GABRIEL" << endl;   
        continue;
    }
    if(P == 2)
    {
        if(X*Y % P == 0) 
            out << "Case #" << k << ": GABRIEL" << endl;   
        else
            out << "Case #" << k << ": RICHARD" << endl;   
        continue;
    }
    if(P == 3)
    {
        if(X*Y % P != 0)
        {
            out << "Case #" << k << ": RICHARD" << endl;    
            continue;
        }
        if(X <= 1 || Y <= 1) 
        {
            out << "Case #" << k << ": RICHARD" << endl;    
            continue;
        }
        out << "Case #" << k << ": GABRIEL" << endl;       
        continue;
    }
    if(P == 4)
    {
        if(X*Y % P != 0) 
        {
            out << "Case #" << k << ": RICHARD" << endl; 
            continue;
        }
        if(X <= 2 || Y <=2 )
        {
            out << "Case #" << k << ": RICHARD" << endl; 
            continue;
        }
        out << "Case #" << k << ": GABRIEL" << endl;   
        continue;
    }
  }
  out.close();
  in.close();
   return 0;  
}
