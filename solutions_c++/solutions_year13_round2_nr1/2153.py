#include <iostream>
#include <map>
#include <math.h>
#define ll long long
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <string>
#define mp make_pair
#define pii pair<int,int>
#define vi vector<int>
#define vl vector<ll>
#define pll pair<ll,ll>
#define s second
#define f first
#define pb push_back
using namespace std;
const ll c=110,inf=2000000000ll;
int t,n,a,x[c];
int f(int a,int pos)
{
    if (a==1)
       return n;
    if (pos>=n)
       return 0;
    if (a>x[n-1])
       return 0;
    if (a>x[pos])
       return f(a+x[pos],pos+1);
    int res=f(2*a-1,pos)+1;
    n--;
    res=min(res,f(a,pos)+1);
    n++;
    return res;
}
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for (int u=1; u<=t; u++)
    {
        cin>>a>>n;
        for (int i=0; i<n; i++)
            cin>>x[i];
        sort(x,x+n);
        int res=min(f(a,0),n);
        printf("Case #%d: %d\n",u,res);
    }
    //system("pause");
    return 0;
}
