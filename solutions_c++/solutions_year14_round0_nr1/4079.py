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
  
long tests,ans1[200000],ans2[20000],a,b;
vector<long> av;
long q,ts;

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
 cin>>a;
 for (int i=1;i<=4;i++)
 for (int j=1;j<=4;j++)
 {
  cin>>q;
  ans1[q]=i;
 }
 cin>>b;
 for (int i=1;i<=4;i++)
 for (int j=1;j<=4;j++)
 {
  cin>>q;
  ans2[q]=i;
 }
 
 av.clear();
 for (int i=1;i<=16;i++)
 {
  if (ans1[i]==a&&ans2[i]==b)
  av.push_back(i);
 }
 ++ts;
 cout<<"Case #"<<ts<<": ";
 if (av.size()>1)cout<<"Bad magician!"<<endl;
 else if (av.size()==0)cout<<"Volunteer cheated!"<<endl;
 else cout<<av[0]<<endl;
}

cin.get();cin.get();
return 0;}
 
