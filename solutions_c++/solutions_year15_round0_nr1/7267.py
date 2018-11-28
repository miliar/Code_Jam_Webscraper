#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long ll;


int main()
{
    int t;
    cin >> t;
    
    for(int tt=1;tt<=t;tt++)
    {
        int smax;
        cin >> smax;
        
        string s;
        cin >> s;
        
        int now = s[0]-'0',cnt=0;
        for(int i=1;i<s.size();i++)
        {
            if(s[i]=='0')continue;
            if(now<i)
            {
                cnt += (i-now);
                now = i;
            }
            now += (s[i]-'0');
        }
        
        cout << "Case #" << tt <<": " << cnt << "\n";
    }
    return 0;
}