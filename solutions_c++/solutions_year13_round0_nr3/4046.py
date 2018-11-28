//
//  main.cpp
//  TestCppCode
//

#include <iostream>
#include <list>
#include <map>
#include <cmath>
#include <vector>
using namespace std;

bool is_palindrome(long long n) {
    int len = (int)log10(n) + 1;
    char num[len];
    sprintf(num, "%lld", n);
    int mid = len>>1;
    for (int i=0; i<mid; i++) {
        if (num[i] != num[len-1-i]) {
            return false;
        }
    }
    return true;
}
//int next_palindrome(int n) {
//    int len = (int)log10(n) + 1;
//    char num[len];
//    sprintf(num, "%d", n);
//}
int main() {
    long long L = 100000000000000LL;
    int limit = (int)sqrt(L) + 1;
    vector<long long> nlist;
    for (int n = 1; n <= limit; n++) {
        long long sq = (long long)n * n;
        if (sq <= L && is_palindrome(n) && is_palindrome(sq)) {
            nlist.push_back(sq);
        }
    }
    //for (vector<long long>::iterator it = nlist.begin(); it != nlist.end(); it++) printf("%lld ", *it);
    //printf("\n[%d]\n", (int)nlist.size());

    int tc; scanf("%d", &tc);
    for (int test = 1; test <= tc; test++) {
        long long A, B; scanf("%lld%lld", &A, &B);
        int lower = 0;
        int upper = (int)nlist.size() - 1;
        for (vector<long long>::iterator it = nlist.begin(); it != nlist.end(); it++, lower++) {
            if (*it >= A) break;
        }
        for (vector<long long>::reverse_iterator it = nlist.rbegin(); it != nlist.rend(); it++, upper--) {
            if (*it <= B) break;
        }
        printf("Case #%d: %d\n", test, upper - lower + 1);
    }
}