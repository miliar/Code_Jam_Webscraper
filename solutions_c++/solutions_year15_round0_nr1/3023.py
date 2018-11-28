#include <bits/stdc++.h>
using namespace   std;



#define mod 1000000009
#define si 100001
#define f first
#define s second
#define rep(i,n) for(i=1;i<=n;i++)
#define rep0(i,n) for(i=0;i<n;i++)
#define rep1(i,a,b) for(i=a;i<=b;i++)
#define rep2(i,a,b) for(i=a;i>=b;i--)
#define pb push_back
#define mp make_pair
#define endl '\n'
#define ll long long
#define ull unsigned long long
#define v2(x) vector< vector <int> > x
#define print(x) printf("%d\n",x)

#ifdef ONLINE_JUDGE
#define gc getchar_unlocked
#else
#define gc getchar
#endif

inline int scan(){
    char c = gc();
    int x = 0;
    bool b=0;
    while(c<'0'||c>'9'){
        {
            if(c=='-')
            b=1;
            c=gc();

        }
    }
    while(c>='0'&&c<='9'){
        x=(x<<1)+(x<<3)+c-'0';
        c=gc();
    }
    if(b==1)
        x*=-1;
    return x;
}

int main() {
freopen("A-large.in","r",stdin);
freopen("al.txt","w",stdout);
int t,n,i,j,ans,c,p;
char x[2000];

scanf("%d",&t);

rep(j,t)
{
 scanf("%d %s",&n,x);
 ans=0;
 c=0;
 rep0(i,n+1)
 {
  if(c<i)
  {ans+=(i-c);
  c=i;
  }
p=x[i]-'0';
c+=p;



 }
 printf("Case #%d: %d\n",j,ans);
}


}

