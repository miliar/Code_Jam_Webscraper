#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main(void) {
  unsigned int n_t(0);

  cin >> n_t;

  for(unsigned int n_i(1); n_i <= n_t; ++n_i) {
    unsigned int n_max;
    unsigned int n_count(0);
    unsigned int n_total(0);
    string       sz_line;

    cin.ignore();

    cin >> n_max;
    cin >> sz_line;

    for(size_t n_j(0); n_j <= n_max; ++n_j) {
      unsigned int n_heads(sz_line[n_j] - '0');

      n_total += n_heads;

      if(n_total < (n_j + 1)) {
	++n_total;
	++n_count;
      }
    }

    fprintf(stdout, "Case #%u: %u\n", n_i, n_count);
  }
  
  return 0;
}
