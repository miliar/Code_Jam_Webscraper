#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define N 5000005
#define ll long long
#define p(t) cout<<t;
#define f(i,n) for(i=0;i<n;i++)
#define g(i,n) for(i=1;i<=n;i++)
#define s(x) scanf("%I64d",&x);
#define pb push_back
#define mp make_pair

ll a[N],b[N],r,m,n;


int main()
{
ios_base::sync_with_stdio(0);
ll k=0,t=0,x,sum=0,q=0,z=0,y=0,l=0,i,j;
k=1;
ifstream my;
  my.open ("B-large.in");
  ofstream out("out.txt");
  my>>x;

  while(x--){
        string s;
    my>>s;
 n=s.size()-1;
 for(i=n;i>=0;i--){
          if(s[i]=='-')break;
 }
 r=0;
 if(i>=0)r=1;
 i--;

 for(;i>=0;i--){
    while(i>=0 && s[i]==s[i+1])i--;
    if(i>=0)
    r++;
 }
    out<<"Case #"<<k<<": "<<r<<endl;
    k++;



  }

  my.close();

return 0;
}
