#include <iostream>
#include <cstdio>
using namespace std;
int testy,a,b,x;
int t[10001], tab[10001], sum[10001];
bool vis[100001], no, noo;

int main()
{
    scanf ("%d", &testy);
    for (int i=1; i<=100; i++)
        t[i] = i*i;
    
    for (int i=1; i<=100; i++)
    {
        x = t[i];
        int j = 1;
        while (x != 0)
        {
            tab[j] = x%10;
            x /= 10;
            j ++;
        }
        
        int b=j-1;
        no = false;
        noo = false;
        for (int j=1; j<=b; j++)
        {
            if (tab[j] != tab[b])
                no = true;
            b--;
        }
        
        x = i;
        j = 1;
        while (x != 0)
        {
            tab[j] = x%10;
            x /= 10;
            j ++;
        }
        
        b=j-1;
        noo = false;
        for (int j=1; j<=b; j++)
        {
            if (tab[j] != tab[b])
                noo = true;
            b--;
        }
        
        if (no == false && noo == false)
            vis[t[i]] = true;
    }
    
    for (int i=1; i<=10000; i++)
        sum[i] += sum[i-1] + vis[i];
        
    for (int i=1; i<=testy; i++)
    {
        scanf ("%d%d", &a,&b);
        printf ("Case #%d: %d\n", i, sum[b] - sum[a-1]); 
    }

cin.ignore(2);
return 0;
}
