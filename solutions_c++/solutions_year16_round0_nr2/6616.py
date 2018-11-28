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

int main() 
{
           ios :: sync_with_stdio(0);
           cin.tie(NULL);
           int t;
           string s;
           cin>>t;
           f(k,1,t)
           {
             cout<<"Case #"<<k<<": ";
			   cin>>s;
			   int c=0;
			   f(i,1,s.length()-1)
			   {
				   if(s[i]!=s[i-1])c++;
			   }
			   if(s[s.size()-1]=='-')c++;
			   cout<<c;el
			}	   

	
  return 0;
}
