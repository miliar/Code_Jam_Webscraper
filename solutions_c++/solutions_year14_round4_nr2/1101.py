#include <algorithm>
#include <functional>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <vector>
#include <sstream>
#include <numeric>
using std::cin;
using std::cout;

bool IsGood(const std::vector<int>& a, int N) {
  auto it = std::max_element(a.begin(), a.end());
  return std::is_sorted(a.begin(), it) && std::is_sorted(it, a.end(), std::greater<int>());
}

int CountSwaps(std::vector<int> a, int N) {
  int result = 0;

  for (int i = 0; i < N; ++i) {
    int index = (int)(std::find(a.begin(), a.end(), i) - a.begin());

    assert(index >= i);
    result += (index - i);

    a.erase(a.begin() + index);
    a.insert(a.begin() + i, i);
  }

  return result;
}

int main() {
  std::ios_base::sync_with_stdio(false);
//  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/1.txt", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/B-small-attempt0.in", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/B-small-attempt0.out", "wb", stdout);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {
    int N;
    cin >> N;

    std::vector<int> A(N);
    for (int& v : A) {
      cin >> v;
    }

    std::vector<int> B = A;
    std::sort(B.begin(), B.end());
    for (int& v : A) {
      v = (int)(std::lower_bound(B.begin(), B.end(), v) - B.begin());
    }

    std::vector<int> P;
    for (int i = 0; i < N; ++i) {
      P.push_back(i);
    }


    std::vector<int> num_to_position(N);
    std::vector<int> to_count(N);

    int answer = std::numeric_limits<int>::max();
    do {
      if (!IsGood(P, N)) {
        continue;
      }

      for (int i = 0; i < N; ++i) {
        num_to_position[P[i]] = i;
      }
      for (int i = 0; i < N; ++i) {
        to_count[i] = num_to_position[A[i]];
      }

      answer = std::min(answer, CountSwaps(to_count, N));

    } while (std::next_permutation(P.begin(), P.end()));

    cout << "Case #" << tc + 1 << ": " << answer << '\n';
  }
  return 0;
}
