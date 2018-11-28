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

long tests,ts,w,h,b,x[4][3000],y[4][3000],x2[3000],y2[3000],
g[2000][2000],d[2000],bst,bp;
long used[2000];

long gd(long a,long b)
{
 long res=2e9;
 for (int i=1;i<=2;i++)
  for (int j=1;j<=2;j++)
   for (int q=1;q<=2;q++)
    for (int w=1;w<=2;w++)
     res=min(res,max(abs(x[i][a]-x[j][b]),abs(y[q][a]-y[w][b])));
 
 if (x[1][a]>=x[1][b]&&x[1][a]<=x[2][b])
  for (int i=1;i<=2;i++)
   for (int j=1;j<=2;j++)
    res=min(res,abs(y[i][a]-y[j][b]));
 if (x[2][a]>=x[1][b]&&x[2][a]<=x[2][b])
  for (int i=1;i<=2;i++)
   for (int j=1;j<=2;j++)
    res=min(res,abs(y[i][a]-y[j][b]));
  if (x[1][b]>=x[1][a]&&x[1][b]<=x[2][a])
  for (int i=1;i<=2;i++)
   for (int j=1;j<=2;j++)
    res=min(res,abs(y[i][a]-y[j][b]));
 if (x[2][b]>=x[1][a]&&x[2][b]<=x[2][a])
  for (int i=1;i<=2;i++)
   for (int j=1;j<=2;j++)
    res=min(res,abs(y[i][a]-y[j][b]));
 
  if (y[1][a]>=y[1][b]&&y[1][a]<=y[2][b])
  for (int i=1;i<=2;i++)
   for (int j=1;j<=2;j++)
    res=min(res,abs(x[i][a]-x[j][b]));
 if (y[2][a]>=y[1][b]&&y[2][a]<=y[2][b])
  for (int i=1;i<=2;i++)
   for (int j=1;j<=2;j++)
    res=min(res,abs(x[i][a]-x[j][b]));
  if (y[1][b]>=y[1][a]&&y[1][b]<=y[2][a])
  for (int i=1;i<=2;i++)
   for (int j=1;j<=2;j++)
    res=min(res,abs(x[i][a]-x[j][b]));
 if (y[2][b]>=y[1][a]&&y[2][b]<=y[2][a])
  for (int i=1;i<=2;i++)
   for (int j=1;j<=2;j++)
    res=min(res,abs(x[i][a]-x[j][b]));
    
 return res;
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
 ++ts;
 cin>>w>>h>>b;
 
 g[0][b+1]=g[b+1][0]=w;
 for (int i=1;i<=b;i++)
 {
  cin>>x[1][i]>>y[1][i]>>x[2][i]>>y[2][i];
  x[2][i]++;
  y[2][i]++;
  g[0][i]=g[i][0]=min(x[1][i],x[2][i]);
  g[i][b+1]=g[b+1][i]=w-max(x[1][i],x[2][i]);
 }
 
 for (int i=1;i<=b;i++)
  for (int j=1;j<=b;j++)
  {
   g[i][j]=gd(i,j);
  }
  /*
  for (int i=0;i<=b+1;i++)
 {  for (int j=0;j<=b+1;j++)
    cout<<g[i][j]<<" ";
    cout<<endl;}
    */
 for (int i=0;i<=b+1;i++) 
 used[i]=0,d[i]=1e9;
 d[0]=0;
 
 for (int iter=1;iter<=b+2;iter++)
 {
  bst=1e9;
  bp=0;
  for (int i=0;i<=b+1;i++)
   if (used[i]==0&&d[i]<bst)
   {bst=d[i];bp=i;}
  used[bp]=1;
  for (int i=0;i<=b+1;i++)
   d[i]=min(d[i],bst+g[bp][i]);
 }
// ts++;
 cout<<"Case #"<<ts<<": "<<d[b+1]<<endl;
 
}

cin.get();cin.get();
return 0;}

