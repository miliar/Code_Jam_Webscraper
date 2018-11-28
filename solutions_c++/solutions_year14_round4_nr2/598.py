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

int T,N,A[1005];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>N;
        for(int i=1;i<=N;i++)
        {
            scanf("%d",A+i);
        }
        int ans=0;
        for(int i=1;i<=N;i++)
        {
            int left=0,right=0;
            for(int j=1;j<i;j++)
            {
                if(A[j]>A[i]) left++;
            }
            for(int j=i+1;j<=N;j++)
            {
                if(A[j]>A[i]) right++;
            }
            ans+=min(left,right);
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
