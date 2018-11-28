#include <bits/stdc++.h>
using namespace std;

char str[2005];
int alg[15], let[33];
int t;

int main() {
  scanf("%d", &t);
  for (int tt = 1; tt<=t; tt++) {
    memset(let, 0, sizeof(let));
    memset(alg, 0, sizeof(alg));
    scanf(" %s", str);
    for (int i = 0; str[i]!= '\0'; i++) let[str[i]-'A']++;

    alg[0] = let['Z'-'A'];
    let['Z'-'A'] -= alg[0];
    let['E'-'A'] -= alg[0];
    let['R'-'A'] -= alg[0];
    let['O'-'A'] -= alg[0];

    alg[2] = let['W'-'A'];
    let['T'-'A'] -= alg[2];
    let['O'-'A'] -= alg[2];
    let['W'-'A'] -= alg[2];

    alg[6] = let['X'-'A'];
    let['S'-'A'] -= alg[6];
    let['I'-'A'] -= alg[6];
    let['X'-'A'] -= alg[6];

    alg[7] = let['S'-'A'];
    let['S'-'A'] -= alg[7];
    let['E'-'A'] -= 2*alg[7];
    let['V'-'A'] -= alg[7];
    let['N'-'A'] -= alg[7];

    alg[8] = let['G'-'A'];
    let['E'-'A'] -= alg[8];
    let['I'-'A'] -= alg[8];
    let['H'-'A'] -= alg[8];
    let['T'-'A'] -= alg[8];
    let['G'-'A'] -= alg[8];

    alg[3] += let['H'-'A'];
    let['T'-'A'] -= let['H'-'A'];
    let['R'-'A'] -= let['H'-'A'];
    let['E'-'A'] -= 2*let['H'-'A'];
    let['H'-'A'] -= let['H'-'A'];

    alg[4] = let['R'-'A'];
    let['F'-'A'] -= alg[4];
    let['O'-'A'] -= alg[4];
    let['U'-'A'] -= alg[4];
    let['R'-'A'] -= alg[4];


    alg[5] = let['F'-'A'];
    let['F'-'A'] -= alg[5];
    let['I'-'A'] -= alg[5];
    let['V'-'A'] -= alg[5];
    let['E'-'A'] -= alg[5];

    alg[1] += let['O'-'A'];
    let['E'-'A'] -= let['O'-'A'];
    let['N'-'A'] -= let['O'-'A'];
    let['O'-'A'] -= let['O'-'A'];

    alg[9] = let['N'-'A']/2;
    let['N'-'A'] -= alg[9]*2;
    let['I'-'A'] -= alg[9];
    let['E'-'A'] -= alg[9];

    printf("Case #%d: ", tt);
    for (int i = 0; i<=9; i++) {
      while(alg[i]--) printf("%d", i);
    }
    printf("\n");
  }
}
