#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <map>
#include <list>
#include<set>
#define sz 1010
#define pb(a) push_back(a)
#define pp pop_back()
#define ll long long
#define l long
#define fread freopen("input.in","r",stdin)
#define fwrite freopen("output.out","w",stdout)
#define inf (1<<30-1)
#define clr(abc,z) memset(abc,z,sizeof(abc))
#define PI acos(-1)
using namespace std;
int main()
{
    fread;
    fwrite;
    int t,n,deceit_war,war,mx;
    double a[sz],b[sz];
    bool flg[sz];
    cin>>t;
    for(int cas=1; cas<=t; cas++)
    {
        clr(a,0.0);
        clr(b,0.0);
        clr(flg,false);
        deceit_war=0;
        war=0;
        cin>>n;
        for(int i=1; i<=n; i++)
        {
            cin>>a[i];
        }
        sort(a+1,a+n+1);
        for(int i=1; i<=n; i++)
        {
            cin>>b[i];
        }
        sort(b+1,b+n+1);
        for(int i=1;i<=n;i++)
        {
            for(int j=i;j<=n;j++)
            {
                if(flg[j]==false&& a[i]<b[j])
                {
                    flg[j]=true;
                    war++;
                    break;
                }
            }
            //cout<<a[i]<<" "<<b[i]<<endl;
        }
        clr(flg,false);
        for(int i=n;i>=1;i--)
        {
            for(int j=n;j>=1;j--)
            {
                if(flg[j]==false&& a[i]>b[j])
                {
                    //cout<<a[i]<<" "<<b[j]<<endl;
                    flg[j]=true;
                    deceit_war++;
                    break;
                }
            }
            //cout<<a[i]<<" "<<b[n-i+1]<<endl;
        }
        cout<<"Case #"<<cas<<": "<<deceit_war<<" "<<n-war<<endl;
    }
    return 0;
}
/*
input:

4
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458

output:

Case #1: 0 0
Case #2: 1 0
Case #3: 2 1
Case #4: 8 4
*/
