#include<cstdio>
#include<algorithm>
#include<set>
using namespace std;
int val[1010];
int id[1010];
bool cmp(int a,int b)
{
    return val[a]>val[b];
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("ret","w",stdout);
    int ti;scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        int E,R,n;scanf("%d%d%d",&E,&R,&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&val[i]);
            id[i]=i;
        }
        sort(id,id+n,cmp);
        long long ret=0;
        set<int>use;
        use.insert(-1);
        for(int i=0;i<n;i++)
        {
            set<int>::iterator a=use.lower_bound(id[i]),b=a;
            a--;
            int tmp=E;
            if(*a!=-1)
            {
                tmp=min(tmp,(id[i]-*a)*R);
            }
            if(b!=use.end())
            {
                int tt=max(E-(*b-id[i])*R,0);
                tmp=max(tmp-tt,0);
            }
            //printf("%d %d\n",tmp,val[id[i]]);
            ret+=(long long)tmp*val[id[i]];
            use.insert(id[i]);
        }
        printf("Case #%d: %I64d\n",ca,ret);
    }
}
