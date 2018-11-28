#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    string s;

    for (int tc = 1; tc <= t; tc++) {
        printf("Case #%d: ", tc);

        cin >> s;

        int sol = 0;

        for (int i = s.size()-1; i >= 0; i--)
            if (s[i] == '-' && sol % 2 == 0)
                sol++;
            else if (s[i] == '+' && sol % 2 == 1)
                sol++;

        printf("%d\n", sol);
    }
    return 0;
}

