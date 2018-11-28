#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<cmath>
#include<vector>
#include<string>
#include<limits.h>
#include<string.h>
#define ll long long
#define PB push_back
#define MP make_pair
#define Y second
#define X first
#define CLR(x) memset(x,0,sizeof(x))
#define For(i,x,y) for(int i=x;i<=y;i++)
#define Rep(i,x,y) for(int i=x;i<y;i++)
using namespace std;
struct query{
    int l,r,v;
    query(){}
    query(int nl,int nr,int nv):l(nl),r(nr),v(nv){}
};

const int                   Maxn=200010,oo=INT_MAX>>1;
typedef int                 Arr[Maxn];
int                         n,m,cnt,t[Maxn*4];
Arr                         l,r,v,a,pos;
query                       q[Maxn];


int cmp(query a,query b){ return a.v>b.v;}

void check(int k,int l,int r)
{
    if (l==r) return;
    if (t[k]<r-l+1) return;
    int mid=l+r>>1;
    t[k*2]=mid-l+1;
    t[k*2+1]=r-mid;
}
void ins(int k,int l,int r,int x,int y)
{
    check(k,l,r);
    if(y<l||r<x) return;
    if (t[k]==r-l+1) return;    
    if (x<=l&&r<=y){
        t[k]=r-l+1;
        return;
    }
    int mid=l+r>>1;
    ins(k*2,l,mid,x,y);
    ins(k*2+1,mid+1,r,x,y);
    t[k]=t[k*2]+t[k*2+1];
}

int ask(int k,int l,int r,int x,int y)
{
    check(k,l,r);
    if (y<l||r<x) return 0;
    if (x<=l&&r<=y) return t[k];
    int mid=l+r>>1;
    return ask(k*2,l,mid,x,y)+ask(k*2+1,mid+1,r,x,y);
}

int check(int mid)
{
    CLR(t);
    For(i,1,mid) q[i]=query(l[i],r[i],v[i]);
    sort(q+1,q+mid+1,cmp);
    // For(i,1,mid) cout<<q[i].l<<' '<<q[i].r<<endl;
    int x,y;
    for (x=1;x<=mid;x=y+1)
    {
        for (y=x;y+1<=mid&&q[y].v==q[y+1].v;y++);
        int Min=-oo,Max=oo;
        For(i,x,y) 
        {
            Min=max(Min,q[i].l);
            Max=min(Max,q[i].r);
        }
        if (Min>Max) return 2;
        int sum=ask(1,1,cnt,Min,Max);
        if (sum==Max-Min+1) return 1;
        // ins(1,1,cnt,Min,Max);
        For(i,x,y) ins(1,1,cnt,q[i].l,q[i].r);
        // cout<<t[1]<<endl;
        // cout<<"all:"<<ask(1,1,cnt,1,cnt)<<endl;
    }
    return 0;
}

int main()
{
    // ios::sync_with_stdio(0);
    // freopen("1.in","r",stdin);
    while(~scanf("%d%d",&n,&m))
    {
        a[0]=cnt=0;
        For(i,1,m) 
        {
            scanf("%d%d%d",&l[i],&r[i],&v[i]);
            a[++a[0]]=l[i];
            a[++a[0]]=r[i];
        }
        sort(a+1,a+a[0]+1);
        a[0]=unique(a+1,a+a[0]+1)-a-1;
        if (a[1]>1) cnt++;
        a[a[0]+1]=n+1;
        For(i,1,a[0])
        {
            pos[i]=++cnt;
            if (a[i+1]>a[i]+1) cnt++;
        }
        For(i,1,m)
        {
            l[i]=pos[lower_bound(a+1, a+a[0]+1, l[i])-a];
            r[i]=pos[lower_bound(a+1, a+a[0]+1, r[i])-a];
        }
        // For(i,1,m) cout<<l[i]<<' '<<r[i]<<endl;
        int low=1,upr=m+1;
        while(low<upr)
        {
            int mid=low+upr>>1;
            // cout<<mid<< ':'<<endl;
            // cout<<mid<<' '<<check(mid)<<endl;
            if (check(mid)) upr=mid;
            else low=mid+1;
        }
        if (low==m+1) puts("0");
        else printf("%d\n",low);
    }
    return 0;
}