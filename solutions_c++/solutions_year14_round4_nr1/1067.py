#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
    int T;
    int n,c,a[20000],f[20000],i,j,rest,ans;
    scanf("%d",&T);
    for (int ri=0;ri<T;ri++)
    {
        
        scanf("%d%d",&n,&c);
        ans=0;
        for (int i=0;i<n;i++)
            scanf("%d",&a[i]);
        sort(a,a+n);
        memset(f,0,sizeof(f));
        i=0;j=n-1;
        while(1)
        {
            if (i==j)
            {
                ans++;
                break;
            }
            rest=c;
            rest-=a[j];
            j--;
            if (a[i]<=rest)
            i++;
            ans++;
            if(i>j) break;
        }
        printf("Case #%d: %d\n",ri+1,ans);
    }
}
