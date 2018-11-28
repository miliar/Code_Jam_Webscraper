#include <bits/stdc++.h>

using namespace std;
struct segtree{
   vector<char> tree;
   vector<char> lazy;
   int N;
   segtree(int n)
   {
      N=n;
      tree.resize(4*n);
      lazy.resize(4*n);
   }
   void build(int v,int tl,int tr,string & s)
   {
      if(tl==tr)
      {
         tree[v]=s[tl];
      }
      else
      {
         int m=(tl+tr)>>1;
         build(v*2,tl,m,s);
         build(v*2+1,m+1,tr,s);
      }
   }
   void push(int v,int tl,int tr)
   {
      if(lazy[v])
      {
         if(tree[v]=='+')
            tree[v]='-';
         else
            tree[v]='+';
         if(v*2<tree.size())
         {
            lazy[v*2]=1-lazy[v*2];
         }
         if(v*2+1<tree.size())
         {
            lazy[v*2+1]=1-lazy[v*2+1];
         }
         lazy[v]=0;
      }
   }
   char getel(int v,int tl,int tr,int pos)
   {
      push(v,tl,tr);
      if(tl==tr)
      {
         return tree[v];
      }
      int m=(tl+tr)>>1;
      if(pos<=m)
      {
         return getel(v*2,tl,m,pos);
      }
      else
      {
         return getel(v*2+1,m+1,tr,pos);
      }
   }
   void update(int v,int tl,int tr,int l,int r)
   {
      push(v,tl,tr);
      if(tl>=l&&tr<=r)
      {
         lazy[v]=1-lazy[v];
         return;
      }
      if(tl>r||tr<l)
      {
         return;
      }
      int m=(tl+tr)>>1;
      update(v*2,tl,m,l,r);
      update(v*2+1,m+1,tr,l,r);
   }
   void update(int l,int r)
   {
      update(1,0,N-1,l,r);
   }
   void build(string & s)
   {
      build(1,0,N-1,s);
   }
   int getel(int pos)
   {
      return getel(1,0,N-1,pos);
   }

};
int main()
{
    ios_base::sync_with_stdio(0);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t;
    cin>>t;
    for(int o=1;o<=t;o++)
    {
       string s;
       int ans=0;
       cin>>s;
       int k;
       cin>>k;
       segtree kek(s.size());
       kek.build(s);
       for(int i=0;i<s.size()+1-k;i++)
       {
          if(kek.getel(i)=='-')
          {
             ans++;
             kek.update(i,i+k-1);
          }
       }
       for(int i=s.size()+1-k;i<s.size();i++)
       {
          if(kek.getel(i)=='-')
          {
             cout<<"Case #"<<o<<": IMPOSSIBLE\n";
             ans=-1;
             break;
          }
       }
       if(ans>=0)
         cout<<"Case #"<<o<<": "<<ans<<'\n';

    }
    return 0;
}
