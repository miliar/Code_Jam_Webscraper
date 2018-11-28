#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int cnt_cases;
    scanf("%d", &cnt_cases);
    for (int current_case = 1; current_case <= cnt_cases; current_case++)
    {
        string str, out = "0";
        cin >> str;
        out[0] = str[0];
        for (int i = 1; i < str.length(); i++)
        {
            if (str[i] >= out[0])
                out = str[i] + out;
            else
                out = out + str[i];
        }
        printf("Case #%d: %s\n", current_case, out.c_str());
    }
    return 0;
}
