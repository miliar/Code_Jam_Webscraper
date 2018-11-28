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

int solve()  {  long int n,sum,ans;
sum=ans=0;
string s;
scanf("%ld",&n);
cin>>s;
s[0]==0?(ans+=1,sum+=1):sum+=s[0]-'0';
rep(i,1,s.size())  {  
if(sum<i)  ans+=1,sum+=1;
sum+=s[i]-'0';
}
return ans;
}

int main()
{
freopen("/home/arvind/Downloads/A-large.in","r",stdin);
freopen("out3.in","w",stdout);
int k=1;
int t;  cin>>t;
while(t--)
 {  
   printf("Case #%d: %d\n",k++,solve());
 }
 return 0;
}
