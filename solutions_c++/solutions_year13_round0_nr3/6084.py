#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#include <complex>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

inline bool palin(int64 num)
{
  string numStr;
  std::stringstream strstream;
  strstream<<num;
  strstream>>numStr;
  int len = numStr.size();
  for(int i = 0; i < len; i++)
    {
      if(numStr[i] != numStr[len - (i+1)]) return false;
    }
  return true;
}

int main() {
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
  int t, i, j, n;
  cin>>t;
  int64 A, B, count;
  for(n = 1; n <= t; n++)
    {
      count = 0;
      cin>>A>>B;
      cout<<"Case #"<<n<<": ";
      double t_A = sqrt(double(A)), t_B = sqrt(double(B));
      int64 sqA, sqB;
      if(t_A - (long long)(t_A) > 0)
	{
	  sqA = ceil(t_A);
	  if(sqA * sqA > B)
	    {
	      cout<<count<<endl;
	      continue;
	    }
	}
      else sqA = t_A;
      if(t_B - (long long)(t_B) > 0)
	{
	  sqB = floor(t_B);
	  if(sqB * sqB < A)
	    {
	      cout<<count<<endl;
	      continue;
	    }
	}
      else sqB = t_B;
      for(j = sqA; j <=sqB; j++)
	{
	  if(palin(j) && palin(j*j))
	    count++;
	}
      cout<<count<<endl;      
    }
  return 0;
}
