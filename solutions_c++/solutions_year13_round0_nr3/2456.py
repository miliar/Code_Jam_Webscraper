#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

int T;
long long A, B;
vector <long long> s;

bool check(long long n) {
    char str[100];
    memset(str, '\0', sizeof(str));
    sprintf(str, "%lld", n);
    int len =strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - i - 1]) return false;
    }
    return true;
}


int main()
{
    freopen("C-large-1.in", "r", stdin);
    freopen("test.out", "w", stdout);
    scanf("%d", &T);
    for (long long i = 0; i <= 10000000; i++) {
        if (check(i) && check(i * i)) {
            s.push_back(i * i);
        }
    }
    for (int cas = 1; cas <= T; cas++) {
        cin >> A >> B;
        int ans = upper_bound(s.begin(), s.end(), B) - upper_bound(s.begin(), s.end(), A - 1);
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
