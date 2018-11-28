#include<math.h>
#include<algorithm>
#include<cstdlib>
#include<iostream>
#include<stdio.h>
#include<map>
#include<ext/hash_map>
#include<ext/hash_set>
#include<set>
#include<string>
#include<assert.h>
#include<vector>
#include<time.h>
#include<queue>
#include<deque>
#include<sstream>
#include<stack>
#include<sstream>
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define AB(a) (-(a)<(a)?(a):-(a))
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ep 0.0000000001
#define INF 1001001001
#define P 1000000007
#define pr(x) ((x)>=P?(x)-P:(x))
using namespace std;
const int N=100201;
int n,m,i,j,a[4],k;
int s[100];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("text.out","w",stdout);
    int t;
    cin>>t;
    int tt=0;
    while (t--)
    {
          tt++;
         for (i=0;i<20;i++) s[i]=0;
          cin>>m;
          for (i=1;i<m;i++) 
          for (j=1;j<=4;j++) cin>>k;
          for (i=1;i<=4;i++) cin>>k,s[k]++;
          for (i=1;i<=4-m;i++)for (j=1;j<=4;j++) cin>>k;
          cin>>m;
          for (i=1;i<m;i++) for (j=1;j<=4;j++) cin>>k;
          for (i=1;i<=4;i++) cin>>k,s[k]++;
          for (i=1;i<=4-m;i++)for (j=1;j<=4;j++) cin>>k;
          k=0;
          for (i=0;i<20;i++) if  (s[i]>1) k++,m=i;
          if (k>1) cout<<"Case #"<<tt<<": Bad magician!"<<endl;
          if (k==0) cout<<"Case #"<<tt<<": Volunteer cheated!"<<endl;
          if (k==1) cout<<"Case #"<<tt<<": "<<m<<endl;        
          
          }   
    return 0;
}
