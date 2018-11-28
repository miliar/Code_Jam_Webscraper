//
//  main.cpp
//  Google3
//
//  Created by Kirill on 14/04/2013.
//  Copyright (c) 2013 Kirill. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

string doit(vector<vector<int> > & a)
{
  for (int qwe = 1; qwe <= 100; ++qwe)
  {
  for (int i = 0; i < a.size(); ++i)
    for (int j = 0; j < a[i].size();++j)
    {
      if (a[i][j] == qwe)
      {
        bool godRod = true;
        for (int k = 0; k < a.size(); ++k)
        {
          if (!(a[k][j] == -1 || a[k][j] == qwe))
          {
            godRod = false;
            break;
          }
        }
        bool godCol = true;
        for (int k = 0; k < a[i].size(); ++k)
        {
          if (!(a[i][k] == -1 || a[i][k] == qwe))
          {
            godCol = false;
            break;
          }
        }
        if (!godCol && !godRod)
        {
          return "NO";
        }
        a[i][j] = -1;
      }
    }
  }
  return "YES";
}

int main(int argc, const char * argv[])
{
  fstream myfile, out;
  out.open("out.txt");
  myfile.open ("B-large.in");
  int num;
  myfile >> num;
  for (int i = 0; i < num;++i)
  {
    int a,b;
    myfile >> a;
    myfile >> b;
    vector<vector<int> > z(a, vector<int> (b, 0));
    for (int i = 0; i < a; ++i)
      for (int j = 0; j < b; ++j)
      {
        myfile >> z[i][j];
      }
    out << "Case #" << i + 1 <<": " << doit (z) <<'\n';
  }
  myfile.close();
  out.close();

}

