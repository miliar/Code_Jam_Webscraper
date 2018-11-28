#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <set>
#include <vector>
#include <stack>
#include <climits>
#include <functional>
#include <numeric>
#include <utility>
#include <ctime>
#include <map>
#include <ctype.h>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <queue>
#include <list>
using namespace std;


#define all(v)  v.begin(), v.end()
#define sz(v)   ((int)(v.size()))
#define vi      vector<int>
#define vii     vector<vector<int> >
#define vc vector<char>
#define vcc     vector<vector<char> >
#define allr(v) v.rbegin(), v.rend()
#define si set<int>
#define msi multiset<int>
#define pii pair<int,int>
#define pb push_back
#define ll long long
#define ull unsigned long long
const int INF = INT_MAX;

double c,f,x;
int t;

double getMinSec(double XL, double MF)
{
  if( (XL/MF)<=0.1)
    return 0; 
  return min(XL/MF,(c/MF)+getMinSec(XL,MF+f) );
}

int main(int argc, char const *argv[])
{
  freopen("B-small-attempt2.in","r",stdin);
  //int t,c,f,x;
  scanf("%d",&t);

  for (int i = 1; i <= t; ++i)
  {
      cin >> c >> f >> x;
      printf("Case #%d: %.7f\n",i, getMinSec(x,2));
  }

  return 0;
}