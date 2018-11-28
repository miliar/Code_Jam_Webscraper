//wise words from the departing:
//eat your greens, especially broccoli
//remember to say thank you for all the things
//you haven't had
#include <ctime>
#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <map>
#include <bitset>
#include <string.h>
#include <stdio.h>
#include <sstream>
#include <set>
#include <stdlib.h>
#include <memory.h>

using namespace std;

#define		FOR(i,a,b) for(int i=int(a);i<int(b);++i)
#define		X first
#define		Y second
typedef pair <int,int> pii;
#define MP(a,b) make_pair(a,b);
typedef vector <int> vi;
typedef set <int> si;

int arr[1001];

bool p(int x) {
  string a, b;
  stringstream ss;
  ss << x;
  a = ss.str();
  b = a;
  reverse(b.begin(), b.end());
  return a == b;
}

int main()
{

#ifndef ONLINE_JUDGE
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
#endif
#ifdef ONLINE_JUDGE
  //freopen("input.txt", "r", stdin);
  //freopen("output.txt", "w", stdout);
#endif
  int T;
  
  cin >> T;
  
  for(int i = 1; i*i<=1000; i++) {
    if(p(i) && p(i*i))
      arr[i*i] = 1;
  }
  
  int a,b, ans;
  FOR(i, 0, T) {
    cin >> a >> b;
    ans = 0;
    for(int j = a; j<=b; j++)
      if(arr[j]) {
        ans++;
      }
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  return 0;
}
