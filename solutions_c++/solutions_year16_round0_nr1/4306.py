#include<cstdio>
#include<map>

using namespace std;

static unsigned long powersof10[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};

unsigned long n;

int getDigit(int v, int k) {
    return (v / powersof10[k]) % 10;
}

void countEachDigit(map<int, int> &digit, unsigned long nj) {
    for(int i=0; i<10; ++i) {
        if(nj<powersof10[i]) return;
        digit[getDigit(nj, i)] = 1;
        if(digit.size() == 10) return;
    }
}

int main() {
    int t, i = 0;
    scanf("%d", &t);
    while(t--) {
        scanf("%lu", &n);
        printf("Case #%d: ", ++i);
        if(n == 0) printf("INSOMNIA\n");
        else {
            map<int, int> digit;
            unsigned long ntmp, j = 1;
            while(digit.size() != 10) {
                ntmp = n*j++;
                countEachDigit(digit, ntmp);
            }
            printf("%lu\n", ntmp);
        }
    }
    return 0;
}
