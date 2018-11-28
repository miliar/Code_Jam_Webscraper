#include<cstdlib>
#include<iostream>
#include<fstream>
using namespace std;

int rem;

void check(bool* checker, int number) {
    while(number > 0) {
        rem = number % 10;
        checker[rem] = true;
        number /= 10;
    }
}

int main(int argc, char const *argv[]) {
    freopen("A-large.in", "r", stdin);
    freopen("A.test.output", "w", stdout);

    int N, tc, i, j,n, last;
    bool chk[10], isom, checker;

    scanf("%d", &N);
    for(tc=1;tc<=N;tc++) {
        scanf("%d", &n);
        memset(chk, false, sizeof(chk));
        i = 2;
        isom = false;
        last = -1;
        check(chk, n);
        while(!isom){
            if (i > 1 && ( n == (n*i) ) ){
                isom = true;
                break;
            }
            last = n*i;
            check(chk, n*i);
            checker = true;
            for(j=0;j<10;j++) {
                checker &= chk[j];
            }
            
            if(checker) break;
            i++;
        }

        if(isom) printf("Case #%d: %s\n", tc, "INSOMNIA");
        else printf("Case #%d: %d\n", tc, last);
    }

    return 0;
}