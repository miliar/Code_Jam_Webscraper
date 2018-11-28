#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cctype>
#define ll long long
#define ld long double
#define sqr(a) (a)*(a)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define inf (int)1e9
using namespace std;
ld c,f,x,p=2,ans;
int t;
int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
    freopen("B-large.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>t;
    cout.precision(6);
    for(int e=1;e<=t;e++)
    {
        cin>>c>>f>>x;
        ans=0;p=2;
        //c/p+x/(p+f)<>x/p
        while(true)

             if (c/p+x/(p+f)>=x/p) break; else
        {
            ans+=c/p;
            p+=f;
        }
        cout<<"Case #"<<e<<": "<<fixed<<ans+x/p<<endl;
    }
    return 0;
}
