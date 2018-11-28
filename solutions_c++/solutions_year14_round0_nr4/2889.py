#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>
using namespace std;

int n;
double a[1001], b[1001], a0[1001], b0[1001];

void init()
{
    cin >> n;
    for(int i = 1 ; i <= n ; i++)
        cin >> a[i];
    for(int i = 1 ; i <= n ; i++)
        cin >> b[i];
}

void work()
{
    sort(a + 1, a + n + 1);
    sort(b + 1, b + n + 1);
    int s1 = 0, s2 = 0;
    /*for(int i = 1 ; i <= n ; i++)
        cout << a[i] << ' ';
    cout << endl;
    for(int i = 1 ; i <= n ; i++)
        cout << b[i] << ' ';
    cout << endl;*/
    memcpy(a0, b, sizeof(b));
    memcpy(b0, a, sizeof(a));
    
    b0[0] = -1;
    for(int i = 1 ; i <= n ; i++)
    {
        int j = n;
        for(j = n ; j >= 1 ; j--)
        if(b0[j] > a0[i] && b0[j - 1] < a0[i])
            break;
        if(j >= 1)
        {
            b0[j] = -1;
            s1++;
        }
        else
        {
            for(j = 1 ; j <= n ; j++)
                if(b0[j] > 0) break;
            b0[j] = -1;
           
        }
        sort(b0 + 1, b0 + n + 1);
    }
    
    b[0] = -1;
    for(int i = 1 ; i <= n ; i++)
    {
        int j = n;
        for(j = n ; j >= 1 ; j--)
        if(b[j] > a[i] && b[j - 1] < a[i])
            break;
        if(j >= 1)
        {
            b[j] = -1;
        
        }
        else
        {
            for(j = 1 ; j <= n ; j++)
                if(b[j] > 0) break;
            b[j] = -1;
            s2++;
        }
        sort(b + 1, b + n + 1);
    }
    cout << s1 << ' ' << s2 << endl;
}
                

int main()
{
    freopen("qd.in", "r", stdin);
    freopen("qd.out", "w", stdout);
    int tt;
    cin >> tt;
    for(int i = 1 ; i <= tt ; i++)
    {
        cout << "Case #" << i << ": ";
        init();
        work();
    }
    return 0;
}
