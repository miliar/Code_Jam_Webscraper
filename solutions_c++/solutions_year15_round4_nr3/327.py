
#include <iostream>
#include <stdio.h>

using namespace std;
struct Tree
{
    int l, r;
    long long sum, lazy;
}tree[400009];
int n,m,a[100009];
void pushup(int root)
{
    tree[root].sum=tree[root*2].sum+tree[root*2+1].sum;
}
void pushdown(int root)
{
    int mid=(tree[root].l + tree[root].r)/2;
    if (tree[root].lazy)
    {
        tree[root * 2].lazy += tree[root].lazy;
        tree[root * 2].sum += tree[root].lazy * (mid - tree[root].l +1);
        tree[root * 2 +1].lazy += tree[root].lazy;
        tree[root * 2 + 1].sum += tree[root].lazy * (tree[root].r - mid);
        tree[root].lazy = 0;
    }
}
void build (int root, int l, int r)
{
    tree[root].l=l;
    tree[root].r=r;
    if (l==r)
    {
        tree[root].sum=a[l];
        return;
    }
    int mid = (l + r)/2;
    build (root*2,l,mid);
    build (root*2+1,mid+1,r);
    pushup(root);
}
void modify(int root, int l, int r, int val)
{
    if (tree[root].l == l && tree[root].r == r)
    {
        tree[root].sum += val * (r - l + 1);
        tree[root].lazy += val;
        return;
    }
    pushdown(root);
    int mid = (tree[root].l + tree[root].r) / 2;
    if (r <= mid)
    {
        modify(root * 2, l, r, val);
    }
    else if (mid < l)
    {
        modify(root * 2 + 1, l, r, val);
    }
    else
    {
        modify(root * 2, l, mid, val);
        modify(root * 2 + 1, mid + 1, r, val);
    }
    pushup(root);
}
long long query(int root, int l, int r)
{
    if (tree[root].l == l && tree[root]. r == r)
    {
        return tree[root].sum;
}
pushdown(root);
    int mid = (tree[root].l + tree[root].r)/2;
    if (r <= mid)
    {
        return query(root*2, l, r);
    }
    else if (mid < l)
    {
        return query(root*2+1, l, r);
    }
    else
    {
        return query(root*2, l, mid)+query(root*2+1, mid+1, r);
    }
}
int main()
{
    //freopen("in.txt","r",stdin);
    scanf("%d",&n);
    for (int i=1; i<=n; ++i)
    {
        scanf("%d", &a[i]);
    }
    build(1,1,n);
    scanf("%d",&m);
    for (int i=1; i<=m; ++i)
    {
        int t,x,y;
        scanf("%d%d%d",&t,&x,&y);
        if (t == 1)
        {
            int z;
            scanf("%d",&z);
            modify(1, x, y, z);
        }
        else
        {
            cout<<query(1,x,y)<<endl;
        }
    }
    return 0;
}

