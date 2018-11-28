#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
using namespace std;

int T,N,X;
int S[10005];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        printf("Case #%d: ",ca);
        cin>>N>>X;
        for(int i=1;i<=N;i++)
        {
            scanf("%d",S+i);
        }
        sort(S+1,S+N+1);
        int ans=0;
        for(int i=N;i>=1;i--)
        {
            if(S[i]==-1) continue;
            ans++;
            for(int j=i-1;j>=1;j--)
            {
                if(S[j]==-1) continue;
                if((S[i]+S[j])<=X)
                {
                    S[j]=-1;
                    break;
                }
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
