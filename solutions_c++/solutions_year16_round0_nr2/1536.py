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

//#define DEBUG

char swapc(char c)
{
  if(c == '-') return '+';
  return '-';
}

void swapS(int start, int end, string &S)
{
  while(start <= end){
    char cs=S[start];
    char ce=S[end];
    S[start] = swapc(ce);
    S[end] = swapc(cs);
    start++;
    end--;
  }
}

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    string S;
    cin>>S;
    int ans = 0;
    int B = S.length() - 1;
    int bottom = B;
    while (1) {
      while (bottom >= 0) {
        if(S[bottom] != '+') break;
        bottom--;
      }
      if(bottom < 0) break;
      int i = 0;
      while(S[i] == '+'){
        i++;
      }
      if(i>0){
        ans++;
        swapS(0, i-1, S);
      }
      ans++;
      swapS(0,bottom,S);
    }

    cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}

