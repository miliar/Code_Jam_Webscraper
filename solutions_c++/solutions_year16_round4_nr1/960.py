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
    uint64_t N, R, P, S;
    input >> N >> R >> P >> S;
    output << "Case #" << count << ": ";
    if(N%2==0) {
      if (R==P+1 && P==S) {
        if(N==2) output << "PRRS";
      } else {
        if (P==S+1 && S==R) {
          if(N==2) output << "PRPS";
        } else {
          if (S==R+1 && R==P) {
            if(N==2) output << "PSRS";
          } else {
            output << "IMPOSSIBLE";
          }
        }        
      }
    } else {
      if (R+1==P && P==S) {
        if(N==1) output << "PS";
        if(N==3) output << "PRPSPSRS";
      } else {
        if (P+1==S && S==R) {
          if(N==1) output << "RS";
          if(N==3) output << "PRRSPSRS";
        } else {
          if (S+1==R && R==P) {
            if(N==1) output << "PR";
            if(N==3) output << "PRPSPRRS";
          } else {
            output << "IMPOSSIBLE";
          }
        }        
      }
    }
    output << '\n';
  }
}
