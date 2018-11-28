#include <cstring>
#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cmath>
using namespace std;
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define ll long long
#define ff first
#define ss second
#define inf  1e9
#define eps  1e-10
#define infll 1e18
#define pr(x) printf("%d\n",x)
#define sc(x) scanf("%d",&x)
#define fr(i,a,n) for(i=a;i<n;i++)
#define fd(i,a,n) for(i=n;i>a;i--)
#define fiv(v) for(i=0;i<v.size();i++)
#define clr(a) memset(a,0,sizeof(a))
#define fill(a,v) memset(a,v,sizeof(a))
#define all(a) a.begin(),a.end()
#define iter(c,it) for(typeof((c).begin()) it= (c).begin(); it != (c).end(); it++)
int a[6][6],b[6][6];
map<int,int>h;
int main()
{
    int i,n,j,k,l,m,t;
    #ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    sc(t);
    for(int u=1;u<=t;u++)
    {
      int x;
      scanf("%d",&x);
      fr(i,1,5)
      fr(j,1,5)
      scanf("%d",&a[i][j]);
      int y;
      scanf("%d",&y);
      fr(i,1,5)
      fr(j,1,5)
      scanf("%d",&b[i][j]);
      for(i=1;i<=4;i++)
        h[a[x][i]]++;
      int c=0;
      for(i=1;i<=4;i++)
      {
          if(h.count(b[y][i]))
          {
            m=b[y][i];
            c++;
          }
      }
      if(c==1)
      printf("Case #%d: %d\n",u,m);
      else if(c>1)
      printf("Case #%d: Bad magician!\n",u);
      else if(c==0)
      printf("Case #%d: Volunteer cheated!\n",u);
      h.clear();
    }
    return 0;
}

