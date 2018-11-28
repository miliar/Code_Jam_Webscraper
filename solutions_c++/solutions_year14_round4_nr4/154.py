#include<cstdio>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std;
struct trie
{
    trie *a[26];
    int sz;
    int id;
};
int t,best,m,n,c,tmp;
string a[20];
trie *tree[10];
trie *ins(trie *t,int p,string s,int id)
{
    if(t==NULL)
    {
        t=new trie();
        for(int i=0;i<26;i++)
            t->a[i]=NULL;
        tmp++;
        t->sz=0;
        t->id=id;
    }
    if(p==s.size())
        return t;
    else
    {
        t->a[s[p]-'A']=ins(t->a[s[p]-'A'],p+1,s,id);
    }
  return t;
}
trie *rem(trie *t,int r)
{
    if(t==NULL)
        return t;
    else if(t->id==r)
    {

        t=NULL;
        return t;
    }
    else
    {
        for(int i=0;i<26;i++)
            t->a[i]=rem(t->a[i],r);
        return t;
    }
    return t;
}
void f(int x, trie *t[10])
{
    //cout<<x<<endl;
    if(x==m)
    {
        int tc=0;
        for(int i=0;i<n;i++)
            if(t[i]!=NULL)
                tc+=t[i]->sz;
        if(tc>best)
        {
            best=tc;
            c=1;
        }
        else if(tc==best)
            c++;
    }
    else
    {
        for(int i=0;i<n;i++)
        {
            int z=0;
            tmp=0;
            t[i]=ins(t[i],0,a[x],x);
            z=tmp;
            t[i]->sz+=z;
            f(x+1,t);
            t[i]=rem(t[i],x);
            if(t[i]!=NULL)
                t[i]->sz-=z;
        }
    }
    return;
}
int main()
{
    freopen("d-small.out","w",stdout);
    freopen("d-small.in","r",stdin);
    cin>>t;
    for(int zz=1;zz<=t;zz++)
    {
        m=0;
        best=0;
        c=0;
        cin>>m>>n;
        for(int i=0;i<m;i++)
            cin>>a[i];
        for(int i=0;i<n;i++)
            tree[i]=NULL;
        f(0,tree);
        printf("Case #%d: %d %d\n",zz,best,c);
    }
    return 0;
}
