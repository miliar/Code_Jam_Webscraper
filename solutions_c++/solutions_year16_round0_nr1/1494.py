#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair

int main(void)
{
  int T,t;
  int ret;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N;
    cin>>N;
    LL sum = 0;
    UINT32 bits = 0;
    if (N == 0){
      cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
      continue;
    }
    LL i = 1;

    for(;i<=100000000;i++)
    {
      sum += N;
      LL tmp = sum;
//cout<<tmp<<endl;
      while(tmp > 0){
        int m = tmp % 10;
        bits |= (1<<m);
        tmp /= 10;
      }
      if( bits == 0x3ff) break;
    }
    if (bits == 0x3ff) {
      cout<<"Case #"<<t<<": "<<sum<<endl;
    } else { 
      cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
    }
  }
  return 0;
}

