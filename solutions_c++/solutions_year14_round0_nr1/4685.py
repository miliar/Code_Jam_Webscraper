#include<stdio.h>
#include<limits.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<sstream>
#include <map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#define PB push_back
#define MP make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define mod 1000000007
#define pi(n) printf("%d",n)
#define pin(n) printf("%d\n",n)
#define piw(n) printf("%d ",n)
#define pll(n) printf("%lld",n)
#define plln(n) printf("%lld\n",n)
#define pllw(n) printf("%lld ",n)
#define sll(n) scanf("%lld",&n)
#define ss(s) scanf("%s",s)
#define ps(s) printf("%s",s)
#define psn(s) printf("%s\n",s)
#define psw(s) printf("%s ",s)
#define si(n) scanf("%d",&n)
#define pn printf("\n")
#define pw printf(" ")
using namespace std;
double EPS = 1e-9; 
int main(){
int t,ka;
si(t);
for(ka=1;ka<=t;ka++){

int r1,r2,cnt=0,a[18],i,j,k,x,n=4;
rep(i,18){a[i]=0;}
si(r1);
rep(i,n){rep(j,n){cin>>k;if(i+1==r1){a[k]++;}}}
si(r2);
rep(i,n){rep(j,n){cin>>k;if(i+1==r2){a[k]++;}}}
printf("Case #%d: ",ka);
rep(i,18){
if(a[i]>1){cnt++;x=i;}}//pi(cnt);pw;
if(cnt==0){printf("Volunteer cheated!");}
else if(cnt==1){
printf("%d",x);}
else{printf("Bad magician!");}
pn;
}

return 0;}


