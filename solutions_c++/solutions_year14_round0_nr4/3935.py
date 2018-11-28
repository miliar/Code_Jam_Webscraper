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
 
#define  INF 100000000
#define eps 1e-11
//#define M_PI 3.141592653589793
//#define mx 1000000000000ll
#define bs 1000000009
#define bsize 256
 
using namespace std;

long n,tests,ans1,ans2;
vector<double> v1,v2;
double q;

long solve(vector<double> v1,vector<double> v2)
{
 long res=0;
 long l,r;
 l=0;
 r=v2.size()-1;
 for (int i=v1.size()-1;i+1;i--)
 {
  if (v2[r]<v1[i]){++l;++res;}
  else --r;
 }
 return res;
}

long ts;

int main(){
//freopen("melman.in","r",stdin);
//freopen("melman.out","w",stdout);
freopen("C:/input.txt","r",stdin);
freopen("C:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);
cin.tie(0);

cin>>tests;
for (;tests;--tests)
{
 cin>>n;
 ans1=ans2=0;
 
 v1.clear();
 v2.clear();
 for (int i=1;i<=n;i++)
 {
  cin>>q;v1.push_back(q);
 }
 for (int i=1;i<=n;i++)
 {
  cin>>q;
  v2.push_back(q);
 }
 sort(v1.begin(),v1.end());
 sort(v2.begin(),v2.end());
 
 ans1=solve(v1,v2);

 long cur=0;
 for (int i=0;i<v1.size();i++)
 {
     if (cur<v2.size()&&v2[cur]<v1[i])ans2++,cur++;
 }
 ++ts;
 cout<<"Case #"<<ts<<": "<<ans2<<" "<<ans1<<endl;
}

cin.get();cin.get();
return 0;}
 
