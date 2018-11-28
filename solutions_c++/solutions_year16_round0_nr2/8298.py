#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


int tester(string val)
{
  int counter = 1;
  char curSymb = val.at(0);
  for(int i = 1; i < val.length(); i++)
  {
    if(val.at(i) != curSymb)
    {
      curSymb = val.at(i);
      counter++;
    }
  }
  if(curSymb == '+')
  {
    counter = counter - 1;
  }
  return(counter);
}

int main() {
  int t, sol;
  string pancakes;
  cin >> t;
  getline(cin,pancakes);
  for (int i = 1; i <= t; i++) {
    getline(cin,pancakes);   
    sol = tester(pancakes);
    cout << "Case #" << i << ": " << sol << endl; 
  }
  return 0;
}
