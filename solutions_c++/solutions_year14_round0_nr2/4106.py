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
  
  long tests;
  double c,f,x,t,ans,rate;
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
 cin>>c>>f>>x;
 ans=1e9;
 t=0;
 rate=2;
 for (int i=1;i<=100000;i++)
 {
  ans=min(ans,t+x/rate);
  t+=c/rate;
  rate+=f;
 }
 ++ts;
 cout.precision(9);
 cout<<"Case #"<<ts<<": ";
 cout<<fixed<<ans<<endl;
}
cin.get();cin.get();
return 0;}
 
