#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <utility>
#include <algorithm> // sort, max_element, random_shuffle, remove_if, lower_bound 
#include <functional>
#include <fstream>
#include <math.h>
using namespace std;
int palin(int i)
{
  int j=0;
  int s=i;
  while(i>0)
  {
    j = j*10+ (i%10);
    i = i/10;
  }
  if(s==j)
    return 1;
  else
    return 0;
}
int main()
{
  int test_cases;
  ifstream fin;
  fin.open("C-small-attempt0.txt");
  fin>>test_cases;
  int nums;
  int j=1;
  ofstream fout;
  fout.open("output.txt");
  int num=1;
  while(test_cases>0)
  {
    int a,b;
    fin>>a>>b;
    int cnt=0;
    for(int i=(int)((float)sqrt((float)a)-1);i<((float)sqrt((float)b)+1);i++)
    {
      if(palin(i))
        if(palin(i*i))
          if(i*i <=b && i*i>=a)
            cnt++;

    }
    fout<<"Case #"<<num++<<": "<<cnt<<endl;
    test_cases--;
  }
  return 0;
}