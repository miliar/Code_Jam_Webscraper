#include <cstdio>
#include <map>

using namespace std;


bool isPalindrome(long int temp) {
    int j = 0, k;
    bool flag = true;
    int digits[100];
    while (temp != (long long int)0) {
        digits[j++] = temp % 10;
        temp = temp / 10;
    }
    for (k = 0; k <= (j / 2); k++) {
        if (digits[k] != digits[j-k-1]) {
            flag = false;
        }
    }
    return flag;
}

int main()
{

    long int table[100];
    int counttable = 0;
    long int square;
    for (long int i = 1; i < 10000000; i++) {
        if (isPalindrome(i)){
            square = i * i;
            if (isPalindrome(square)) {
                // printf("%ld*%ld = %ld\n", i, i, square);
                // printf("%ld\n", square);
                table[counttable++] = square;
            }
        }
    }
    int t;
    scanf("%d", &t);
    for (int n = 1; n <= t; n++) {
        long int a, b;
        int count = 0;
        scanf("%ld %ld\n", &a, &b);
        for (int i = 0; i < counttable; i++) {
            if (table[i] >= a && table[i] <= b) {
                count++;
            }
        }
        printf("Case #%d: %d\n", n, count);
    }

}
