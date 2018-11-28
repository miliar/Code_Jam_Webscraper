#include <iostream>
#include <map>
#include <algorithm>
#include <array>
#include <fstream>

using namespace std;

void missing(int num, ofstream &output)
{
  int n, temp;
  map<int, bool> present;
  cin >> n;
  for(int i = 0; i < 2*n-1; i++)
  {
    for(int j = 0; j< n; j++)
    {
      cin >> temp;
      present[temp] = !present[temp];
    }
  }

  output << "Case #" << num << ":";
  for(map<int,bool>::iterator it = present.begin(); it != present.end(); it++)
  {
    if(it->second)
    {
      output << " "<< it->first;
    }
  }
  output << endl;
}

int main()
{
  ofstream output;
  output.open("B.out");
  int t;
  cin >> t;
  for(int i = 1; i <= t; i++)
  {
    missing(i, output);
  }
  output.close();
}