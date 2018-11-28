#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <time.h>
#include <string.h>
#include <queue>
#include <stack>
#include <cstring>
using namespace std;
#define MOD 1000000007
#define ll long long int
#define rep(i,a,b) for(int (i) = (a) ; (i) <= (b) ; (i)++)
#define per(i , a , b) for(int (i) = (a) ; (i) >= (b) ; (i)--)

ll exp(ll t,ll x){if(x==0) return 1;if(x==1) return t;if(x%2==1) return (t*exp((t*t)%MOD,x/2))%MOD;if(x%2==0) return exp((t*t)%MOD,x/2);} 
ll gcd(ll x,ll y){return x%y==0?y:gcd(y,x%y);}
ll lcm(ll x,ll y){return x*(y/gcd(x,y));}
bool isprime(ll x){for(ll i=2;i*i<=x;i++){if(x%i==0){return false;}}return true;}

int t,k;
char inpt[1020];
bool check(int &cont){
    cont=0;
    int n=strlen(inpt);
    rep(i,0,n-k){
       if (inpt[i]=='+')continue;
       ++cont;
       rep(j,0,k-1){
	   if (inpt[i+j]=='+')inpt[i+j]='-';
	   else inpt[i+j]='+';
       }
    }
    rep(i,n-k-2,n-1)
	if (inpt[i]=='-')return false;
    return true;
}
int main(){
  freopen("output.txt","w",stdout);
  freopen("input.in","r",stdin);

  cin>>t;
  int cont;
  rep(i,1,t){
	cin>>inpt>>k;
        if (check(cont))printf("Case #%d: %d\n",i,cont);
	else printf("Case #%d: IMPOSSIBLE\n",i);
  }
  return 0;
}
