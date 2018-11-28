/*
*/

#pragma comment(linker, "/STACK:16777216")
#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>
#include <memory.h>

#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
 
#define eps 1e-11
//#define M_PI 3.141592653589793
#define bs 1000000007
#define bsize 256

using namespace std;

long long tests,n,p,q,r,ss,s[2000000];
long long ar[2000000];
long long bst,l,mid;
long long s1,s2;
long long ts;

void check(long long a,long long b)
{
 long long t1,t2,t3;
 if (a<0||a>n||b<0||b>n||b<a)return;
 t1=s[a];
 t2=s[b]-s[a];
 t3=s[n]-s[b];
 t1=max(t1,t2);
 t1=max(t1,t3);
 bst=min(bst,t1);
}

int main(){
//freopen("trade.in","r",stdin);
//freopen("trade.out","w",stdout);
freopen("C:/input.txt","r",stdin);
freopen("C:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);
//cin.tie(0);

cin>>tests;
for (;tests;--tests)
{
 ++ts;
 cin>>n>>p>>q>>r>>ss;
 
 for (int i=0;i<n;i++)
 {
  ar[i+1]=i*p+q;
  ar[i+1]%=r;
  ar[i+1]+=ss;
 }
 
 for (int i=1;i<=n;i++)
  s[i]=s[i-1]+ar[i];
 
 bst=1e18;
 
 for (int cp=0;cp<n;cp++)
 {
  l=cp+1;
  r=n;
  while (l<r)
  {
   mid=l+r;
   mid/=2;
   s1=s[mid]-s[cp];
   s2=s[n]-s[mid];
   if (s1<s2)l=mid+1;
   else r=mid;
  }
  check(cp,l-1);
  check(cp,l);
  check(cp,l+1);
 }
 cout<<"Case #"<<ts<<": ";
 cout.precision(12);
 cout<<fixed<<1.0-bst*1.0/s[n]<<endl;
}

cin.get();cin.get();
return 0;}
