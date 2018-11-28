//#pragma comment(linker, "/STACK:16777216")
#include <fstream>
#include <iostream>
#include <string>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <memory.h>
 
#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
 
#define  INF 100000000
#define eps 1e-11
#define M_PI 3.141592653589793
//#define mx 1000000000000ll
#define bs 1000000007
//#define free asdfasdfsdadsg
//#define szz 400
//#define pb push_back
#define MAXN 100000
#define free afdshjioey
//#define SIZE 60
#define FOR(i,a,b) for(int i = a; i < b; ++i)

using namespace std;

long tests,n,m,mi[1000],mj[1000];
long ar[1000][1000],ts,fl;

int main(){
//freopen("icy.in","r",stdin);
//freopen("icy.out","w",stdout);
freopen("C:/input.txt","r",stdin);
freopen("C:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);

cin>>tests;
for (;tests;--tests){
    ++ts;
    cin>>n>>m;
    for (int i=1;i<=max(n,m);i++)
    mi[i]=mj[i]=0;
    for (int i=1;i<=n;i++)
    for (int j=1;j<=m;j++)
    {cin>>ar[i][j];
    mi[i]=max(mi[i],ar[i][j]);
    mj[j]=max(mj[j],ar[i][j]);
    }
    
    fl=0;
    for (int i=1;i<=n;i++)
    for (int j=1;j<=m;j++)
    if (ar[i][j]<mi[i]&&ar[i][j]<mj[j])fl=1;
    cout<<"Case #"<<ts<<": ";
    if (fl)cout<<"NO"<<endl;
    else cout<<"YES"<<endl;
    
}
cin.get();cin.get();
return 0;}
