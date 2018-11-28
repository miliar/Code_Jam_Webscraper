#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>

#define FOR(I,A,B)   for(int I= (A); I<(B); ++I)
#define REP(I,N)     FOR(I,0,N)
#define ALL(A)       (A).begin(), (A).end()
#define SZ(A)        int((A).size())
#define PB           push_back
#define FST(A)       (A).first
#define SEC(A)       (A).second
#define DEBUG        0

typedef unsigned long long int ulld;

using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<bool> vb;

int main ()
{
  int T;
  cin >> T;
  REP(t, T) {
    int N, X;
    cin >> N >> X;
    vector<int> nums(N);
    REP(i, N)
      cin >> nums[i];
    sort(nums.begin(), nums.end());
    int count = 0;
    while (!nums.empty()) {
      auto lastElement = nums.end();
      lastElement--;
      int val = *lastElement;
      nums.erase(lastElement);
      if (nums.empty()) {
        count++;
        break;
      }
      auto itUpp = lower_bound(nums.begin(), nums.end(), X-val);
      if (itUpp == nums.end()) {
        // take last element
        auto otherLast = nums.end();
        otherLast--;
        nums.erase(otherLast);
      }
      else {
        while (true) {
          bool isFirst = itUpp == nums.begin();
          if (*itUpp > X-val) {
            if (itUpp == nums.begin()) {
              break;
            }
            itUpp--;
          }
          else {
            nums.erase(itUpp);
            break;
          }
          if (isFirst)
            break;
        }
      }
      count++;
    }
    cout << "Case #" << t+1 << ": " << count << endl;
  }
}
