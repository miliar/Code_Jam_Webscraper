#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void flip(string &s, int n)
{
  char c = s[0];
  int i;
  for(i = 0; i < n; i++)
  {
    if(c == '+')
      s[i] = '-';
    else
      s[i] = '+';
  }
}
int nextNotEqual(string s, char top)
{
  int i;
  for(i = 0; i < s.length(); i++)
  {
    if(s[i] != top)
      return i;
  }
  return -1;
}
bool allSame(string s, char c)
{
  int i;
  for(i = 0; i < s.length(); i++)
  {
    if(s[i] != c)
      return false;
  }
  return true;
}
int main()
{
  ifstream in;
  in.open("B-large.in");
  ofstream out;
  out.open("out.txt");
  int cases;
  in >> cases;
  int i;
  for(i = 0; i < cases; i++)
  {
    string s;
    in >> s;
    int count = 0;
    while(!allSame(s, '+'))
    {
      if(s.size() == 1)
        s = "+";
      else
      {
        char top = s[0];
        int index = nextNotEqual(s, top);
        if(index == -1)
        {
          s = "+";
        }
        else
        {
          flip(s, index);
        }
      }
      count++;
    }
    out <<"Case #" << (i+1)<< ": "<< count << endl;
  }
  return 0;
}
