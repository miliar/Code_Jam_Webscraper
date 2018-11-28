#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int test,n,m;
int t[101][101];
int w[109], kol[109];
bool no;

int main()
{
    scanf ("%d", &test);
    for (int k=1; k<=test; k++)
    {
        no = false;
        
        scanf ("%d%d", &n,&m);
        for (int i=1; i<=n; i++)
            for (int j=1; j<=m; j++)
                scanf ("%d", &t[i][j]);
        
        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=m; j++)
            {
                w[i] = max (w[i], t[i][j]);
                kol[j] = max (kol[j], t[i][j]); 
            }
        }
        
        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=m; j++)
            {
                if (t[i][j] >= w[i] || t[i][j] >= kol[j])
                    continue;
                else
                    no = true;
            }
        }
        
        if (no == true)
            printf ("Case #%d: NO\n", k);
        else
            printf ("Case #%d: YES\n", k);
            
        for (int i=1; i<=n; i++)
            w[i] = 0;
            
        for (int j=1; j<=m; j++)
            kol[j] = 0;
    }
    
cin.ignore(2);
return 0;
}
