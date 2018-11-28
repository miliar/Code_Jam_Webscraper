#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>

#define LL long long
#define VLL vector<LL>

#define NMAX 10000000LL

using namespace std;

int test_count;
LL a, b;
VLL data;

bool isPalindrome(const LL num) {
    LL rev = 0;
    LL tmp = num;
    while (tmp != 0){
        rev = rev * 10LL + tmp % 10LL;
        tmp /= 10LL;
    }
    return rev == num;
}

bool test(const LL num) {
    return isPalindrome(num) && isPalindrome(num * num);
}

void prepare() {
    for (LL i=1; i <= NMAX; i++) {
        if (test(i)) {
            data.push_back(i * i);
        }
    }
}

int query(const LL a, const LL b) {
    return upper_bound(data.begin(), data.end(), b) - lower_bound(data.begin(), data.end(), a);
}

int main(int argc, char *argv[]) {
    scanf("%d", &test_count);
    prepare();
    //cout << "All " << data.size() << " elements:" << endl;
    //for (VLL::iterator it=data.begin(); it != data.end(); it++) {
    //    cout << "   " << *it << endl;
    //}
    for (int t=0; t < test_count; t++) {
        scanf("%lld%lld", &a, &b);
        cout << "Case #" << (t + 1) << ": " << query(a, b) << endl;
    }
    return 0;
}
