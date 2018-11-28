//
//  main.cpp
//  google2
//
//  Created by Kirill on 13/04/2013.
//  Copyright (c) 2013 Kirill. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int arr[] = {1, 4, 9, 121, 22 * 22, 101 * 101, 111 * 111, 121 * 121, 202 * 202, 212 * 212};
fstream out;

using namespace std;

bool isPal(int a)
{
  vector<int> b;
  while(a)
  {
    b.push_back(a % 10);
    a /= 10;
  }
  for (int i = 0; i < b.size() / 2; ++i)
  {
    if (b[i] != b[b.size() - i - 1])
      return false;
  }
  return true;
}

int doit(int a, int b)
{
  int res = 0;
  for (int i = a; i <=b; ++i)
  {
    for (int j = 0; j < (sizeof(arr) / sizeof(int)); ++j)
    {
      std::cout << i << " " << arr[j] << endl;
      if (arr[j] == i)
      {
        ++res;
        break;
      }
      if (arr[j] > i )
        break;
    }
  }
  return res;
}


int main(int argc, const char * argv[])
{
  fstream myfile;
  out.open("out.txt");
  myfile.open ("C-small-attempt0.in");
  int num;
  myfile >> num;
  for (int i = 0; i < num;++i)
  {
    int a,b;
    myfile >> a;
    myfile >> b;
    out << "Case #" << i + 1 <<": " << doit (a, b) <<'\n';
  }
  myfile.close();
  out.close();

  return 0;
}

