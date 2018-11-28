#include <iostream>
#include <fstream>

int main() {
  std::ifstream input;
  std::ofstream output;
  uint64_t T;
  input.open("input.in");
  output.open("output.out");
  input >> T;
  for(uint16_t count=1; count<=T; count++) {
    std::string a;
    input >> a;
    uint64_t c = 0;
    for(uint64_t i=0; i+1<a.length(); i++) {
      if(a[i]!=a[i+1]) c++;
    }
    if(a[a.length()-1] == '-') c++;
    output << "Case #" << count << ": ";
    output << c;
    output << '\n';
  }
}
