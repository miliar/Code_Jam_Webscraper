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

int main() {
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
  int T, tc;
  cin>>T;
  for(tc = 1; tc <= T; tc++)
    {
      string inp;
      int n, i, j;
      cin>>inp>>n;
      int check[105];
      memset(check, 0, sizeof(int)*105);
      /*      for(i = 0; i < inp.size(); i++)
	cout<<check[i]<<" ";
      cout<<endl<<"Reseting...\n";
      */
      for(i = 0; i < inp.size(); i++)
	{
	  if((inp[i] == 'a') || (inp[i] == 'e') || (inp[i] == 'i') || (inp[i] == 'o') || (inp[i] == 'u'))
	    check[i] = 1;
	}
      /*
      for(i = 0; i < inp.size(); i++)
	{
	  cout<<check[i]<<" ";
	}
      cout<<endl;
      */
      int  count = 0, cons = 0, flag = 0;
      for(i = 0; i < inp.size(); i++)
	{
	  cons = 0, flag = 0;
	  for(j = i; j < inp.size(); j++)
	    {
	      
	      if((check[j] == 0) && (flag == 0))
		{
		  cons++;
		  flag = 1;
		}
	      else if(check[j] == 0)
		{
		  cons++;
		}
	      else if(check[j] == 1)
		{
		  cons = 0;
		  flag = 0;
		}
	      if(cons >= n)
		{
		  count += (inp.size() - j);
		  //cout<<"brrr...cons:"<<cons<<" i:"<<i<<" j:"<<j<<" ans:"<<(inp.size() - j)<<endl;
		  break;
		}
	    }
	}
      cout<<"Case #"<<tc<<": "<<count<<endl;
    }
  return 0;
}
