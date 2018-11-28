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
map<ll,ll>co;

void updt(ll g){
    while(g){
        ll p=g%10;
        co[p]=1;
        g=g/10;
    }
}

ll ch(){
   for(ll i=0;i<10;i++) if(co[i]==0)return 0;
   return 1;
}


int main()
{
ios_base::sync_with_stdio(0);
ll k=0,t=0,x,sum=0,q=0,z=0,y=0,l=0,i,j;
r=1;
ifstream my;
  my.open ("A-large.in");
  ofstream out("out.txt");
  my>>x;

  while(x--){
    my>>z;
  for(i=0;i<10;i++)co[i]=0;
    k=0;
    for(i=1;i<=100000;i++){
      t=(i*z);
      updt(t);
      if(ch()){k=1; break;}

    }
    out<<"Case #"<<r<<": ";
    r++;
 if(k)out<<t<<endl;
 else out<<"Insomnia\n";


  }

  my.close();

return 0;
}
