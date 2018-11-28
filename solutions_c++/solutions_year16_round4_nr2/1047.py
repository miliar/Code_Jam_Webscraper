// 2016 Round 2, Problem B:
// Copyright 2016 Christian Brechbuehler alias Quigi
// using gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1)

#include <iostream>
#include <vector>


class In {                      // const int, initialized from std::cin
public:
  In() {std::cin >> i_;}
  operator int() {return i_;}
private:
  int i_;
};

typedef std::vector<double> VD;

// TODO optimize using 'lame'
static double p_max(const int N, const int K, const VD& P, VD p_yes) {
  // pick K more members from among the first N

  if (N == 0) return p_yes[p_yes.size()/2];
  const int i = N-1;            // consider last member
  double best = 0;
  // leave out
  if (K < N) {
    // std::cerr << "skip " << i << " (" << P[i] << ")" << std::endl;
    best = std::max(best, p_max(i, K, P, p_yes));
  }
  // include
  if (K > 0) {
    const int K1 = p_yes.size()-K;
    for (int j = K1; j > 0 ; --j)
      p_yes[j] = (1-P[i])*p_yes[j] + P[i]*p_yes[j-1];
    p_yes[0] *= 1-P[i];
    best = std::max(best, p_max(i, K-1, P, p_yes));
  }
  return best;
}

static double do_case() {
  In N, K;
  VD P(N),                      // probability by member
    p_yes(K+1);                 // probability of [0..K] number of "yes" votes,
  for (double& p:P) std::cin >> p;
  p_yes[0]=1.0;
  return p_max(N, K, P, p_yes);
}

int main() {
  In T;
  for (int j = 1; j <= T; ++j) {
    std::cout << "Case #" << j << ": "
              << do_case()
              << std::endl;
  }
  return 0;
}
