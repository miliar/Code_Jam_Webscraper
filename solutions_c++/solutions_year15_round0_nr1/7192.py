/*
 *
 *    File Name: 
 *    Created By: r3gz3n
 *    Description: 
 *
 *
 */

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, smax, sum, ans;
    char c;
    cin >> t;
    for(int i = 1;i <= t;++i)
    {
        cin >> smax;
        sum = 0;
        ans = 0;
        for(int j = 0;j <= smax;++j)
        {
            cin >> c;
            if(sum < j)
                ans += (j - sum), sum = j;
            sum += (c - '0');
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}