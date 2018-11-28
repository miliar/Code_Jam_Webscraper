#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

#include <assert.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>
#include <time.h>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

typedef long long ll;

char let[3] ={'P','R','S'};

string solve(int win, int n) {
  if (n==0) {
    string s(1,let[win]);
    return s;
  }
  string s1=solve(win, n-1);
  string s2=solve((win+1)%3, n-1);
  if (s1>s2) {
    return s2+s1;
  }
  else
    return s1+s2;
}


int main()
{
  freopen("showdown.in", "r", stdin);
  freopen("showdown.out", "w", stdout);

  int t2;
  cin >> t2;
  for (int t1 = 1; t1 <= t2; ++t1) {
    printf("Case #%d: ", t1);
    int n,r,p,s;
    cin >> n >> r >> p >> s;
    int low = min(s,min(r,p));
    int high = max(s,max(r,p));
    if (high-low>1) {
      cout << "IMPOSSIBLE";
    }
    else {
      int winner=-1;
      int diff=0;
      if (n%2==0) {
	diff=high;
      }
      else {
	diff=low;
      }
      
      if (diff==r)
	winner=1;
      else if (diff==s)
	winner=2;
      else if (diff==p)
	winner=0;
      winner= (winner+n)%3;
      cout << solve(winner, n);
    }
    printf("\n");
  }
  return 0;
}
