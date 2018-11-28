#include <bits/stdc++.h>
using namespace std;
#define SD(a) scanf("%d", &a)

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("outputlarge.txt", "w", stdout);
    int tcase, t, i, len;
    SD(tcase);
    string in, str;
    for(t = 1; t <= tcase; t++)
    {
        cin >> in;
        len = in.length();
        str = "";
        for(i = 0; i < len; )
        {
            str += in[i];
            i++;
            while(i < len)
            {
                if(in[i] == in[i-1]) i++;
                else break;
            }
        }
        len = str.length();
        if(str[len - 1] == '+') len--;
        printf("Case #%d: %d\n", t, len);

    }
    return 0;
}
