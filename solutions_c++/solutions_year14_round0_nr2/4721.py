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
int t,k;
si(t);
for(k=1;k<=t;k++){

int i,j;
double c,x,f,ans=1000000000000.0,sum=0.0,temp;

scanf("%lf%lf%lf",&c,&f,&x);
ans=x/2.0;
for(i=0;;i++){sum+=(c/(2.0+((double)i*f)));
temp=sum+(x/(2.0+((double)(i+1)*f)));//printf("%lf",temp);pn;
if(temp>ans-EPS){break;}
else{ans=temp;}}
printf("Case #%d: ",k);
printf("%.7lf",ans);pn;}

return 0;}


