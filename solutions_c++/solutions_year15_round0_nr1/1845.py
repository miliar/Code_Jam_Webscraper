#include <iostream>
#include <cstdio>
using namespace std;


class GCJ {
 public:
  static uint16_t const MAX_SHYNESS_LEVEL = 1000;
  GCJ(){}
 public:
  uint16_t const& friends_count() const {
    return mini_friends;
  }
  void init_shyness(int s_max, char const* init_shyness_level) {
    s_max_ = s_max + 1;
    int i = 0;
    for (; i != s_max_; ++i) {
      shyness_all_count[i] = *(init_shyness_level + i) - '0';
    }
  }
  void handle() {
    int low_bound = 0;
    int up_bound = s_max_;
    while (low_bound <= up_bound) {
      int mid = (low_bound + up_bound) / 2;
      //cout << "low bound = " << low_bound << "\n"
      //     << "up_bound = " << up_bound << "\n"
      //     << "mid = " << mid << "\n"
      //     << "judge = " << judge(mid) << endl;
      if (judge(mid)) {
        mini_friends = mid;
        up_bound = mid - 1;
      } else {
        low_bound = mid + 1;
      }
    }
  }
 private:
  bool judge(int friends_count) {
    int already_strand = friends_count + 
        (s_max_ > 0 ? shyness_all_count[0] : 0);
    int shyness = 1;
    for (; shyness <= s_max_; ++ shyness) {
      if (shyness <= already_strand) {
        already_strand += shyness_all_count[shyness];
      } else {
        return false;
      }
    }
    return true;
  }
 private: 
  uint16_t s_max_;
  uint16_t shyness_all_count[MAX_SHYNESS_LEVEL];
  uint16_t mini_friends;
};

int main() {
  freopen("/Users/corey.xpx/Desktop/A-large.in","r",stdin);
  freopen("/Users/corey.xpx/Desktop/out.txt","w",stdout);
  int T;
  int s_max;
  char init_shyness_level[GCJ::MAX_SHYNESS_LEVEL + 1];
  GCJ gcj;
  cin >> T;
  for (int case_count = 1; case_count <= T; ++case_count) {
    cin >> s_max >> init_shyness_level;
    gcj.init_shyness(s_max, init_shyness_level);
    gcj.handle();
    cout << "Case #" << case_count << ": " << gcj.friends_count() << endl;
  }
  return 0;
}
