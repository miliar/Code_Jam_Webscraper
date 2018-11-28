#include <bits/stdc++.h>
using namespace std;
#define MAX 50009
#define ll long long

char arr[1005];
int fn(int l);

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int tc, cases = 1;
    scanf("%d", &tc);

    while(tc--)
    {
        int length, k, s;
        scanf("%s", arr);

        int l = strlen(arr);

        int ans = fn(l);

        printf("Case #%d: %d", cases++, ans);

        printf("\n");
    }
    return 0;
}

int fn(int l)
{
    int ret = 0;
    bool flag = 0;

    for(int i = l - 1; i >= 0; i--)
    {
        if((arr[i] == '-' && flag == 0) || (arr[i] == '+' && flag == 1))
            ret++, flag = !flag;
    }

    return ret;
}
