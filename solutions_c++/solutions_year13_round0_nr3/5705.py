#include <iostream>
#include <cmath>
#include <algorithm>
#include <sstream>

using namespace std;

bool check(int num)
{
    stringstream ss;
    ss << num;
    string s2 = ss.str();
    
    reverse(s2.begin(), s2.end());
    if (ss.str() == s2)
        return true;
    else 
        return false;
}

int main()
{
    int n;
    
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int ans = 0;
        int a, b;

        cin >> a >> b;
        a = ceil(sqrt(a));
        b = floor(sqrt(b));
        
        for ( ; a <= b; a++) {
            if (check(a) && check(a * a))
                ans++;
        }
        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}
