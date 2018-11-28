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

long tests,ts,ar[200000];
vector<pair<long, long> > v;
long n,dp[1200][1200],tp[1200],answ;

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
 cin>>n;
 for (int i=1;i<=n;i++)
 cin>>ar[i];
 v.clear();
 
 for (int i=1;i<=n;i++)
 {
  v.push_back(make_pair(ar[i],i));
 }
 sort(v.begin(),v.end());
 
 for (int i=0;i<=n;i++)
  for (int j=0;j<=n;j++)
   dp[i][j]=1e9;
 
 dp[0][0]=0;
 
 for (int i=0;i<=n;i++)
  tp[i]=0;
  
 for (int s=0;s<n;s++)
  for (int q=s+1;q<n;q++)
   if (v[q].second<v[s].second)++tp[s];
   
 for (int i=0;i<=n;i++)
  for (int j=0;j<=n;j++)
  {
   if (i+j>n)continue;
   dp[i+1][j]=min(dp[i+1][j],dp[i][j]+tp[i+j]);
   dp[i][j+1]=min(dp[i][j+1],dp[i][j]+(n-i-j-tp[i+j]-1));
  }
 answ=1e9;
 for (int i=0;i<=n;i++)
  for (int j=0;j<=n;j++)
   if (i+j==n)answ=min(answ,dp[i][j]);
 
 cout<<"Case #"<<ts<<": "<<answ<<endl;
}

cin.get();cin.get();
return 0;}

