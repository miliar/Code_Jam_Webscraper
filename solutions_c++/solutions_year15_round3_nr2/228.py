#include <bits/stdc++.h>

using namespace std;

int K, L, S;

string KEY, TARGET;

size_t repeat()
{
  size_t i = 1;
  for(; i < TARGET.size(); ++i){
    size_t len = TARGET.size() - i;
    if(0 == TARGET.compare(i, len, TARGET, 0, len)){
      break;
    }
  }
  return i;
}

size_t maxbanana()
{
  size_t rep = repeat();
  size_t j = 0;
  for(size_t i = L; i <= S; i += rep, ++j){
  }
  return j;
}

map<char, size_t> KEYMAP;

void fillmap()
{
  KEYMAP.clear();
  for(const auto& c : KEY){
    ++KEYMAP[c];
  }
}

bool can()
{
  // 文字列長は保証されてる
  // 文字種のチェック
  for(const auto& c : TARGET){
    if(KEYMAP[c] == 0){
      return false;
    }
  }
  return true;
}

double getrate()
{
  double rate = 1.0;
  for(const auto c : TARGET){
    rate = rate * KEYMAP[c] / K;
  }
  return rate;
}

double solve()
{
  fillmap();
  if(!can()){
    return 0.0;
  }
  size_t mbanana = maxbanana();
  double rate = getrate();
  return mbanana - (S - L + 1) * rate;
}

int main(){
  size_t T;
  std::cin >> T;
  for(size_t i = 1; i <= T; ++i){
    std::cin >> K >> L >> S >> KEY >> TARGET;
    std::cout << "Case #" << i << ": " << setprecision(9) << solve() << "\n";
  }
}
