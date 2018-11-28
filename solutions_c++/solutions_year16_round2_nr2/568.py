#include <bits/stdc++.h>

using namespace std;

typedef long long int int64;

char S[2][30];
int64 c, j;
int n;


int64 getMax(int p, int i, int64 vl) {
   for (; i < n; ++i) {
       if (S[p][i] != '?') {
           vl = vl * 10 + S[p][i] - '0';
       } else {
           vl = vl * 10 + 9;
       }
   }
   return vl;
}

int64 getMin(int p, int i, int64 vl) {
   for (; i < n; ++i) {
       if (S[p][i] != '?') {
           vl = vl * 10 + S[p][i] - '0';
       } else {
           vl = vl * 10;
       }
   }
   return vl;
}


void relax(int64 vc, int64 vj) {
    if (abs(vc - vj) < abs(c - j)) {
       c = vc;
       j = vj;
       return;
    }

    if (abs(vc - vj) == abs(c - j)) {
        if (vc < c) {
            c = vc;
            j = vj;
            return;
        }
        if (vc == c) {
            if (vj < j) {
                c = vc;
                j = vj;
            }
        }
    }
}

int main() {
    int T;
    scanf("%d\n", &T);
    for (int test = 1; test <= T; ++test) {        
        scanf("%s %s\n", S[0], S[1]);
        n = strlen(S[0]); 
      
        c = 0;
        for (int i = 0; i < n; ++i) {
            if (S[0][i] != '?') {
                c = c * 10 + S[0][i] - '0';
            } else {
                c = c * 10;
            }
        }
        j = 0;

        for (int i = 0; i < n; ++i) {
            j = j * 10;
            if (S[1][i] != '?') {
                j += S[1][i] - '0';
            }
        }

        
        int64 cc = 0, cj = 0;
        for (int i = 0; i < n; ++i) {
            if (S[0][i] != '?' && S[1][i] != '?') {
                cc = cc * 10 + S[0][i] - '0';
                cj = cj * 10 + S[1][i] - '0';
                if (S[0][i] > S[1][i]) {
                    cc = getMin(0, i + 1, cc);
                    cj = getMax(1, i + 1, cj);
                    relax(cc, cj);
                    break;
                } else if (S[0][i] < S[1][i]) {
                    cc = getMax(0, i + 1, cc);
                    cj = getMin(1, i + 1, cj);
                    relax(cc, cj);
                    break;
                }
                continue;    
            }
            if (S[0][i] != '?' && S[1][i] == '?') {
                cc = cc * 10 + S[0][i] - '0';
                if (S[0][i] != '0') {
                    cj = cj * 10 + S[0][i] - '0' - 1;
                    int64 vj = getMax(1, i + 1, cj);
                    int64 vc = getMin(0, i + 1, cc);
                    relax(vc, vj);
                    cj /= 10;
                }
                if (S[0][i] != '9'){
                    cj = cj * 10 + S[0][i] - '0' + 1;
                    int64 vj = getMin(1, i + 1, cj);
                    int64 vc = getMax(0, i + 1, cc);
                    relax(vc, vj);
                    cj /= 10;           
                }
                cj = cj * 10 + S[0][i] - '0';
            }

            if (S[0][i] == '?' && S[1][i] != '?') {
                cj = cj * 10 + S[1][i] - '0';
                if (S[1][i] != '0') {
                    cc = cc * 10 + S[1][i] - '0' - 1;
                    int64 vj = getMin(1, i + 1, cj);
                    int64 vc = getMax(0, i + 1, cc);
                    relax(vc, vj);
                    cc /= 10;
                }
                if (S[1][i] != '9'){
                    cc = cc * 10 + S[1][i] - '0' + 1;
                    int64 vj = getMax(1, i + 1, cj);
                    int64 vc = getMin(0, i + 1, cc);
                    relax(vc, vj);
                    cc /= 10;           
                }
                cc = cc * 10 + S[1][i] - '0';
            }


            if (S[0][i] == '?' && S[1][i] == '?') {
               cj = cj * 10;
               cc = cc * 10 + 1;
               int64 vj = getMax(1, i + 1, cj);
               int64 vc = getMin(0, i + 1, cc);
               relax(vc, vj);
               cj /= 10;
               cc /= 10;

               cj = cj * 10 + 1;
               cc = cc * 10;
               
               vj = getMin(1, i + 1, cj);
               vc = getMax(0, i + 1, cc);
               relax(vc, vj);
               cj /= 10;
               cc /= 10;
                
               cj = cj * 10;
               cc = cc * 10;
            }
        }
        relax(cc, cj);



        cout << "Case #" << test << ": ";
        int l1 = 0;
        int64 tst = 1;
        while (tst <= c) {
            ++l1;
            tst *= 10;
        }

        if (c == 0) ++l1;
        for (int i = 0; i < n - l1; ++i) {
            cout << "0";
        }
        cout << c << " ";
        l1 = 0;
        tst = 1;
        while (tst <= j) {
            ++l1;
            tst *= 10;
        }

        if (j == 0) ++l1;
        for (int i = 0; i < n - l1; ++i) {
            cout << "0";
        }
        cout << j << "\n";
    }
}