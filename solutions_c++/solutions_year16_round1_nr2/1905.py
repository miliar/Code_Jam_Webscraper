
#include <string.h>
#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <fstream>
#define  LL long long
#define MOD 1000000007
const int maxn = 105;

using namespace std;

int n;
int lis[maxn][55];
int cnt[2555];
int ans[55];

int main()
{
    int T;
   freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j;
    int cas=1;


    cin>>T;
    while(T--)
        {
            memset(cnt,0,sizeof(cnt));
            cin>>n;
            for(i=0;i<n*2-1;i++)
                {
                    for(j=0;j<n;j++)
                        {
                            cin>>lis[i][j];
                            cnt[lis[i][j]]++;
                        }
                }
            int cc=0;
            for(i=0;i<2501;i++)
                {
                    if(cnt[i]%2==1) ans[cc++]=i;
                }
            cout<<"Case #"<<cas++<<": ";
            for(i=0;i<n-1;i++) cout<<ans[i]<<' ';
            cout<<ans[n-1]<<endl;
        }
    return 0;
}
