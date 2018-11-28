#include <bits/stdc++.h>
using namespace std;
#define MAX 50009
#define ll long long

int fn();
int get(int num);


string numbers [] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int c[]={0,2,6,8,7,5,4,9,3,1};
int ans[MAX], array[50];
char input[MAX];

int main()
{
    freopen("A-large (1).in", "r", stdin);
    freopen("c.out", "w", stdout);
    int cases = 1, tc;
    scanf("%d", &tc);
    while(tc--)
    {
        memset(array, 0, sizeof(array));
        scanf("%s", input);

        for(int i = 0; i < strlen(input); i++)
            array[input[i] - 'A']++;

        int ret = fn();
        sort(ans, ans + ret);

        printf("Case #%d: ", cases++);
        for(int i = 0; i < ret; i++)
            printf("%d", ans[i]);
        printf("\n");
    }

    return 0;
}

int fn()
{
    int x = 0;

    for(int i = 0; i <= 9; i++)
        while(1)
        {
            int tmp = get(c[i]);
            if(tmp)
                ans[x++] = c[i];
            else break;
        }

    return x;
}

int get(int num)
{
    string x = numbers[num];
    int cnt[30];
    memset(cnt, 0, sizeof(cnt));

    for(int i = 0; i < x.length(); i++)
        cnt[x[i] - 'A']++;

    for(int i = 0; i < 30; i++)
        if(array[i] < cnt[i])
            return 0;

    for(int i = 0; i < 30; i++)
        array[i] -= cnt[i];

    return 1;
}
