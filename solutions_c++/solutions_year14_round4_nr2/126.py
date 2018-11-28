//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
const int N = 1003;

int t;
int n;
int tab[N];

int main()
{
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
        scanf("%d", &n);
        for(int i = 1;i <= n;i++)
            scanf("%d", &tab[i]);
        int wyn = 0;
        for(int i = 1;i <= n;i++)
        {
            int lewo = 0, prawo = 0;
            for(int j = 1;j < i;j++)
                if(tab[j] > tab[i])
                    lewo++;
            for(int j = i+1;j <= n;j++)
                if(tab[j] > tab[i])
                    prawo++;
            wyn += min(lewo, prawo);
        }
        printf("Case #%d: %d\n", ti, wyn);
    }
    return 0;
}
