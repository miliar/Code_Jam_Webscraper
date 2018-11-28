#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>

int war(std::vector<float> N, std::vector<float> K, int num)
{
  int score =0 ;
  for (int i = 0; i < num; ++i){
    int j = 0;
    while (N[i] >= K[j] && j < num-i) { ++j;}
    if (j == num-i) { j = 0 ; ++score;}
    K.erase(K.begin()+j);
  }
  return score;
}

int main (int argc, char** argv)
{
  std::ifstream ifs(argv[1]);
  if (!ifs) {
    std::cout << "Cannot open" << argv[1] << std::endl;
    return -1;
  }

  int T;
  ifs >> T;

  for (int cases = 1; cases <= T && !ifs.eof(); ++cases) {
    int N; 
    ifs >> N;
    int y, z;

    std::vector<float> Naomi(N);
    std::vector<float> Ken(N);
    for (int i=0; i < N; ++i) {
      float a; ifs >> a;
      Naomi[i] = a;
    }
    for (int i=0; i < N; ++i) {
      float a; ifs >> a;
      Ken[i] = a;
    }

    std::sort(Naomi.begin(), Naomi.end());
    std::sort(Ken.begin(), Ken.end());

    y = N;
    int m = 0, M = N-1;
    for (int i=0; i<N; ++i) {
    	if (Naomi[i] < Ken[m] ) {
    		--y; --M;
    	} else {
    		++m;
    	}
    }

    z = war(Naomi, Ken, N);
    printf("Case #%d: %d %d\n", cases, y, z);
  }

  ifs.close();
  return 0;
}
