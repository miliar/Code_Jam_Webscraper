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

int n,i,j,k;double a[1009],b[1009];

si(n);

rep(i,n){scanf("%lf",&a[i]);}rep(i,n){scanf("%lf",&b[i]);}

sort(a,a+n);sort(b,b+n);

int cnt1=0,cnt2=n,l=0,r=n-1;
//rep(i,n){printf("%lf",a[i]);pw;}pn;rep(i,n){printf("%lf",b[i]);pw;}pn;

                                                     
i=0;j=0;
while(i<n&&j<n){if(b[j]<a[i]){cnt1++;i++;j++;}else{i++;}}




i=n-1;j=n-1;
while(i>=0&&j>=0){if(b[j]>a[i]){cnt2--;i--;j--;}else{i--;}}
printf("Case #%d: ",ka);
pi(cnt1);pw;pi(cnt2);pn;
}

return 0;}
