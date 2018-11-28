#include <bits/stdc++.h>

using namespace std;

long long a[12];
int bin[20];

long long power(int a, int n) {
    long long sol = 1;
    while (n--) sol *= a;
    return sol;
}

int main() {
    freopen("C-large.out", "w", stdout);

    int len = 32;
    int num = 500;
    for (int j=2; j<=10; j++) {
        //1<<len/2 + 1
        a[j] = power(j, len/2) + 1;
    }
    cout << "Case #1:" << endl;
    int x = (1 << len/2 - 1) + 1; //100..01
    for (int i=0; i<num; i++) {
        int xx = x;
        for (int j=len/2-1; j>=0; j--) {
            bin[j] = xx & 1;
            xx >>= 1;
        }
        for (int k=0; k<2; k++)
            for (int j=0; j<len/2; j++) printf("%d", bin[j]);


        for (int j=2; j<=10; j++) {
            printf(" %lld", a[j]);
        }
        printf("\n");
        x += 2;
    }



    return 0;
}
