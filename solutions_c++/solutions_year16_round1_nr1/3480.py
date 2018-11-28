#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


int main(int argc, char const *argv[]) {
  ifstream in(argv[1]);
  ofstream out("output.txt");


  int t;
  in>>t;
  for(int i = 1; i<=t; i++)
  {
    out<<"Case #"<<i<<": ";
    string word;
    in>>word;
    string op = "";
    char firstLetter;
    for(auto x: word)
    {
      if(op == "")
      {
        op.append(string(1,x));
        firstLetter = x;
      }
      else
      {
        if(static_cast<int>(x)>=static_cast<int>(op[0]))
        {
          op.insert(0, string(1,x));
        }
        else{
          op.append(string(1,x));
        }
      }

    }
    out<<op<<endl;

  }
  return 0;
}
