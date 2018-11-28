#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <cmath>
#include <cstdlib>
using namespace std;

#define foreach(i, c) for (__typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)

char str[110];
int n;
int a[110];

void work()
{
    memset(a, 0, sizeof(a));
    scanf("%s", str);    
    scanf("%d", &n);
    int l = strlen(str);

    for (int i = 0;i<l;i++)
    {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u')
        {
            a[i] = 0;
        }
        else
            a[i] = 1;
    }

    int res = 0;
    for (int i = 0;i<l;i++)
    {
        for (int j = i+1; j<=l;j++)
        {
            int count = 0;
            int flag = 0;
            for (int k = i; k<j;k++)
            {
                if (a[k] == 1)
                    count ++;
                else
                    count = 0;

                if (count >= n)
                    flag = 1;
            }
            if (flag)
                res ++;
        }
    }

    printf("%d\n", res);
}
 
int main()
{
    // freopen("A-small-practice.in", "r", stdin);
    // freopen("A-large-practice.in", "r", stdin);    
    freopen("a.in", "r", stdin);
    freopen("out.txt", "w", stdout);
 
    int t;
    scanf("%d", &t);
    for (int cs = 1; cs <= t; cs++)
    {
        printf("Case #%d: ", cs);
        work();
    }
 
    return 0;
}