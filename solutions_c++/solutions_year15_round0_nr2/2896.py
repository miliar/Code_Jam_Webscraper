#include <bits/stdc++.h>
using namespace   std;



#define mod 1000000009
#define si 1001
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
int c[si],cc[si];
int main() {
freopen("B-large.in","r",stdin);
freopen("Bl.txt","w",stdout);
int t,n,i,j,x,ma,ans=pow(10,6),f,temp,div,p;

cin>>t;
rep(j,t)
{ ans=pow(10,6);
 n=scan();
 memset(c,0,sizeof(c));

 ma=0;
 rep(i,n)
 {
  x=scan();
  c[x]++;

  ma=max(ma,x);
 }

 rep(i,ma)
 {

  div=0;
  for(f=i+1;f<=ma;f++)
  {
   p=0;
   if(f%i>0)
   p=1;
    temp=(f/i)+p-1;

    div+=(temp*c[f]);



  }
  ans=min(ans,i+div);

 }

 printf("Case #%d: %d\n",j,ans);


}


}
