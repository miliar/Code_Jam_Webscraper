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
    int x,r,c;
    cin>>t;
    string ans;
    for (int i=1;i<=t;i++)
    {
        cin>>x>>r>>c;
        ans="";
        if (x==1) ans="GABRIEL";
        else if (x==2)
        {
            if (r%2==0 || c%2==0) ans="GABRIEL";
            else ans="RICHARD";
        }
        else if (x==3)
        {
            if (r==3 && c==3) ans="GABRIEL";
            else if (r==3 && c==4) ans="GABRIEL";
            else if (r==4 && c==3) ans="GABRIEL";
            else if (r==3 && c==2) ans="GABRIEL";
            else if (r==2 && c==3) ans="GABRIEL";
            else ans="RICHARD";
        }
        else if (x==4)
        {
            if (r==4 && c==4) ans="GABRIEL";
            else if (r==3 && c==4) ans="GABRIEL";
            else if (r==4 && c==3) ans="GABRIEL";
            else ans="RICHARD";
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
