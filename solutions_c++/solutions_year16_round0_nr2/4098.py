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
 
  int t,n,i,j,ans,in;
  cin>>t;
  rep(j,t)
    {
      string x;
      cin>>x;
      n=x.size();
      ans=0;
      while(1)
	{in=-1;
	  rep2(i,n-1,0)
	    {
	      if(x[i]=='-')
		{
		  in=i;break;
		}
	       
	    }
	  
	  if(in==-1)break;
	  ans++;
	 
	  rep0(i,in+1)
	    {
	      if(x[i]=='-')x[i]='+';
	      else
		x[i]='-';
	    } 
	   
	}
      printf("Case #%d: %d\n",j,ans);
    }
 

}
