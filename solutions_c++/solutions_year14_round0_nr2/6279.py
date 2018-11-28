#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
double c;
double f;
double add;
int t;
double x;
double ans;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out4.txt","w",stdout);
    int cas = 1;
    cin>>t;
    while(t--)
    {
        cin>>c>>f>>x;
        add = 2;
        ans = 0;
        while(1)
        {
            if(x/add>(c/add+x/(add+f)))
            {
                ans+=c/add;
                add+=f;
            }
            else
                break;
        }
        ans+=x/add;
        printf("Case #%d: %.6lf\n",cas++,ans);
    }
    return 0;
}
