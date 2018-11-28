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

int T,N;
string s;
int ans(0);

int main()
{
  freopen("A-large.in","r",stdin);
  freopen("A.out","w",stdout);
  
  cin>>T;
  for(int cas=1;cas<=T;cas++)
  {
    cin>>N>>s;
    ans=0;
    int tt=s[0]-'0';
    for(int i=1;i<=N;i++)
    {
      int ts=s[i]-'0';
      if(tt<i) 
      {
        ans+=i-tt;
        tt=i;
      }
      tt+=ts;
    }
    cout<<"Case #";cout<<cas<<": ";
    cout<<ans<<endl;
  }
  return 0;
}

