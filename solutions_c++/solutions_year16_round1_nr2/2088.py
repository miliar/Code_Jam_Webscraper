#include <stdio.h>
#include <set>

int t;
int n;
std :: set <int> S;

int main()
{
    freopen("/Users/IohcEjnim/Downloads/B-large.in.txt", "r", stdin);
    freopen("/Users/IohcEjnim/Downloads/result.txt", "w", stdout);
    int tn, i, j, tmp;
    
    scanf("%d", &t);
    
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%d", &n);
        for (i = 1; i < 2*n; i++)
            for (j = 1; j <= n; j++)
            {
                scanf("%d", &tmp);
                if (S.find(tmp) != S.end()) S.erase(tmp);
                else S.insert(tmp);
            }
        
        printf("Case #%d: ", tn);
        while (!S.empty())
        {
            printf("%d ", *S.begin());
            S.erase(S.begin());
        }
        puts("");
    }
}