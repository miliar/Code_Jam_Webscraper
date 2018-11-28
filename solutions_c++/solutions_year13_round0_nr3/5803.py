#include <iostream>
#include <cstdio>

using namespace std;


bool r(char a, char b, char c, char d, char e) {
    return ((a == b) && (b == c) && (c == d) && (d == e));
}
int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    int a, b;
    int ans;
    for (int i = 0; i < t; ++i) {
        ans = 0;
        cin >> a >> b;
        if (a <= 1) ++ans;
        if ((a <= 4) && (4 <= b)) ++ans;
        if ((a <= 9) && (9 <= b)) ++ans;
        if ((a <= 121) && (121 <= b)) ++ans;
        if ((a <= 484) && (484 <= b)) ++ans;
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
