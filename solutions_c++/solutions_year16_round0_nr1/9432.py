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
int arr[10],cnt;
void find(ll n)
{ll i=n;
  while(i)
  {ll temp=i%10;
    if(!arr[temp])
    {cnt++;
      arr[temp]=1;
    }
    i/=10;
  }
}
int main()
{freopen("input.txt","r",stdin);

freopen("output.txt","w",stdout);
ll t,n,i,flag,t1;
  sl(t);t1=t;
   w(t)
   {sl(n);
    if(n==0){
    cout<<"Case #"<<(t1-t)<<": "<<"INSOMNIA\n";continue;}
   memset(arr,0,sizeof(arr));cnt=0;
     flag=0;
     i=1;
     while(cnt<10)
     {
	 find(n*i);
      i++;
     }
     cout<<"Case #"<<(t1-t)<<": "<<(n*(i-1));ent;
   }
}
