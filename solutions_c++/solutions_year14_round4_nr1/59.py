/*
*/

//#pragma comment(linker, "/STACK:16777216")
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

long tests,n,x,ar[200000];
long ans;
string st;
long ts;
long used[200000];
long rem;

int main(){
//freopen("dagger.in","r",stdin);
//freopen("dagger.out","w",stdout);
freopen("C:/input.txt","r",stdin);
freopen("C:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);
//cin.tie(0);

cin>>tests;
for (;tests;--tests)
{
 ++ts;
 cin>>n>>x;
 for (int i=0;i<n;i++)
 cin>>ar[i];
 sort(ar,ar+n);
 for (int i=0;i<n;i++)
  used[i]=0;
 ans=0;
 for (int i=0;i<n;i++)
 {
  if (used[i])continue;
  rem=x-ar[i];
  used[i]=1;
  ++ans;
  for (int j=n-1;j>i;--j)
   if (used[j]==0&&ar[j]<=rem){used[j]=1;break;}
 }
 cout<<"Case #"<<ts<<": "<<ans<<endl;
// cout<<ans<<endl;
}

cin.get();cin.get();
return 0;}

