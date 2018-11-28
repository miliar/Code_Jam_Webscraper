#include <iostream>
#include <set>
#include <cstdlib>
#include <string>

//#define __OJ__
using namespace std;

int countSheep(int N) {
    set<int> S;
    set<int> Digit;
    int i = 1;
    int digit;
    int number = N;
    while (!S.count(number)) {
        while (number > 0) {
            digit = number % 10;
            number /= 10;
            if (!Digit.count(digit)) {
                Digit.insert(digit);
            }
        }
        if (Digit.size() == 10)
            return (i * N);
        S.insert(i * N);
        i++;
        number = i * N;
    }
    return -1;
}

int main() {
#ifdef __OJ__
    freopen("//Users//jiahuiguo//GitHub//Problems//GoogleCodeJam//A-large.in", "r", stdin);
    freopen("//Users//jiahuiguo//GitHub//Problems//GoogleCodeJam//A-large.out", "w", stdout);
#endif
    int T;
    scanf ("%d", &T);
    int N;
    for (int i = 0; i < T; i++) {
        scanf("%d\n", &N);
        int result = countSheep(N);
        if (result == -1)
            printf("Case #%d: %s\r\n", i + 1, "INSOMNIA");
        else
            printf("Case #%d: %d\r\n", i + 1, result);
    }
}
