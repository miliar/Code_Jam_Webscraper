#include <iostream>
#include <cstdio>

using namespace std;

bool get_flag(bool arr[10]) {
    for (int i=0; i<10; i++) {
        if (arr[i] == false)
            return false;
    }
    return true;
}

void set_digit(unsigned long long n, bool arr[10]) {
    int d;
    while (n!=0) {
        d = n%10;
        arr[d] = true;
        n = n/10;
    }
}

int main(void) {
    unsigned long long N, num;
    int T;
    bool visited[10], flag;
    scanf("%d", &T);
    for (int i=1; i<=T; i++) {
        scanf("%llu", &N);
        if (N > 0) {
            num = 0;
            for (int j=0; j<10; j++)
                visited[j] = false;
            flag = false;
            while (flag==false) {
                num += N;
                set_digit(num, visited);
                flag = get_flag(visited);
            }
            printf ("Case #%d: %llu\n", i, num);
        }
        else {
            printf ("Case #%d: INSOMNIA\n", i);
        }
    }
    return 0;
}
