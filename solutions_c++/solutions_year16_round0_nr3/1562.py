#include <bits/stdc++.h>

using namespace std;

long long check_prime(__int128 n) {
    for (__int128 i = 2; i < 1000 && i * i <= n; i++) {
        if (n % i == 0) {
            return i;
        }
    }
    return 0;
}

int main() {
    long long n = 32, J = 500, cnt = 0;
    cout << "Case #1:\n";
    for (long long i = (1LL << (n - 1)) + 1; i < (1LL << n); i+=2) {
        long long num = i;
        if (cnt == J) break;
        vector <long long> lst(n, 0);
        vector <long long> answer;
        for (long long j = 0; j < n; j++) {
            lst[j] = (num >> j) & 1LL; 
        }
        std::reverse(lst.begin(), lst.end());
        for (__int128 j = 2; j <= 10; j++) {
            __int128 a = 0;
            for (int z = 0; z < n; z++)
                a = a * j + lst[z];
            long long res = check_prime(a);
            if (!res) break;
            answer.push_back(res);
        }
        if (answer.size() != 9) continue;
        cnt++;
        for (int j = 0; j < n; j++) cout << lst[j];
        cout << ' ';
        for (int j = 0; j < 9; j++) {
            cout << answer[j] <<  ' ';
        }
        cout << '\n';
    }
    return 0;
}
