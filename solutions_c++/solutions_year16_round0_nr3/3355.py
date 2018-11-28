#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

long long xpow(long long x, long long y) {
    long long sol = 1;
    for (int i = 0; i < y; i++)
        sol *= x;
    return sol;
}

vector < string > perm;

void gen_perm(int n) {
    for (int i = 0; i < (1 << (n-2)); i++) {
        string s = "1";
        for (int i = 0; i < n-2; i++)
            s += '0';
        s += '1';

        int aux = i;
        int cont = 1;
        while (aux) {
            if (aux & 1)
                s[cont] = '1';
            aux >>= 1;
            cont++;
        }
        perm.push_back(s);
    }
}

int main() {
    int t, n, k;
    scanf("%d", &t);

    for (int tc = 1; tc <= t; tc++) {
        printf("Case #%d:\n", tc);
        scanf("%d %d", &n, &k);

        gen_perm(n);

        int cont = 0;

        for (int i = 0; i < perm.size(); i++) {
            vector < long long > divs;

            for (int a = 2; a <= 10; a++) {
                long long val = 0;

                for (int j = 0; j < perm[i].size(); j++) {
                    if (perm[i][j] == '1')
                        val += xpow(a, j);
                }

                int sqr = sqrt(val);
                for (long long j = 2; j <= sqr; j++)
                    if (val % j == 0) {
                        divs.push_back(j);
                        break;
                    }
            }

            if (divs.size() == 9) {
                reverse(perm[i].begin(), perm[i].end());
                cout << perm[i];
                for (int j = 0; j < divs.size(); j++)
                    printf(" %lld", divs[j]);
                printf("\n");

                cont++;
                if (cont == k) break;
            }
        }
    }
    return 0;
}

