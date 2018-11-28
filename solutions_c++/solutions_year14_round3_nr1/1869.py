#include<cstdio>

using namespace std;

int log(int n) {
     if (n==0) return -1;
     int logValue = -1;
     while (n) {//
         logValue++;
         n >>= 1;
     }
     return logValue;
}



long long testcase() {
    long long p,q;
    scanf("%lld/%lld", &p, &q);
    long long q2 = q;
    long long z = 0;
    while (q2 > 0 && q2 % 2 == 0){
        z++;
        q2 /= 2;
    }

    if (q2 != 1 && q2 != p) return -1;
    if (z > 40) return -1;

    int counter = 1;
    while (2*p < q && counter <= 42) {
        p *= 2;
        counter++;
    }

    if (counter > 40) return -1;
    return counter;

}

int main () {
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T;t++) {
        int r = testcase();
        if (r > -1) {
            printf("Case #%d: %d\n", t, r);
        } else {
            printf("Case #%d: impossible\n", t);
        }
    }
}
