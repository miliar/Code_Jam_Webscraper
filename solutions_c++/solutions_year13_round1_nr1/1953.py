#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <utility>
#include <algorithm> // sort, max_element, random_shuffle, remove_if, lower_bound 
#include <functional>
#include <fstream>
using namespace std;
char a[4][4];
int aa[101][101];
int main()
{
  int test_cases;
  ifstream fin;
  fin.open("A-small-attempt0 (2).in");
  fin>>test_cases;
  int nums;
  int j=1;
  ofstream fout;
  fout.open("output.txt");
  int num=1;
  while(test_cases>0)
  {
    int N,M;
    fin>>N>>M;
    int cnt=0;
    int radius=N;
    while(2*radius+1 <= M)
    {
      M = M - 2*radius - 1;
      cnt++;
      radius = radius+2;
    }
    fout<<"Case #"<<num<<": ";
      fout<<cnt<<endl;
    num++;


    test_cases--;
  }
  return 0;
}