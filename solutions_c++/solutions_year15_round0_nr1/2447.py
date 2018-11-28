#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("output.txt", "w",stdout);
    int t;
    cin >> t;
    for (int q=0;q<t;q++)
    {
        int s1;
        string s;
        cin >> s1 >> s;
        int count=0,ans=0;
        count +=s[0]-48;
        for (int i=1;i<s.length();i++)
        {
            if (count<i){ans+=i-count;count=i;}
            count+=s[i] - 48;
        }
        cout << "Case #" << q+1 << ": " << ans << endl;
    }
    return 0;
}
