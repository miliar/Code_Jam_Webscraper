/*   W          w           w        mm          mm             222222222       7777777777777    */
/*    W        w w         w        m  m        m  m          222        22              7777    */
/*    w        w w         w        m  m        m  m                     22              777     */
/*     w      w   w       w        m    m      m    m                    22              77      */
/*     w      w    w      w        m    m      m    m                 222                77      */
/*      w    w      w    w        m      m    m      m              222                  77      */
/*      w    w      w    w        m      m    m      m            222                    77      */
/*       w  w        w  w        m        m  m        m         222                      77      */
/*       w  w        w  w        m        m  m        m      222                         77      */
/*        ww          ww        m          mm          m     222222222222222             77      */

//#pragma comment(linker, "/STACK:102400000,102400000")

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>

using namespace std;

const int N=1005;
int T;
int n;
char a[N];
int main()
{
  #ifdef ONLINE_JUDGE
  #else
    //freopen("test.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("A-small-attempt1.out","w",stdout);
  #endif
  scanf("%d",&T);
  int ca=1;
  while(T--)
  {
    scanf("%d",&n);
    scanf(" %s",a);
    int ans=0;
    int cnt=(int)(a[0]-'0');
    for(int i=1;i<=n;i++)
    {
      int x=(int)(a[i]-'0');
      if(x)
      {
        if(cnt>=i)
        {
          cnt+=x;
        }
        else
        {
          ans+=i-cnt;
          cnt=i+x;
        }
        //printf("i=%d cnt=%d ans=%d\n",i,cnt,ans);
      }
    }
    printf("Case #%d: %d\n",ca++,ans);
  }
  return 0;
}
