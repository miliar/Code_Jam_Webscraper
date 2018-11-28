#include<iostream>
#include<fstream>
#include<vector>
#include<sstream>
#include<algorithm>
#include<cmath>
using namespace std;


int main()
{
  ifstream in("in.txt");
  ofstream out("out2.txt");
  int T;
  in >> T;
  for(int t = 1; t <= T; t++)
  {
    long long N, P;
    in >> N >> P;
    P--;
    vector<int> b(N,0);
    long long temp = P;
    int k = N-1;
    while(temp > 0)
    {
      b[k] = temp%2;
      k--;
      temp/=2;
    }
    long long max = (1LL << N) - 1, min = 0;
    for(int i = 0; i < N; i++)
    {
      if(b[i] == 0)
      {
        max = (1LL << (i+1)) - 2;
        break;
      }
    }
    int count = 0;
    int i = 0;
    while(i < N && b[i] == 0) {i++;count++;}
    for(int k  = i; k < N; k++)
    {
      if(b[k] == 0) 
      {
        count++;
        break;
      }
    }
    min = (1LL << N) - 1 - ( (1LL << count) - 1);
    out<<"Case #"<<t<<": "<<max<<" "<<min<<endl;
  } 
  return 0;
}
