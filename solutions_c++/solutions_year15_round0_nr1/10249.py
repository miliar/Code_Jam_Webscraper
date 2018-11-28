#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cstring>
#include<limits.h>
#include<vector>
#include<stack>
#include<math.h>
#define mp make_pair
#define pb push_back
#define sc(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define scs(a) scanf("%s",a)
#define pii pair< long, int >
#define pr(a) printf("%d ",a)
#define prl(a) printf("%lld\n",a)
#define rep(i,a,b) for(i=a;i<b;i++)
#define rev(i,a) for(i=a;i>=0;i--)
typedef long long ll;
using namespace std;
int main()
{
 int t,i,j;
 char a[10005];
 sc(t);
 rep(i,1,t+1){
 int l;
 sc(l);
 scs(a);
 ll ans=0;
 int ppl=0;
 rep(j,0,l+1){
    if(ppl<j){
     ans+=j-ppl;
     ppl+=j-ppl;}
    ppl+=a[j]-48;
 }
 cout<<"case #"<<i<<": "<<ans<<"\n";
 }
 return 0;
}

