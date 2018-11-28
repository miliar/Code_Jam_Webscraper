#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define Key_value ch[ch[root][1]][0]
const int MAXN = 100010;
int pre[MAXN],ch[MAXN][2],root,tot1;
int size[MAXN];
int rev[MAXN];
int s[MAXN],tot2;
void NewNode(int &r,int f,int k)
{
    r = k;
    pre[r] = f;
    ch[r][0] = ch[r][1] = 0;
    size[r] = 1;
    rev[r] = 0;
}
void Update_Rev(int r)
{
    if(!r)return;
    swap(ch[r][0],ch[r][1]);
    rev[r] ^= 1;
}
inline void push_up(int r)
{
    size[r] = size[ch[r][0]] + size[ch[r][1]] + 1;
}
inline void push_down(int r)
{
    if(rev[r])
    {
        Update_Rev(ch[r][0]);
        Update_Rev(ch[r][1]);
        rev[r] = 0;
    }
}
void Build(int &x,int l,int r,int f)
{
    if(l > r)return;
    int mid = (l+r)/2;
    NewNode(x,f,mid);
    Build(ch[x][0],l,mid-1,x);
    Build(ch[x][1],mid+1,r,x);
    push_up(x);
}
int n;
void Init()
{
    root = tot1 = tot2 = 0;
    ch[root][0] = ch[root][1] = pre[root] = size[root] = rev[root] = 0;
    NewNode(root,0,n+1);
    NewNode(ch[root][1],root,n+2);
    Build(Key_value,1,n,ch[root][1]);
    push_up(ch[root][1]);
    push_up(root);
}
inline void Rotate(int x,int kind)
{
    int y = pre[x];
    push_down(y);
    push_down(x);
    ch[y][!kind] = ch[x][kind];
    pre[ch[x][kind]] = y;
    if(pre[y])
        ch[pre[y]][ch[pre[y]][1]==y] = x;
    pre[x] = pre[y];
    ch[x][kind] = y;
    pre[y] = x;
    push_up(y);
}
inline void Splay(int r,int goal)
{
    push_down(r);
    while(pre[r] != goal)
    {
        if(pre[pre[r]] == goal)
        {
            push_down(pre[r]);
            push_down(r);
            Rotate(r,ch[pre[r]][0]==r);
        }
        else
        {
            push_down(pre[pre[r]]);
            push_down(pre[r]);
            push_down(r);
            int y = pre[r];
            int kind = ch[pre[y]][0]==y;
            if(ch[y][kind] == r)
            {
                Rotate(r,!kind);
                Rotate(r,kind);
            }
            else
            {
                Rotate(y,kind);
                Rotate(r,kind);
            }
        }
    }
    push_up(r);
    if(goal == 0) root = r;
}
inline int Get_kth(int r,int k)
{
    push_down(r);
    int t = size[ch[r][0]] + 1;
    if(t == k)return r;
    if(t > k)return Get_kth(ch[r][0],k);
    else return Get_kth(ch[r][1],k-t);
}
inline int Get_pre(int r)
{
    push_down(r);
    if(ch[r][0] == 0)return -1;
    r = ch[r][0];
    while(ch[r][1])
    {
        r = ch[r][1];
        push_down(r);
    }
    return r;
}
inline int Get_next(int r)
{
    push_down(r);
    if(ch[r][1] == 0)return -1;
    r = ch[r][1];
    while(ch[r][0])
    {
        r = ch[r][0];
        push_down(r);
    }
    return r;
}
struct Node
{
    int id,val;
}node[MAXN];
bool cmp(Node a,Node b)
{
    if(a.val != b.val)return a.val < b.val;
    else return a.id < b.id;
}
int main()
{
	while(scanf("%d",&n) == 1 && n)   
    {
        for(int i = 1;i <= n;i++)
        {
            scanf("%d",&node[i].val);
            node[i].id = i;
        }
        sort(node+1,node+n+1,cmp);
        Init();
        for(int i = 1; i <= n;i++)
        {
            Splay(node[i].id,0);
            printf("%d",size[ch[root][0]]);
            if(i < n)printf(" ");
            else printf("\n");
            Splay(Get_kth(root,i),0);
            Splay(Get_next(node[i].id),root);
            Update_Rev(Key_value);
        }
    }
    return 0;
}