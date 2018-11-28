#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

char s[20];
bool isPalindrom(long long a) {
    int m = 0;
    while (a) {
        s[m++] = a % 10;
        a /= 10;
    }

    bool res = true;
    for (int i = 0; i < m / 2; i++)
        res &= s[i] == s[m - 1 - i];

    return res;
}

long long d[100];

int main()
{
    int n = 0, t;
    for (long long i = 1; i <= 10000000; i++)
        if (isPalindrom(i) && isPalindrom(i * i)) d[n++] = i * i;

    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        long long a, b;
        cin >> a >> b;
        int l = 0, r = n - 1;
        while (d[l] < a) l++;
        while (d[r] > b) r--;
        cout << "Case #" << tc << ": " << r - l + 1 << endl;
    }

    return 0;
}
