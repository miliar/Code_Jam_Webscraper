#include <bits/stdc++.h>
using namespace   std;


      
#define mod 1000000007
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
#define pi(x) printf("%d ",x)
#define pll(x) printf("%lld ",x)
#define pie(x) printf("%d\n",x)
#define plle(x) printf("%lld\n",x)

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
 
  ll t,n,i,j,temp,c,ans;
  cin>>t;
  rep(j,t)
    {
      cin>>n;
      printf("Case #%d: ",j);
      if(n==0)
	{
	  printf("INSOMNIA\n");
	  continue;
	}
      bool a[10]={0};
      c=0;i=1;
      while(c<10)
	{ 
	  ans=n*i;
	  temp=ans;
	  while(temp)
	    {
	      if(a[temp%10]==0)
		{
		  a[temp%10]=1;
		  c++;
		}
	      temp/=10;
	    }
	  i++;

	}
      plle(ans);

    }
 

}
