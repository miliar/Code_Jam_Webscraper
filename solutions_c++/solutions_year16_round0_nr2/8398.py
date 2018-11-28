#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

int main() {
#ifndef ONLINE_JUDGE
    // freopen("a.txt", "r", stdin);
    freopen("bbb.in","r",stdin);
    freopen("ans.txt", "w", stdout);
#endif
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout << "Case #" << i << ": ";
        string s;
        cin>>s;
        PII prev, curr;
        if(s[0] == '+')
            prev = make_pair(0,1);
        else
            prev = make_pair(1,0);
        for(int j=1;j<s.length();j++)
        {
            if(s[j] == '+')
                curr = make_pair(prev.first, min(prev.first+1, prev.second+2));
            else
                curr = make_pair(min(prev.first+2, prev.second+1), prev.second);
            prev = curr;
        }
        cout << prev.first << endl;
    }
    return 0;
}
