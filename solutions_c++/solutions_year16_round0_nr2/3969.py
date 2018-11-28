#include <vector>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;
int main(int argc, char const *argv[]) {
  ifstream in(argv[1]);
  ofstream out("output.txt");
  auto negate = [](string vecSeg){
    string ret;
    for(auto i:vecSeg)
    {
      if(i == '-')
      {
        ret+='+';
      }
      else{
        ret+='-';
      }
    }
    return ret;
  };
  auto allNegative = [](string v){
    for(auto i:v)
    {
      if(i != '-')
      {
        return false;
      }
    }
    return true;
  };
  auto allPositive = [](string v){
    for(auto i:v)
    {
      if(i != '+')
      {
        return false;
      }
    }
    return true;
  };
  int t;
  in>>t;
  for(int i = 1; i <=t; i++)
  {
    string stack;
    in>>stack;
    if(allNegative(stack))
    {
      out<<"Case #"<<i<<": 1"<<endl;
    }
    else if(allPositive(stack))
    {
      out<<"Case #"<<i<<": 0"<<endl;
    }
    else
    {
      int numMoves = 0;
      while(true)
      {
        char starting = stack[0];
        auto pos = stack.find_first_not_of(starting);
        auto partialStack = stack.substr(0,pos);
        partialStack = negate(partialStack);
        stack.replace(0, pos, partialStack);
        numMoves++;
        if(allNegative(stack))
        {
          out<<"Case #"<<i<<": "<<numMoves+1<<endl;
          break;
        }
        if(allPositive(stack))
        {
          out<<"Case #"<<i<<": "<<numMoves<<endl;
          break;
        }
      }
    }
  }
  return 0;
}
