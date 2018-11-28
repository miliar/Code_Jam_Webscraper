#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <set>

using namespace std;

int main() {
    int t;
    long long n;
    long long aux;
    long long prev_aux;
    bool flag = false;
    set<int> s;

    scanf("%d", &t);
    for(int i = 0; i < t; ++i) {
        scanf("%lld", &n);
        prev_aux = -1;

        for(int j = 1; j < INT_MAX; ++j) {
            aux = j * n;

            if(prev_aux == aux) {
                printf("Case #%d: INSOMNIA\n", i + 1);
                flag = true;
                break;
            }

            while(aux) {
                s.insert(aux % 10);
                aux /= 10;
            }

            if(s.size() == 10) {
                printf("Case #%d: %lld\n", i + 1, n * j);
                flag = true;
                break;
            }

            prev_aux = aux;
        }

        if(flag == false) {
            printf("Case #%d: INSOMNIA\n", i + 1);
        }

        s.clear();
    }

    return 0;
}
