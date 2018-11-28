#include<cstdio>
#include<algorithm>
using namespace std;
int bg[151];
int solve (int a,int n)
{
    int p,q,mins=999999999,c=0;
    if (a==1)
        return n;
    sort (bg,bg+n);
    p = 0;
    q = n-1;
    while (p<=q)
    {
        while (bg[p]<a and p<=q)
        {
            a += bg[p];
            p++;
        }
        if (mins>q-p+c+1)
            mins = q-p+c+1;
        a = a*2-1;
        c++;
    }
    return mins;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    int T,t,a,n,i;
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        scanf("%d %d",&a,&n);
        for (i=0;i<n;i++)
            scanf("%d",&bg[i]);
        printf("Case #%d: %d\n",t,solve (a,n));
    }
    return 0;
}
