#include <bits/stdc++.h>

using namespace std;

bool tab[10];
int ile;

void sprawdz (int k) {
    while(k>0) {
        if(tab[k%10] == false) {
            ile++;
            tab[k%10] = true;
        }
        k/=10;
    }
}
int main() {
    int t, t2;
    scanf("%d", &t);
    t2 = t;
    while(t--) {
        printf("Case #%d: ", t2-t);
        ile = 0;
        long long n, m;
        scanf("%lld", &n);
        m=0;
        if(n == 0) {
            printf("INSOMNIA\n");
        }
        else {
            fill(tab, tab+10, false);
            while(ile != 10) {
                m+=n;
                sprawdz(m);
            }
            printf("%lld\n", m);
        }
    }
    return 0;
}

