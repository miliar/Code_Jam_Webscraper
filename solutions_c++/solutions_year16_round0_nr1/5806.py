#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main() {
  std::ifstream input;
  std::ofstream output;
  uint64_t T;
  input.open("input.in");
  output.open("output.out");
  input >> T;
  for(uint16_t count=1; count<=T; count++) {
    uint64_t a;
    input >> a;
    output << "Case #" << count << ": ";
    if(a==0) {
      output << "INSOMNIA";
    } else {
      std::vector <bool> seen(10);
      uint64_t cs = 0;
      uint64_t i=0;
      while(cs < 10) {
        i++;
        std::string str = std::to_string(a*i);
        for(uint64_t j=0; j<10; j++) {
          if(seen[j]==false && str.find('0'+j)!=std::string::npos) {
            cs++;
            seen[j]=true;
            //std::cout << str << '-' << j << '-' << str.find('0'+j) << '\n';
          }
        }
      }
      
      output << i*a;
    }
    output << '\n';
  }
}
