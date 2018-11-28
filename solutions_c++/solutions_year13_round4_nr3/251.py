#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
const int N=80009;
class SegmentTree
{
    struct node
    {
        int l,r,le,re,me,ly;
    }a[N<<2];
    public:
    #define ls (p<<1)
    #define rs (ls|1)
    #define mid (a[p].l+a[p].r>>1)
    #define A a[p]
    int B(int p)
    {
        return A.r-A.l+1;
    }
    void build_tree(int p,int s,int t)
    {
        A.l=s,A.r=t;
        A.me=A.le=A.re=B(p);
        A.ly=-1;
        if(s==t) return;
        build_tree(ls,s,mid);
        build_tree(rs,mid+1,t);
    }
    void pushDown(int p)
    {
        if(A.ly+1)
        {
            a[ls].me=a[ls].re=a[ls].le=A.ly*B(ls);
            a[rs].me=a[rs].re=a[rs].le=A.ly*B(rs);
            a[rs].ly=a[ls].ly=A.ly;
            A.ly=-1;
        }
    }
    void pushUp(int p)
    {
        A.me=max(a[ls].re+a[rs].le,max(a[ls].me,a[rs].me));
        A.le=a[ls].le==B(ls)?a[ls].le+a[rs].le:a[ls].le;
        A.re=a[rs].re==B(rs)?a[rs].re+a[ls].re:a[rs].re;
    }
    void modify(int p,int s,int t,int v)
    {
        if(A.l==s&&A.r==t)
        {
            A.me=A.le=A.re=B(p)*v;
            A.ly=v;
            return;
        }
        pushDown(p);
        if(t<=mid) modify(ls,s,t,v);
        else
        if(s>mid) modify(rs,s,t,v);
        else
        {
            modify(ls,s,mid,v);
            modify(rs,mid+1,t,v);
        }
        pushUp(p);
    }
    int query(int p,int s,int  t,int x)
    {
        if(A.me<x) return -1;
        if(A.l==s&&A.r==t)
        {
            if(A.me==B(p))
            {
                return s;
            }
        }
        pushDown(p);
        if(t<=mid) return query(ls,s,t,x);
        else
        if(s>mid) return query(rs,s,t,x);
        {
            int k=query(ls,s,mid,x);
            if(k+1) return k;
            else
            {
                if(a[ls].re&&a[ls].re+a[rs].le>=x)
                return mid+1-a[ls].re;
                else
                return query(rs,mid+1,t,x);
            }
        }
        pushUp(p);
    }
}seg;
int n,m;
void init()
{
    scanf("%d%d",&n,&m);
    seg.build_tree(1,1,n);
    while(m--)
    {
        int key;
        scanf("%d",&key);
        if(key&1)
        {
             int d;scanf("%d",&d);
             int k=seg.query(1,1,n,d);
             if(k==-1) puts("0");
             else
             {
                 printf("%d\n",k);
                 seg.modify(1,k,k+d-1,0);
             }
        }else
        {
            int x,d;scanf("%d%d",&x,&d);
            seg.modify(1,x,x+d-1,1);
        }
    }
}
int main()
{
   // freopen("in.txt","r",stdin);
    init();
    return 0;
}