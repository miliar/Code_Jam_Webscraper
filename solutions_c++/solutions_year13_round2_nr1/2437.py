#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

typedef long long int64;
 
typedef pair<int,int> ipair;//NOTES:ipair
typedef vector<int> vi;
typedef vector<int64> vl;
typedef vector<vi> vii;
typedef vi::iterator vit;

int counter = 0;

int solve(int A, vi &motes)
{
  int64 a = A;
  vit i;
  int steps = 0;
  int64 grow;
  for (i = motes.begin(); i != motes.end(); i++) {
    if (*i < a) {
      a += *i;
    }
    else {
      steps++;
      grow = 2 * a - 1;
      if (grow > *i)
        a = grow;
    }
  }
  return steps;
}

void make() {
  printf("Case #%d: ", ++counter);
  int A, N;
  scanf("%d %d", &A, &N);
  int i, m;
  vi motes;
  vl sums;
  for (i = 0; i < N; i++) {
    scanf("%d", &m);
    motes.push_back(m);
  }
  sort(motes.begin(), motes.end());
  printf("%d\n", solve(A, motes));
  return;
}

int main()
{
  int t; 
  scanf("%d", &t);
  while(t--) {
      make();
  }
  return 0;
}
