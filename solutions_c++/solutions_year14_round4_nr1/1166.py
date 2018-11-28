#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
using namespace std;
#define length(x) (int)x.size()
const double pi=acos(-1);

int a[10001], b[10001];
bool kt[10001];
int n, m;

void xuli()
{
    cin>>n>>m;
    for(int i=1; i<=n; i++) cin>>a[i];
    sort(1+a, 1+n+a);
    int res = 0;
    while (n>0)
    {
        int k=0, sum=0, dem=0;
        for(int i=n; i>=1; i--)
            if (sum+a[i]<=m&&dem<2)
        {
            dem++; sum=sum+a[i];
        }
        else
        {
            k++; b[k]=a[i];
        }
        res++; n=0;
        for(int i=k; i>=1; i--)
        {
            n++; a[n]=b[i];
        }
    }
    cout<<res<<endl;
}

int main()
{
     freopen("input.inp","r",stdin);
     freopen("output.out","w",stdout);
     int test;
     cin>>test;
     for(int t=1; t<=test; t++)
     {
        cout<<"Case #"<<t<<": ";
        xuli();
     }
     return 0;
}
