#include <iostream>
using namespace std;

long long isPrime(long long x) {
    long long i;
    //printf("Judge number %lld is Prime ?\n", x);
    for (i = 2; i*i <= x; i++) {
        if (x % i == 0) return i;
    }
    return 0;
}

void print_01(int x) {
    //printf("(%d) ", x);
    for (int i = 15; i >= 0; i--) {
        printf("%d", ((x >> i) & 1));
    }
}

long long conv(long long  x, int base){
    long long res = 0, y = 1;
    int t = x;
    int cnt = 1;
    while(x) {
        if (x & 1) {
       //     printf("%d is 1\n", cnt);
            res += y;
        }
      //  printf("x = %lld, res = %lld, y = %lld\n", x, res, y);
        x >>= 1;
        y *= base;
        cnt ++;
    }
    //print_01(t);
    //printf("(%d) base %d is %lld\n", t, base, res);
    return res;
}


int main() {

    long long x, p;
    int t,c = 1;
    long long a[11][2];
    int flag = 0;
    int cnt = 0;
    scanf("%d", &t);
    scanf("%d %d", &t, &t);
    printf("Case #1:\n");
    for(int i = 0; i <= 65535; i++) {
        //cout << "compute " << i << endl;
        flag = 0;
        if ((i & 1) == 0 || ((i >> 15) & 1) == 0) continue;
        for(int j = 2; j <= 10; j++){
            p = 0;
            x = conv(i, j);
            p = isPrime(x);
            if (p == 0) {
                flag = 1;
            }
            a[j][0] = x;
            a[j][1] = p;
        }
        if (flag == 1) continue;
        //printf("Case #%d: ", cnt);
        print_01(i);
        print_01(i);
        for (int j = 2; j <= 10; j++) {
            printf(" %lld", a[j][0]);
            //printf(" %lld", a[j][1]);
            //printf(" %lld(%lld)", a[j][1], a[j][0]);
        }
        printf("\n");
        cnt++;
        if (cnt == 500) {
            break;
        }
    }
    return 0;
}
