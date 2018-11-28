#include <iostream>
#include <string>
// #include <vector>
#include <map>

using namespace std;

int reverse(long n) {
    long reverse = 0;
    while (n != 0) {
        reverse *= 10;
        reverse += n % 10;
        n /= 10;
    }
    return reverse;
}

// int solve(long n) {
//     // cout << n << endl;

//     if (n <= 20)
//         return n;

//     if (reverse(n) < 10)
//         return min(10 + solve(n - 9), 11 + solve(n - 10));

//     int count = 1;
//     int last = n % 10;
//     count += last;
//     n -= last;

//     long r = reverse(n);
//     if (r < 10) {
//         count--;
//         n++;
//         r = reverse(n);
//         if (r == n) {
//             // cout << "Count " << count << endl;
//             return min(count + 10 + solve(n - 11), count + 9 + solve(n - 10));
//         }
//     }

//     return count + solve(r);
// }

map<long, int> m;

// int solve(long n) {
//     if (m.count(n) != 0)
//         return m[n];

//     if (n <= 20)
//         return n;

//     long r = reverse(n);
//     int min = n;
//     if (r < n && r > 10)
//         min = solve(r);
//     for (int i = 1; i <= 11; i++) {
//         int res = 1 + i + solve(n - i);
//         if (res < min)
//             min = res;
//     }
//     m[n] = min;
//     cout << "Min for " << n << " is " << min << endl;
//     return min;
// }

void precompute() {
    for (long i = 1; i < 20; i++) {
        m[i] = (int) i;
    }
    for (long i = 20; i <= 1000000; i++) {
        long r = reverse(i);
        if (r >= i || reverse(r) != i)
            m[i] = 1 + m[i - 1];
        else
            m[i] = min(1 + m[i - 1], 1 + m[r]);
    }
}

int main() {
    int cases;
    cin >> cases;
    precompute();
    for (int i = 1; i <= cases; i++) {
        long n;
        cin >> n;

        cout << "Case #" << i << ": " << m[n] << endl;
    }
}
