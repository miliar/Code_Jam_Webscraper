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
  fin.open("B-large.txt");
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
    for(int i=0;i<N;i++)
    for(int j=0;j<M;j++)
      fin>>aa[i][j];
          int flag =0;
          int sum=0;
    for(int i=0;i<N;i++)
    for(int j=0;j<M;j++)
    {
      int s1=i,s2=j;
      flag = 0;
      for(int k=0;k<N&&flag==0;k++)
        if(aa[k][j]<=aa[i][j])
          flag = 0;
        else
          flag = 1;
      if(flag==1)
      {
        flag=0;
        for(int k=0;k<M&&flag==0;k++)
         if(aa[i][k]<=aa[i][j])
          flag = 0;
         else
           flag = 1;
      }
      if(flag==1)
      {
        i=N;
        j=M;
      }
    }
    fout<<"Case #"<<num++<<": ";
    if(flag==0)
      fout<<"YES"<<endl;
    else
      fout<<"NO"<<endl;



    test_cases--;
  }
  return 0;
}