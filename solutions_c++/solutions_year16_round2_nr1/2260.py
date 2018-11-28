#include <cstdio>
#include <cstring>

int main() {
  int T;
  char S[3000];
  scanf("%d ", &T);
  for (int TC = 1; TC <= T; ++TC) {
    scanf("%s", S);
    int len = strlen(S);
    int Freq[26];
    int Nums[10];

    memset(Freq, 0, sizeof Freq);
    memset(Nums, 0, sizeof Nums);

    for (int i = 0; i < len; ++i) {
      ++Freq[S[i] - 'A'];
    }

    while (Freq['U' - 'A']) {
      --Freq['F' - 'A'];
      --Freq['O' - 'A'];
      --Freq['U' - 'A'];
      --Freq['R' - 'A'];
      ++Nums[4];
    }

    while (Freq['Z' - 'A']) {
      --Freq['Z' - 'A'];
      --Freq['E' - 'A'];
      --Freq['R' - 'A'];
      --Freq['O' - 'A'];
      ++Nums[0];
    }

    while (Freq['X' - 'A']) {
      --Freq['S' - 'A'];
      --Freq['I' - 'A'];
      --Freq['X' - 'A'];
      ++Nums[6];
    }
    while (Freq['W' - 'A']) {
      --Freq['T' - 'A'];
      --Freq['W' - 'A'];
      --Freq['O' - 'A'];
      ++Nums[2];
    }
    while (Freq['G' - 'A']) {\
      --Freq['E' - 'A'];
      --Freq['I' - 'A'];
      --Freq['G' - 'A'];
      --Freq['H' - 'A'];
      --Freq['T' - 'A'];
      ++Nums[8];
    }
    while (Freq['F' - 'A']) {\
      --Freq['F' - 'A'];
      --Freq['I' - 'A'];
      --Freq['V' - 'A'];
      --Freq['E' - 'A'];
      ++Nums[5];
    }
    while (Freq['V' - 'A']) {\
      --Freq['S' - 'A'];
      --Freq['E' - 'A'];
      --Freq['V' - 'A'];
      --Freq['E' - 'A'];
      --Freq['N' - 'A'];
      ++Nums[7];
    }
    while (Freq['H' - 'A']) {\
      --Freq['T' - 'A'];
      --Freq['H' - 'A'];
      --Freq['R' - 'A'];
      --Freq['E' - 'A'];
      --Freq['E' - 'A'];
      ++Nums[3];
    }
    while (Freq['O' - 'A']) {\
      --Freq['O' - 'A'];
      --Freq['N' - 'A'];
      --Freq['E' - 'A'];
      ++Nums[1];
    }
    while (Freq['E' - 'A']) {\
      --Freq['N' - 'A'];
      --Freq['I' - 'A'];
      --Freq['N' - 'A'];
      --Freq['E' - 'A'];
      ++Nums[9];
    }

    printf("Case #%d: ", TC);
    for (int i = 0; i < 10; ++i) {
      while (Nums[i]) {
        printf("%d", i);
        --Nums[i];
      }
    }
    putchar('\n');
  }

}
