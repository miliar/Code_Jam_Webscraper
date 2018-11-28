#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    int cnt_cases;
    scanf("%d", &cnt_cases);
    for (int current_case = 1; current_case <= cnt_cases; current_case++)
    {
        string s;
        cin >> s;
        int N = s.length();
        int operations = 0;

        if (N != 0 && s[0] == '-')
            operations++;

        for (int i = 1; i < N; i++)
        {
            if (s[i - 1] == '+' && s[i] == '-')
                operations += 2;
        }

        printf("Case #%d: %d\n", current_case, operations);
    }
    return 0;
}
