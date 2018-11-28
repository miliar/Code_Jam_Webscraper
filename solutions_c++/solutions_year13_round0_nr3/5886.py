#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>

using namespace std;

bool IsPalindrome(long long n) {
    vector<int> digits;
    while (n > 0) {
        digits.push_back(n % 10);
        n /= 10;
    }
    for (int i = 0, j = digits.size() - 1; i < j; i++, j--) {
        if (digits[i] != digits[j]) {
            return false;
        }
    }
    return true;
}

bool IsSuqare(int n) {
    int r = sqrt(n);
    return n == r * r && IsPalindrome(r);
}

int main()
{
    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    int cs = 1;
    while (T--) {
        int A, B;
        scanf("%d%d", &A, &B);
        int cnt = 0;
        for (int i = A; i <= B; ++i) {
            if (IsPalindrome(i) && IsSuqare(i)) {
                cnt++;
                //printf("%d..\n", i);
            }
        }
        printf("Case #%d: %d\n", cs++, cnt);
    }

    /*for (long long i = 1; i < 0x7ffff; ++i) {
        if (IsPalindrome(i * i)) {
            printf("%lld %lld\n", i, i * i);
            //cout << i << " : " << i*i <<endl;
        }
    }
    cout << "Hello world!" << endl;*/
    return 0;
}
