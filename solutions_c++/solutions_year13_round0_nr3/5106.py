#include <cstdio>
#include <vector>

using namespace std;

vector<long long> specials;

bool is_palindrome(long long n) {
    long long t = n, reverse = 0;
    while(t > 0) {
        reverse = reverse * 10 + t % 10;
        t /= 10;
    }
    return reverse == n;
}

int main() {
    for(long long i = 1; i <= 10000000; ++i) {
        long long k = i * i;
        if(is_palindrome(i) && is_palindrome(k)) {
            specials.push_back(k);
        }
    }
    int num_tests = 0;
    scanf("%d", &num_tests);
    for(int test = 0; test < num_tests; ++test) {
        long long A,B;
        scanf("%lld %lld", &A, &B);
        int sol = 0;
        for(int i = 0; i <= (int)specials.size(); ++i) {
            if(specials[i] >= A && specials[i] <= B) ++sol;
        }
        printf("Case #%d: %d\n", test+1, sol);
    }
    return 0;
}
