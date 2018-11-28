// 2016 Round 2, Problem A. Rather Perplexing Showdown
// Copyright 2016 Christian Brechbuehler alias Quigi
// using gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1)

#include <iostream>
#include <vector>
#include <map>


class In {                      // const int, initialized from std::cin
public:
  In() {std::cin >> i_;}
  operator int() {return i_;}
private:
  int i_;
};

static void lineup(int p, int r, int s) {
  if (p + r + s == 1) {
    if (p==1) std::cout << "P";
    if (r==1) std::cout << "R";
    if (s==1) std::cout << "S";
    return;
  }
  lineup((p+1)/2, (r+1-p%2)/2, s    /2);
  lineup((p  )/2, (r+  p%2)/2, (s+1)/2);
}

static void do_case() {
  In N, R, P, S;
  const int third = (1<<N)/3;
  if (R < third || P < third || S < third ||
      R > third+1 || P > third+1 || S > third+1)
    std::cout << "IMPOSSIBLE";
  else 
    lineup(P, R, S);
}

int main() {
  In T;
  for (int j = 1; j <= T; ++j) {
    std::cout << "Case #" << j << ": ";
    do_case();
    std::cout << std::endl;
  }
  return 0;
}
