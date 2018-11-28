#include<bits/stdc++.h>
#define ll long long int
#define s(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define w(t) while(t--)
#define f(i,n) for(i=0;i<n;i++)
#define fd(i,n) for(i=n-1;i>=0;i--)
#define p(a) printf("%d",a)
#define pl(a) printf("%lld",a)
#define ps(a) printf("%s",a)
#define pc(a) printf("%c",a)
#define ent printf("\n")
#define maxn 100000
#define mod 1000000007
#define po(a,b) (long long int)pow((double)(a),(double)(b))
#define abs(a) (long long int)abs((double)(a))
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define sz(a) (long long int)((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define se second
#define fi first
using namespace std;
typedef pair <ll,ll> pii;
string s;
int main()
{freopen("input.txt","r",stdin);

freopen("output.txt","w",stdout);
ll t,i,res,j,t1;
  sl(t);
  t1=t;
   getchar();
   w(t)
   {getline(cin,s);ll cnt=0;
     ll pos=s.length()-1;
      if(s[pos]=='+')
      while(s[pos]=='+')pos--;
      i=0;
      if(s[0]=='-')
      {while(s[i]=='-')i++;cnt++;
	  }
	  for(j=i;j<=pos;j++)
	  {if(s[j]=='+')
	     {cnt+=2;
	       while(s[j]=='+' && j<=pos)j++;
	       if(s[j]=='-')j--;
	     }  
	  }
	  cout<<"Case #"<<(t1-t)<<": "<<cnt;ent;
   }
}
