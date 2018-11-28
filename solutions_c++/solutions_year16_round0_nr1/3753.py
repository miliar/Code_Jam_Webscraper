#include <cstdio>
#include <string>

int main() {
  unsigned T;
  scanf("%u", &T);

  for(unsigned i = 1; i <= T; ++i) {
    unsigned N;
    scanf("%u", &N);

    printf("Case #%u: ", i);
    if(!N) {
      printf("INSOMNIA\n");
      continue;
    }

    unsigned j;
    char cont_flag = 10;
    char counts[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    for(j = 1; cont_flag; ++j) {
      for(auto && c : std::to_string(j * N)) {
        if(!counts[c - '0']) {
          counts[c - '0'] = 1;
          cont_flag--;
        }
      }
    }
    printf("%u\n", (j - 1) * N);
  }
}
