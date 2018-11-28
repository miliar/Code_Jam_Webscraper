#include <iostream>
#include <stdio.h>
using namespace std;

// changes the string from a + to - or vice versa
string flip(string pancake, int start, int end)
{
  string happy = "+";
  for(int i = start; i < end; i++)
  {
    if (pancake.at(i) == happy.at(0))
    {
      pancake.replace(i, 1, "-");
    }

    else
    {
      pancake.replace(i, 1, "+");
    }
  }

  return pancake;
}

bool isHappy(string s)
{
  string sad = "-";
  for(size_t i = 0; i < s.length(); i++)
  {
    if (s.at(i) == sad.at(0))
    {
      return false;
    }
  }

  return true;
}

int main()
{
  int t;
  string s;
  string happy = "+";
  string sad = "-";

  cin >> t; // read number of testcases;

  for (int i = 1; i <= t; i++)
  {
    int flips = 0;
    cin >> s; // read in the string s

    int count = 0;
    while (!isHappy(s))
    {
      if (s.at(count) == happy.at(0))
      {
        while (count < s.length() && s.at(count) == happy.at(0))
        {
         count++;
        }

        s = flip(s, 0, count);
        flips++;
      }

     if (s.at(count) == sad.at(0))
     {
        while(count < s.length() && s.at(count) == sad.at(0))
        {
         count++;
        }


        s = flip(s, 0, count);
        flips++;
     }
    }

    cout << "Case #" << i << ": " << flips << endl;
  }
}
