#include<map>
#include<set>
#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;
const int N = 1006;

int a[N];
int main()
{
    int T,CAS,n=0;

    scanf("%d",&T);
    for(CAS=1;CAS<=T;CAS++)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;i++) scanf("%d",a+i);
        sort(a+1,a+1+n);
        int ans=-1;
        for(int maxv=1;maxv<=a[n];maxv++)
        {
            int split=0;
            for(int i=1;i<=n;i++) if(a[i]>maxv) split+=(a[i]-1)/maxv;
            if(ans==-1 || ans>maxv+split) ans=maxv+split;
        }
        printf("Case #%d: %d\n",CAS,ans);
    }
    return 0;
}
