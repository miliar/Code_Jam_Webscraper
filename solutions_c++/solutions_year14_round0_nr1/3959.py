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
#define sz 100
#define pb(a) push_back(a)
#define pp pop_back()
#define ll long long
#define l long
#define fread freopen("input.in","r",stdin)
#define fwrite freopen("output.in","w",stdout)
#define inf (1<<30-1)
#define clr(abc,z) memset(abc,z,sizeof(abc))
#define PI acos(-1)
using namespace std;
int main()
{
    fread;
    fwrite;
    int t,r,a[18],x,c,ans;
    cin>>t;
    for(int ca=1; ca<=t; ca++)
    {
        c=0;
        ans=0;
        clr(a,0);
        cin>>r;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                cin>>x;
                if(i==r)
                {
                    a[x]=1;
                }
            }
        }
        cin>>r;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                cin>>x;
                if(i==r && a[x]==1)
                {
                    ans=x;
                    c++;
                }
            }
        }
        if(c==0)
        {
            cout<<"Case #"<<ca<<": "<<"Volunteer cheated!"<<endl;
        }
        else if(c==1)
        {
            cout<<"Case #"<<ca<<": "<<ans<<endl;
        }
        else
        {
            cout<<"Case #"<<ca<<": "<<"Bad magician!"<<endl;
        }
    }
    return 0;
}

