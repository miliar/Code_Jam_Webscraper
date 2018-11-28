#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<stdlib.h>
#include<vector>
#include<cmath>
#include<queue>
#include<set>
using namespace std;
#define N 1010
#define LL long long
#define INF 0xfffffff
const double eps = 1e-8;
const double pi = acos(-1.0);
const double inf = ~0u>>2;
double x[N],y[N];
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int i,j,t,n,kk=0;
    cin>>t;
    while(t--)
    {
        cin>>n;
        for(i = 0; i < n ;i++)
        cin>>x[i];
        for(i =0 ;i < n ;i++)
        cin>>y[i];
        sort(x,x+n);
        sort(y,y+n);
        j = 0;
        int o1=0;
        for(i = 0 ;i < n ;i++)
        {
            while(j<n&&y[j]<x[i])
            {
                j++;
            }
            if(j==n) break;
            j++;
            o1++;
        }
        j = 0;
        int o2 = 0;
        for(i = 0 ;i < n ;i++)
        {
            while(j<n&&x[j]<y[i])
            j++;
            if(j==n) break;
            j++;
            o2++;
        }
        printf("Case #%d: ",++kk);
        cout<<o2<<" "<<n-o1<<endl;
    }
    return 0;
}
