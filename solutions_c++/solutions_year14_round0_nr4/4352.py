#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <queue>
#define MAXN 1005
using namespace std;
int N,ansa,ansb;
double a[MAXN],b[MAXN];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int Case,M1,M2;
    scanf("%d",&Case);
    for(int ca=1;ca<=Case;++ca)
    {
        scanf("%d",&N);
        for(int i=0;i<N;++i)
            scanf("%lf",&a[i]);
        for(int i=0;i<N;++i)
            scanf("%lf",&b[i]);
        sort(a,a+N);
        sort(b,b+N);
        ansa=ansb=0;
        for(int i=0,j=0;i<N&&j<N;)
        {
            if(a[i]<b[j]) ansb++,i++,j++;
            else j++;
        }
        ansb=N-ansb;
        M1=0,M2=N;
        while(1)
        {
            int cnt=0;
            for(int i=M1,j=0;i<N&&j<M2;)
            {
                if(b[j]<=a[i]) cnt++,i++,j++;
                else break;
            }
            if(cnt==M2)
            {
                ansa=cnt;
                break;
            }
            M1++;
            M2--;
            if(M1==N) break;
        }
        printf("Case #%d: %d %d\n",ca,ansa,ansb);
    }
    return 0;
}
