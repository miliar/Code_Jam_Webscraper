#include <iostream>
#include <set>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
int main(int argc, char const *argv[]) {
  ifstream in("A-large.in");
  ofstream out("output.txt");
  int t;
  in>>t;
  auto containsAll = [](set<char> x){
    set<char> compSet = {'0','1','2','3','4','5','6','7','8','9'};
    if(compSet == x)
    {
      return true;
    }
    else
    {
      return false;
    }
  };
  auto toDigits = [](int x){
    string y = to_string(x);
    vector<char> v;
    for(auto i:y)
    {
      v.push_back(i);
    }
    return v;
  };
  for(int i = 1; i <= t; i++)
  {
    int n;
    set<char> seen;
    in>>n;
    if(n == 0)
    {
      out<<"Case #"<<i<<": INSOMNIA"<<endl;
    }
    else
    {
      int prod;
      int factor = 1;
      while(true)
      {
        prod = factor*n;
        vector<char> digs = toDigits(prod);
        for(auto c:digs)
        {
          seen.insert(c);
        }
        factor++;
        if(containsAll(seen))
        {
          out<<"Case #"<<i<<": "<<prod<<endl;
          break;
        }
      }
    }
  }




  return 0;
}
