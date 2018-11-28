#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

int main() {
  std::ifstream input;
  std::ofstream output;
  uint64_t T;
  input.open("input.in");
  output.open("output.out");
  input >> T;
  for(uint16_t count=1; count<=T; count++) {
    uint64_t N, K;
    input >> N >> K;
    std::vector <double> PS(N), P(K);
    for(uint64_t i=0; i<N; i++) input >> PS[i];
    std::sort(PS.begin(), PS.end());
    
    
    
    std::vector <double> PP(K+1);
    double max=0;
    for(uint64_t t=0;t<=K;t++) {
      for(uint64_t i=0; i<t; i++) P[i]=PS[i];
      for(uint64_t i=0; i<K-t; i++) P[i+t]=PS[N-1-i];
      PP[0]=1;
      for(uint64_t i=1; i<=K; i++) {PP[i]=0;}
      //for(uint64_t i=0; i<K; i++) std::cout << P[i]<<'-';
      //std::cout << '\n';
      //for(uint64_t i=0; i<=K; i++) std::cout << PP[i]<<' ';
      //std::cout << '\n';
      for(uint64_t i=0; i<K; i++) {
        for(uint64_t j=i+1; j>0;j--) {
          PP[j]=PP[j-1]*P[i]+PP[j]*(1-P[i]);
        }
        PP[0]=PP[0]*(1-P[i]);
        //for(uint64_t j=0; j<=K; j++) std::cout << PP[j]<<' ';
        //std::cout << '\n';
      }
      //for(uint64_t i=0; i<=K; i++) std::cout << PP[i]<<' ';
      //std::cout << '\n';
      if(max<PP[K/2]) max=PP[K/2];
    }
    output << "Case #" << count << ": ";
    output << max;
    output << '\n';
    std::cout << count;
  }
}
