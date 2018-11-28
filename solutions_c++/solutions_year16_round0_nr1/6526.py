#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define f(i,a,b) for(int i =a; i <=b ; i++)
#define all(a) a.begin(),a.end()
#define ff first
#define ss second
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define sqr(x) ((x)*(x))
#define EPS 1e-9
#define db(var) cout<<var<<" ";
#define gcd(a,b) __gcd(a,b)
#define p(A,a,b)  f(i,a,b) cout<<A[i]<<" ";
#define sj  cout<<"OK"<<endl;
#define ll long long int 
#define el cout<<endl;

#define MOD 1000000007
#define PI acos(-1.0)
#define e exp(1.0)
#define EPS 1e-9

using namespace std;
vector<int> v;
 int ar[10];
int main() 
{
           ios :: sync_with_stdio(0);
           cin.tie(NULL);
           int t,n,f;
           cin>>t;
           f(k,1,t)
           {
           f=0;
           cin>>n;
           v.clear();
           f(i,0,9)ar[i]=0;
           int m=n,c=1;
           while(v.size()<10 && c<1000000)
           {
           if(n==0)break;
          
             c++;
           while(n)
           {
         
           int d=n%10;
           if(ar[d]==0){
           v.pb(d);
           ar[d]=1;
           if(v.size()==10){f=1;break;}
           }
           n=n/10;
           }
           if(f==1)break;
           n=c*m;
         // cout<<n;el
           }
          cout<<"Case #"<<k<<": ";
           if(f==1)cout<<m*(c-1);
           else cout<<"INSOMNIA";el
       //    cout<<v.size();
  }

	
  return 0;
}
