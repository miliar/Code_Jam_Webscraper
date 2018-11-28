#include <iostream>
#include <map>
#include <vector>
#include <deque>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <cstdint>

std::vector<int> split(int K, int C) {
  std::vector<int> part;
  if (C > K) {
    part.push_back(1);
    return part;
  }
  
  for (int i = 1; i <= K; i += C) {
    part.push_back(i);
    //std::cout << "part: " << i << std::endl;
  }
  if (part.back() > (K - C + 1)) {
    part.pop_back();
    part.push_back(K - C + 1);
    //std::cout << "fix part: " << part.back() << std::endl;
  }
  
  return part;
}

uint64_t calc_part(int p, int K, int C) {
  //std::cout << "calc_part " << p << " " << " K " << K <<" C " << C << std::endl;
  if (C > K) C = K;
  uint64_t resp = 1;
  int q = p + C - 2;
  uint64_t kc = 1;
  for(int i = 0; i < C; i++, q--) {
    resp += q * kc;
    //std::cout << "resp :" << q << " ^ " << kc << " -> " << resp << std::endl;
    kc *= K;
  }
  return resp;
}

std::string solve() {
  int K;
  std::cin >> K;
  int C;
  std::cin >> C;
  int S;
  std::cin >> S;
  //std::cout << "K " << K << " C " << C << " S " << S << std::endl;
  
  std::vector<int> parts = split(K, C);
  if (S < parts.size()) return "IMPOSSIBLE";

  std::stringstream output;
  for(int p : parts) {
    uint64_t resp = calc_part(p, K, C);
    output << " " << resp;   
  }
  return output.str();
}

int main(int argc, char* argv[]) {
  int T;
  std::cin >> T;
  for(int t = 1; t <= T; ++t) {
    std::string response = solve();
    std::cout << "Case #" << t << ":" << response << std::endl;
  }
  return 0;
}