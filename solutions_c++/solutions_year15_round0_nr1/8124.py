#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int c = 1; c <= t; ++c)
    {
        int n;
        string s;
        cin >> n >> s;
        
        int ans = 0, standing = 0;
        for (int i = 0; i < (int)s.size(); ++i)
        {
            if ((s[i] - '0') && i > standing)
            {
                ans += i - standing;
                standing += i - standing;
            }
            standing += s[i] - '0';
        }
        
        cout << "Case #" << c << ": " << ans << endl;
    }
    
    return 0;
}