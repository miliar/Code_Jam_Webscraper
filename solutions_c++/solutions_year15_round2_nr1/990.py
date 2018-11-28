#include <bits/stdc++.h>

#define maxN 1000005
#define maxC 1000000007

using namespace std;

long long reverse_num(long long n) {
    long long res = 0;
    while (n) {
        res = 10*res + n%10;
        n /= 10;
    }
    return res;
}

long long find_not_zero(long long n) {
    long long k = 0;
    bool zero = true;
    n /= 10;
    while (n > 9) {
        ++k;
        if (n%10 != 0) zero = false;
        n /= 10;
    }
    if (zero) return 1;
    long long res = 10;
    for (int i = 0; i < (k+1)/2; ++i) res *= 10;
    return res;
}

int first_num(long long n) {
    while (n > 9) {
        n /= 10;
    }
    return n;
}

long long find_res(long long n) {
    long long res = 0, k, r, m;
    while (n > 20) {
      // cout << n << " ";
       if (n % 10 == 1) {
            if (n/100 == 0) return (res + reverse_num(n) + 1);
            k = find_not_zero(n);
            if (k == 1) {
                m = reverse_num(n);
                if (m < n) {
                    ++res;
                    n = m;
                }
                else {
                    res += 10;
                    n -= 10;
                }
            }
            else {
                r = n%k;
                res += r;
                m = reverse_num(n - (r-1));
                if (n - (r-1) <= m) {
                    --res;
                    n = n - (r-1);
                }
                else n = m;
            }
       }
       else {
            k = (n%10 + 9) % 10;
            res += k;
            n -= k;
       }
    }
    res += n;
    return res;
}

int main() {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("outputb.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    int nTest;
    scanf("%d", &nTest);

    long long n;
    for (int iTest = 1; iTest <= nTest; ++iTest) {
        cin >> n;
        cout << "Case #" << iTest << ": " << find_res(n) << endl;
    }
    return 0;
}
