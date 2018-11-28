#include <iostream>
#include <string>

std::string flipn(std::string s, int n) {
  std::reverse(s.begin(), s.begin()+n);
  for (int i = 0; i < n; ++i) {
    s[i] = ((s[i] == '+') ? '-' : '+');
  }
  return s;
}

int flips(std::string s) {
  int flips = 0;
  while (s != std::string(s.size(), '+')) {
    //std::cout << std::endl << s << std::endl;
    int flipPoint = s.find_first_not_of(s[0]);
    if (flipPoint == std::string::npos) {
      return flips+1;
    }
    s = flipn(s, flipPoint);
    flips++;
  }
  return flips;
}

int main() {
  int N;
  std::cin >> N;

  for (int n = 0; n < N; ++n) {
    std::string str;
    std::cin >> str;
    std::cout << "Case #" << n+1 << ": " << flips(str) << std::endl;
  }
}
