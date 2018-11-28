#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
using namespace std;

int T;
string x;
string ans;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-output.txt","w",stdout);

    cin >> T;
    for(int i=1;i<=T;i++)
    {
        cin >> x;
        ans = "";
        for(int j=0;j<x.length();j++)
        {
            if( ans == "" || x[j] < ans[0] )
                ans = ans + x[j];
            else
                ans = x[j] + ans;
        }
        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}
