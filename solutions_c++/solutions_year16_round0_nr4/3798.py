#include <iostream>
#include <fstream>

template <class T>
inline T pow(T base, T exp) {
  T res = 1;
  while(exp) {
    if(exp & 1) res = (res * base);
    base = (base * base);
    exp >>= 1;
  }
  return res;
}

int main() {
  std::ifstream input;
  std::ofstream output;
  uint64_t T;
  input.open("input.in");
  output.open("output.out");
  input >> T;
  for(uint16_t count=1; count<=T; count++) {
    uint64_t k,c,s;
    input >> k >> c >> s;
    uint64_t p=pow(k,c-1);
    output << "Case #" << count << ":";
    for(uint64_t i=0; i<s; i++) {
      output << " " << 1+i*p;
    }
    output << '\n';
  }
}
