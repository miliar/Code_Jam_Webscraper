#include <cstdio>
#include <cstring>
int kase;
char str[105];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &kase);
    for (int cas=1; cas<=kase; cas++) {
        memset(str, 0, sizeof(str));
        scanf("%s", str);
        int len=strlen(str), res=0;
        bool flag=false;
        for (int i=0; i<len; i++) {
            if (str[i]=='-'&&flag) {
                res+=2;
                flag=false;
            } else if (str[i]=='+'&&!flag)
                flag=true;
        }
        if (str[0]=='-')
            res++;
        printf("Case #%d: %d\n", cas, res);
    }
    return 0;
}
