#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int t, smax;
string s;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a_out.txt", "w", stdout);
    
    cin >> t;
    
    for (int i = 0; i < t; i++)
    {
        cin >> smax;
        cin >> s;
        
        int cursum = 0;
        int ans = 0;
        for (int j = 0; j < smax + 1; j++)
        {
            if (j > cursum)
            {
                ans += j - cursum;
                cursum += j - cursum;
            }
            cursum += s[j] - '0';
        }
        
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    
    return 0;
            
}
