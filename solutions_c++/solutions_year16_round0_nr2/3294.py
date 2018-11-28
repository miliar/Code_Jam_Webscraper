#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int T,n,kase = 0;
char a[105];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> T;
    while (T--)
    {
        scanf("%s", a);
        n = strlen(a);
        int i = n-1, cnt = 0;
        char t = '+';
        while (i >= 0)
        {
            while (i > 0 && a[i] == t)
                i--;
            if (a[i] == t) break;
            if (t == '+') t = '-'; else t = '+';
            cnt ++;
        }
        printf("Case #%d: %d\n", ++kase, cnt);
    }
    return 0;
    fclose(stdin);
    fclose(stdout);
}
