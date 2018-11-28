#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

bool unique(vector<int> digits, int n)
{
  int i;
  for(i = 0; i < digits.size(); i++)
  {
    if(digits[i] == n)
      return false;
  }
  return true;
}
void add(vector<int> &digits, int n)
{
  while(n > 0)
  {
    if(unique(digits, n%10))
      digits.push_back(n%10);
    n /= 10;
  }
}
int main()
{
  ifstream tests;
  ofstream output;
  output.open("out.txt");
  tests.open("A-large.in");
  int testcases;
  tests >> testcases;
  int i;
  for(i = 0; i < testcases; i++)
  {
    int n;
    tests >> n;
    if(n == 0)
    {
      output << "Case #" << (i+1) << ": " <<"INSOMNIA" << endl;
    }
    else
    {
        vector<int> digits;
        int mul = n;
        add(digits, mul);
        int x = 2;
        while(digits.size() != 10)
        {
           mul = n*x;
           add(digits, mul);
           x++;
        }
        output << "Case #" << (i+1) << ": "  << mul << endl;
    }
  }
}
