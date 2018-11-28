#include "cassert"
#include "vector"
#include "iostream"
#include "set"
#include "functional"

using namespace std;

int main() {
  int T, t = 1, N, X;
  for (std::cin >> T; t <= T; ++t) {
    std::cout << "Case #" << t << ": ";
    std::cin >> N;
    int n = N;
    std::vector<int> a(N+1);
    /*
    std::vector<int> seq(N);
    std::map<int, int> pos;
    for (int i = 0; i < N; ++i) {
      std::cin >> seq[i];
      pos[seq[i]] = i;
    }
    auto sort_seq = seq;
    std::sort(sort_seq.begin(), sort_seq.end());
    int ans = 0;
    int beg = 0, end = N - 1;
    for (int i = 0; i < sort_seq.size(); ++i) {
      int x = sort_seq[i];
      int b = abs(pos[x] - beg), e = abs(end - pos[x]);
      if (b < e) { 
	++ beg;
      } else {
	-- end;
      }
      ans += std::min(b, e);
    }
    */
            int ans = 0;
        for (int i = 1; i <= n; i++) {
            int f = 0, g = 0;
            for (int j = 0; j < i; j++) {
                if (a[j]  > a[i] ) f++;
            }
            for (int j = i + 1; j <= n; j++) {
                if (a[j]  > a[i] ) g++;
            }
            ans += min(f, g);
        }
    std::cout << ans << std::endl;
	
  }
  return 0;
}
