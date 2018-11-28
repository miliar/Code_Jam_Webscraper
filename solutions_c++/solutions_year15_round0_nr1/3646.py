#include <iostream>
#include <cstdio>

using namespace std;

int proceed()
{
    int ans = 0, num = 0, am = 0;
    cin >> ans;
    ans = 0;
    getchar();
    while (cin.peek() != '\n')
        ans = max(ans, num - am), num++, am += getchar() - '0';
    getchar();
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
//    getchar();
    for (int i = 0; i < t; ++i)
        cout << "\nCase #" << i + 1 << ": " << proceed();
    return 0;
}
