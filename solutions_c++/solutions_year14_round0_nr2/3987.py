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
#define fwrite freopen("output.out","w",stdout)
#define inf (1<<30-1)
#define clr(abc,z) memset(abc,z,sizeof(abc))
#define PI acos(-1)
using namespace std;
int main()
{
    fread;
    fwrite;
    int t;
    double c,f,x,ans=0,cookie,rate,mn;
    cin>>t;
    for(int ca=1; ca<=t; ca++)
    {
        ans=0.0;
        cookie=0.0;
        rate=2.0;
        cin>>c>>f>>x;
        if(c>=x)
        {
            ans=x/rate;
        }
        else
        {
            mn=x/rate;
            while(1)
            {
                ans+=(c/rate);
                rate+=f;
                if((ans+(x/rate))<mn)
                {
                    mn=ans+(x/rate);
                }
                else break;
            }
            ans=mn;
        }
        printf("Case #%d: %.7lf\n",ca,ans);
    }
    return 0;
}
