#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

const int MAXN=200010;
const int INF=~0U>>3;

int n,m,k,s[MAXN];

#define lc (c<<1)+1
#define rc (c<<1)+2
#define ls lc,l,mid
#define rs rc,mid+1,r

int w[MAXN<<2],bj[MAXN<<2];

void pushDown(int c)
{
    bj[lc]+=bj[c],w[lc]+=bj[c];
    bj[rc]+=bj[c],w[rc]+=bj[c];
    bj[c]=0;
}
void insert(int c,int l,int r,int L,int R,int val)
{
    if(l==L && r==R)
    {
        bj[c]+=val;
        w[c]+=val;
        return;
    }
    if(bj[c]) pushDown(c);
    int mid=(l+r)>>1;
    if(R<=mid)insert(ls,L,R,val);
    else if(mid<L)insert(rs,L,R,val);
    else insert(ls,L,mid,val),insert(rs,mid+1,R,val);
    w[c]=max(w[lc],w[rc]);
}
int query(int c,int l,int r,int L,int R)
{
    if(l==L && r==R)return w[c];
    if(bj[c]) pushDown(c);
    int mid=(l+r)>>1;
    if(R<=mid)return query(ls,L,R);
    else if(mid<L)return query(rs,L,R);
    else return max(query(ls,L,mid),query(rs,mid+1,R));
}
void init()
{
    scanf("%d%d%d",&n,&m,&k);
    memset(bj,0,sizeof(bj));
    memset(w,0,sizeof(w));
    for(int i=1;i<=n;++i)
    {
        scanf("%d",&s[i]);
        insert(0,1,n,max(i,k),min(i+k-1,n),s[i]);
    }
}
void solve()
{
    for(int i=0,a,b,c;i<m;++i)
    {
        scanf("%d%d%d",&a,&b,&c);
        if(a==0)
        {
            insert(0,1,n,max(b,k),min(b+k-1,n),-s[b]);
            insert(0,1,n,max(b,k),min(b+k-1,n),c);
            s[b]=c;
        }
        else if(a==1)
        {
            if(b==c)continue;
            insert(0,1,n,max(b,k),min(b+k-1,n),-s[b]);
            insert(0,1,n,max(b,k),min(b+k-1,n),s[c]);

            insert(0,1,n,max(c,k),min(c+k-1,n),-s[c]);
            insert(0,1,n,max(c,k),min(c+k-1,n),s[b]);

            swap(s[b],s[c]);

        }
        else
        {
            printf("%d\n",query(0,1,n,b+k-1,c));
        }
    }
}
int main()
{
//    freopen("in.txt","r",stdin);
    int t;
    for(scanf("%d",&t);t--;)
    {
        init();
        solve();
    }
    return 0;
}