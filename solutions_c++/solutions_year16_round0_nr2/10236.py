#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        string s;
        cin>>s;
        printf("Case #%d: ", t);
        int c = 1;
        bool last;
        if (s[0] == '+')
        {
            last = true;
        }
        else
        {
            last = false;
        }
        for (int i = 1; i < s.length(); ++i)
        {
            if (s[i] == '-' && last)
            {
                ++c;
                last = false;
            }
            else if (s[i] == '+' && !last)
            {
                ++c;
                last = true;
            }
        }
        if (last == true)
        {
            --c;
        }
        printf("%d\n", c);
    }
    return 0;
}
