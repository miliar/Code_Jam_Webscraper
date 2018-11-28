#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
    int t;
    int n;
    string s;
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        cin>>n;
        cin>>s;
        int ans=0;
        int st=0;
        for (int i=0;i<=n;i++)
        {
            if (st<i)
            {
                ans=ans+i-st;
                st=i+s[i]-'0';
            }
            else
                st=st+s[i]-'0';
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
