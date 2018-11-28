#include <bits/stdc++.h>
using namespace std;

int main()
{
    char s[1000];
    int test, t=0;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &test);
    while (test--)
    {
        scanf("%s", s);
        int l = strlen(s);


        int cnt = 0;
        for (int i=0, prev = 0 ; i<l ; )
        {
            if (s[i] == '-')
            {
                while (s[i] == '-' && i<l) i++;
                cnt++;
                cnt += prev;
                prev = 0;
            }
            else
            {
                while (s[i] == '+' && i<l) i++;
                prev = 1;
            }
        }

        printf("Case #%d: %d\n", ++t, cnt);
    }
    return 0;
}
