#include <iostream>
#include <bitset>

using namespace std;

bitset<10> b;

int n, t;

bool check_digits(bitset<10> &b, int number) {
    while(number>0) {
        b.set(number%10, true);
        number/=10;
    }
    return b.all();
}

int main() {

    scanf("%d", &t);

    for (int c = 0; c < t; ++c) {
        scanf("%d", &n);
        b.reset();

        printf("case #%d: ", c+1);

        bool found = false;

        if(n<=0) {
            printf("INSOMNIA\n");
            continue;
        }

        int i;
        for (i = 1; ; ++i) {
            if(check_digits(b, i*n))
            {
                found = true;
                break;
            }
        }

        printf("%d\n", i*n);

    }

    return 0;
}