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

long tests;
long m,n,bst,bcalc;
string st[2000];
vector<long> v[200];
long ts;

void check()
{
 for (int i=0;i<n;i++)
  if (v[i].size()==0)return;
 long calc=0;
 set<string> s;
 string temp;
 for (int i=0;i<n;i++)
 {
  s.clear();
  temp="";
  s.insert(temp);
  for (int j=0;j<v[i].size();j++)
  {
   temp="";
   long p=v[i][j];
   for (int q=0;q<st[p].size();q++)
   {temp+=st[p][q];s.insert(temp);}
  }
  calc+=s.size();
 }
 if (calc<bst)return;
 if (calc>bst)bcalc=0;
 bst=calc;bcalc++;
}

void solve(long ps)
{
 if (ps==m)
 {check();return;}
 for (int i=0;i<n;i++)
 {
  v[i].push_back(ps);
  solve(ps+1);
  v[i].pop_back();
 }
}

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
 ts++;
 cin>>m>>n;
 bst=0;
 bcalc=0;
 
 for (int i=0;i<m;i++)
 {
  cin>>st[i];
 }
 for (int i=0;i<n;i++)
 v[i].clear();
 solve(0);
 cout<<"Case #"<<ts<<": "<<bst<<" "<<bcalc<<endl;
}

cin.get();cin.get();
return 0;}

