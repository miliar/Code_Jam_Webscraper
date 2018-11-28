#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <math.h>
#include <limits.h>

using namespace std;
/*
int gcd(int a, int b) {
  while (a != b) {
    if (a < b) {
      swap(a, b);
    }
    a %= b;
  }
  return a;
}*/

int gcd(int a,int b)
{
  int temp;
  if(a<b)
  {
    temp=a;
    a=b;
    b=temp;
  }
  while(b!=0)
  {
    temp=a%b;
    a=b;
    b=temp;
  }
  return a;
}


int solution() {
  int B, N;
  cin >> B >> N;
  vector<int> nums(B);
  for (int i = 0; i < B; ++i) {
    cin >> nums[i];
  }
  if (N < B) {
    return N;
  }
  int g = nums[0];
  for (int i = 1; i < B; ++i) {
    g = gcd(g, nums[i]);
  }

  int64_t cm = 1;
  for (int i = 0; i < B; ++i) {
    nums[i] /= g;
    cm *= nums[i];
  }

  int64_t dm = 0;
  for (int i = 0; i < B; ++i) {
    dm += cm / nums[i];
  }
  --N;
  N = N % dm;
  if (N < B) {
    return N+1;
  }
  N -= B;
  vector<int> times(B, 0);
  int res = 0;
  while (N >= 0) {
    int min_time = INT_MAX;
    for (int i = 0; i < B; ++i) {
      min_time = min(min_time, times[i] + nums[i]);
    }
    for (int i = 0; i < B; ++i) {
      if (times[i] + nums[i] == min_time) {
        times[i] = min_time;
        if (N == 0) {
          return i+1;
        }
        --N;
        break;
      }
    }
  }
}

int main() {
  int TS = 0;
  cin >> TS;
  for (int T = 1; T <= TS; ++T) {
    int res = solution();
    cout << "Case #" << T << ": ";
    cout << res;
    cout << endl;
  }
}
