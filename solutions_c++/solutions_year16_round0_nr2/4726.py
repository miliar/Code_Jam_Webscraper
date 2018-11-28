#include <algorithm>
#include <iostream>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <map>

using namespace std;

template <typename T>
inline void upd_max(T &dest,const T& src){if(dest<src)dest=src;return ;}
template <typename T>
inline void upd_min(T &dest,const T& src){if(dest>src)dest=src;return ;}

const int maxN=1000+13;


inline char change(char ts) 
{
  if(ts=='-') return '+';
  return '-';
}

char s[maxN];
char vs[maxN];

void reverse(int n)
{
  for(int i=0;i<=n;i++)
    vs[n-i]=change(s[i]);
  for(int i=0;i<=n;i++)
    s[i]=vs[i];
  return ;
}

int main()
{
#ifndef ONLINE_JUDGE
  freopen("B-large.in","r",stdin);
  freopen("B1.out","w",stdout);
#endif
  int T;
  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++)
  {
    printf("Case #%d: ",cas);
    scanf("%s",s);
    int n=strlen(s);
    int ans=0;
    int ed=-1;
    for(int i=n-1;i>=0;i--)
    {
      if(s[i]=='-')
      {
        ed=i;
        break;
      }
    }
    //cout<<ed<<endl;
    if(ed==-1) 
    {
      printf("0\n");
      continue;
    }
    while(ed>=0)
    {
      int tt=0;
      for(int i=0;i<=ed;i++)
      {
        if(s[i]=='+')
          tt++;
        else
          break;
      }
      if(tt>0)
      {
        ans++;
        for(int i=0;i<tt;i++)
          s[i]='-';
      }
      reverse(ed); ans++;
      for(int i=ed;i>=0;i--)
      {
        if(s[i]=='+') ed--;
        else break;
      }
    }
    printf("%d\n",ans);
  }

  return 0;
}

