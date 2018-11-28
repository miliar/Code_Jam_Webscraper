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

int a[1001];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
    int t;
    int n;
    cin>>t;
    //string ans;
    for (int i=1;i<=t;i++)
    {
        cin>>n;
        for (int j=1;j<=n;j++)
        {
            cin>>a[j];
        }
        int ans1=0;
        int ans2=0;
        int cur=a[1];
        for (int j=2;j<=n;j++)
        {
            if (cur>=a[j])
            {
                ans1=ans1+cur-a[j];
            }
            cur=a[j];
        }
        int ma=0;
        for (int j=1;j<=n-1;j++)
        {
            ma=max(ma,a[j]-a[j+1]);
        }
        cur=a[1];
        for (int j=2;j<=n;j++)
        {
            if (cur<=ma) ans2=ans2+cur; else ans2=ans2+ma;
            cur=a[j];
        }
        cout<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}
