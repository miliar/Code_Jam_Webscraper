#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <set>
#include <utility>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        int n, x;
        cin >> n >> x;
        
        multiset<int, greater<int>> s;
        
        for(int i = 0; i < n; ++i)
        {
            int a;
            cin >> a;
            
            s.insert(a);
        }
        
        int ans = 0;
        int cap = 0;
        
        // cout << x << endl;        
        for(auto it = s.begin(); it != s.end();)
        {
            ++ans;
            cap = x - *it;
            
            // cout << *it;
            
            s.erase(it++);
            
            if(it == s.end())
                break;
                
            auto cit = s.lower_bound(cap);
            if(cit != s.end())
            {
                // cout << ' ' << *cit;
                if(cit == it)
                    s.erase(it++);
                else
                    s.erase(cit);
            }
            // cout << endl;
        }
        
        cout << "Case #" << t << ": " << ans << '\n';
            
    }
    return 0;
}
