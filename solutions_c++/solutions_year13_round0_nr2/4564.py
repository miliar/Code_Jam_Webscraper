#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <cmath>
#include <map>
#include <cctype>
#include <climits>
#include <cassert>
#include <sstream>
using namespace std;

#define MOD 1000000007

#define all(C) (C).begin(),(C).end()
#define tr(C, it) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); it++)

 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 

typedef long long LL;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;

int a[100][100];

int process() {
  int n,m;
  cin>>n>>m;
  vi maxr(100,0), maxc(100,0);

  for (int i=0; i<n; i++) { 
    maxr[i] = 0;
    for (int j =0; j<m; j++) {
      cin>>a[i][j];
      maxr[i] = max(maxr[i], a[i][j]);
    }
  }

  for (int i =0; i<m; i++) {
    for (int j =0; j<n; j++) {
      maxc[i] = max(maxc[i], a[j][i]);
    }
  }

  for (int i=0; i<n; i++) {
    for (int j =0; j<m; j++) {  
      if (a[i][j] < min(maxr[i], maxc[j])) {
        return 0;
      }
    }
  }
  return 1;

}


int main() {
  string msg;
  int i, t=1;
  cin >>t;
  for (i = 0; i <t; i++) {
    int r = process();
    if (r) {
      msg = "YES";
    } else {
      msg = "NO";
    }
    cout<<"Case #"<<i+1<<": "<<msg<<endl;
  }
}
