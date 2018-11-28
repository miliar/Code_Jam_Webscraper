// AUTHOR: ARVIND NAIR

#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

#define s(x) long int x; scanf("%ld", &x)
#define ss(x,y) long int x,y; scanf("%ld%ld", &x, &y)
#define sss(x,y,z) long int x,y,z; scanf("%ld%ld%ld", &x, &y, &z)
#define repit(a,b)   for (__typeof((b).begin()) (a)=(b).begin(); (a)!=(b).end(); (a)++)
#define rep(a,b,c)   for (long int (a)=(b); (a)<(c); (a)++)
#define repn(a,b,c)  for ( long int (a)=(b); (a)<=(c); (a)++)
#define repd(a,b,c)  for ( long int (a)=(b); (a)>=(c); (a)--)
#define all(v) (v).begin(),(v).end()
#define fi  first
#define se  second
#define pb  push_back
#define mp  make_pair
#define INF (int)1e9
#define EPS (double)(1e-9)
#define PI (double)(3.141592653589793)
#define M(x,i) memset(x,i,sizeof(x))

string solve()  {  int x,r,c,m; 
scanf("%d%d%d",&x,&r,&c);
if(x==1)
return "GABRIEL";
else if(x==2) {
if((r*c)%2==0)
return "GABRIEL";
else
return "RICHARD";
}
else if(x==3)  {  m=r*c;
if(m==6||m==9||m==12)
return "GABRIEL";
else 
return "RICHARD";
}
else { m=r*c;
if(m==12||m==16)
return "GABRIEL";
else 
return "RICHARD";
}
}

int main()
{ 
freopen("/home/arvind/Downloads/inp.in","r",stdin);
freopen("out4.in","w",stdout);
s(t);
int k=1;
while(t--)  {
 cout<<"Case #"<<k++<<": "<<solve()<<"\n";
}
return 0;
}
