#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;
int ans = 999999999;
void solve(int pan[], int t)
{
    int m = 0, temp[10];
    for(int i = 9; i >= 1; i--)
        if(pan[i] != 0)
        {
            m = i;
            break;
        }
    ans = min(ans, t + m);
    if(m <= 3)
        return;
    for(int i = 0; i < 10; i++)
        temp[i] = pan[i];
    for(int i = 2; i <= m/2; i++)
    {
        pan[m]--;
        pan[m-i]++;
        pan[i]++;
        solve(pan, t+1);
        for(int i = 0; i < 10; i++)
            pan[i] = temp[i];
    }
}
int main()
{
    freopen("stuff.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, d, p, pan[10] = {0};
    cin >> t;
    for(int i = 0; i < t; i++)
    {
        fill(pan, pan + 10, 0);
        cin >> d;
        ans = 999999999;
        while(d--)
        {
            cin >> p;
            pan[p]++;
        }
        solve(pan, 0);
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
