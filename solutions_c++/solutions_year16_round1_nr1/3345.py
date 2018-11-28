#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    char s[1010];
    int test, t=0;
    scanf("%d", &test);

    while (test--)
    {
        scanf("%s", s);

        char bgn = s[0], ed = s[0];
        list<char>lst;

        for (int i=0 ; s[i] ; i++)
        {
            if (!i) lst.push_back(s[i]);
            else
            {
                if (s[i] >= bgn) lst.push_front(s[i]), bgn = s[i];
                else lst.push_back(s[i]), ed = s[i];
            }
        }

        printf("Case #%d: ", ++t);
        for (list<char>::iterator it = lst.begin() ; it != lst.end() ; it++)
            printf("%c", *it);
        puts("");
    }
    return 0;
}
