#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int test=1;test<=t;test++)
    {
        int k,c,s;
        cin >> k >> c >> s;
        cout << "Case #" << test << ": ";
        for(int i=1;i<=k-1;i++) cout << i << " ";
        cout << k << endl;
    }
    return 0;
}
