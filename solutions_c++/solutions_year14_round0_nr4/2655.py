#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;
int n;
int aux, a[1010], b[1010];

void cit()
{
    scanf("%d", &n);
    for (int i=0; i<n; i++)
        scanf("%d.%d", &aux, &a[i]);
    for (int i=0; i<n; i++)
        scanf("%d.%d", &aux, &b[i]);
}

void sol()
{
    int i, j;
    int w1, w2;
    sort(a, a+n);
    sort(b, b+n);
    /// 2, war normal
    w2=0;
    i=j=0;
    while (i<n && j<n)
    {
        while (a[i]>b[j] && j<n)
        {
            j++;
            w2++;
        }
        i++;
        j++;
    }
    /// 1, war deceipt
    w1=0;
    i=j=0;
    int m=n;
    while (i<n && j<m)
    {
        if (a[i]<b[j])
            while (a[i]<b[j] && m>0)
            {
                m--;
                i++;
            }
        else
        {
            w1++;
            i++;
            j++;
        }
    }
    printf("%d %d", w1, w2);
}

int main()
{
    freopen("war.in", "r", stdin);
    freopen("war.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int r=1; r<=T; r++)
    {
        printf("Case #%d: ", r);
        cit();
        sol();
        printf("\n");
    }
    return 0;
}
