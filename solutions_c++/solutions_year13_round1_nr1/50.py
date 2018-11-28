#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define popb pop_back

#define pii pair<int,int>
#define mp make_pair
#define X first
#define Y second

#define pi 3.1415926536

int T,Tnow;
ll t;
ll used;
ll r;
ll n,nl,nr;

int main(){
 scanf("%d",&T);
 for(Tnow=1;Tnow<=T;Tnow++){
  scanf("%lld%lld",&r,&t);
  nl = 0; nr = 1000000001;
  while(nr>nl+1){
   n = (nl+nr)/2;
   used = (2*r+1+2*n);
//printf("%lld\n%lld\n%lld\n\n",n,used,t);
   if(used<=t/(n+1)) nl=n;
   else nr=n;
  }
  printf("Case #%d: %lld\n",Tnow,nl+1);
 }

 return 0;
}
