#include <algorithm>
#include <iostream>

struct Party {
  Party(char label, unsigned int count)
  : label(label), count(count) { };
  char label;
  unsigned int count;
};

void task() {
  unsigned int u, N;
  std::cin >> N;
  std::vector<Party> s;

  auto c = [=](Party p0, Party p1) {
    return p0.count < p1.count;
  };

  for(u = 0; u < N; ++u) {
    unsigned int p;
    std::cin >> p;
    s.push_back(Party('A' + u, p));
  }

  std::make_heap(s.begin(), s.end(), c);

  while(s.size() > 2) {
    std::pop_heap(s.begin(), s.end(), c);
    Party p = s.back();
    if(p.count == 1) {
      s.pop_back();
    } else {
      --s.back().count;
      std::push_heap(s.begin(), s.end(), c);
    }
    std::cout << ' ' << p.label;
  }

  while(s[1].count != s[0].count) {
    std::cout << ' ' << s[1].label;
    --s[1].count;
  }

  while(s[1].count > 0) {
    std::cout << ' ' << s[0].label << s[1].label;
    --s[1].count;
  }
}

int main(int argc, char **argv) {
  unsigned int u, T;

  std::cin >> T;

  for(u = 1; u <= T; ++u) {
    std::cout << "Case #" << u << ":";
    task();
    std::cout << std::endl;
  }

  return 0;
}
