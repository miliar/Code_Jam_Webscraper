#include <bits/stdc++.h>
using namespace std;
bool used[10];
void use(int n)
{
    if(n == 0)
    {
        used[0] = 1;
        return;
    }
    while(n > 0)
    {
        used[n % 10] = 1;
        n /= 10;
    }
}
void solve(int t)
{
    for(int i = 0; i <= 9; i ++)
        used[i] = 0;
    int n;
    cin >> n;
    for(int i = 1; i <= 1000; i ++)
    {
        use(n * i);
        bool ok = 1;
        for(int i = 0; i <= 9; i ++)
            if(!used[i])
                ok = 0;
        if(ok)
        {
            cout << "case #" << t << ": " << n * i << endl;
            return;
        }
    }
    cout << "case #" << t << ": " << "INSOMNIA" << endl;
}
main()
{
    freopen("large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    int k = 1;
    while(k <= t)
    {
        solve(k);
        k ++;
    }
}
