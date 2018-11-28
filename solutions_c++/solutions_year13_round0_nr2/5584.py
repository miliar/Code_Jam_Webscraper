#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int maxn = 105;
int arr[maxn][maxn];
int N,M;
bool ok(int x,int y)
{
    int i;
    int now = arr[x][y];
    bool flag = true;
    for(i=x+1;i<N;i++)
        if(arr[i][y]>now)
        {
            flag = false;
            break;
        }
    for(i=x-1;i>=0;i--)
        if(arr[i][y]>now)
        {
            flag = false;
            break;
        }
    if(flag)
        return true;
    flag = true;
    for(i=y+1;i<M;i++)
        if(arr[x][i]>now)
        {
            flag = false;
            break;
        }
    for(i=y-1;i>=0;i--)
        if(arr[x][i]>now)
        {
            flag = false;
            break;
        }
    return flag;
}
int main()
{
    int T,ncase=0;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    int i,j;
    while(T--)
    {
        cin>>N>>M;
        for(i=0;i<N;i++)
            for(j=0;j<M;j++)
                cin>>arr[i][j];
        bool flag = true;
        printf("Case #%d: ",++ncase);
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
            {
                flag = ok(i,j);
                if(!flag)break;
            }
            if(!flag)break;
        }
        if(flag)
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
    return 0;
}
