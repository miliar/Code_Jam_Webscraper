/*

*/

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
#define lr asgasgash
 
#define  INF 100000000
#define eps 1e-6
#define M_PI 3.141592653589793
//#define mx 1000000000000ll
#define bs 1000002013
//#define free asdfasdfsdadsg
//#define szz 400
//#define pb push_back
#define MAXN 100000
#define free afdshjioey
//#define SIZE 60

using namespace std;

long long tests,n,p,m,l,r;
long long ts;

long long g(long long overal, long long cbranch,
long long tleft, long long gwin)
{
//    cout<<overal<<" "<<cbranch<<" "<<tleft<<" "<<gwin<<endl;
    // cin.get();
 if (gwin==0)
 {
  if (overal>1){long long no=overal/2;
  long long ntleft=tleft/2;
  long long nbranch=cbranch+tleft/2;return g(no,nbranch,ntleft,gwin);}
  else return cbranch;
 }
 if (overal<tleft)
 {
  long long no=(overal-1)-(overal-1)/2+1;long long ntleft=tleft/2;
  long long nbranch=cbranch;return g(no,nbranch,ntleft,gwin);
 } 
 else return cbranch+tleft-1;
}
int main(){
//freopen("funny.in","r",stdin);
//freopen("funny.out","w",stdout);
freopen("C:/input.txt","r",stdin);
freopen("C:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);

cin>>tests;
for (;tests;--tests)
{
    ++ts;
 cin>>n>>p;
 l=1;
 r=(1ll<<n);
 
 
 while (l<r)
 {
  m=l+r+1;m/=2;
  if (g(m,0,(1ll<<n),0)>=p)r=m-1;
  else l=m;     
 }   
 cout<<"Case #"<<ts<<": ";
 cout<<l-1;
 
 l=1;
 r=(1ll<<n);
 
 while (l<r)
 {
        m=l+r+1;
        m/=2;
        if (g(m,0,(1ll<<n),1)>=p)r=m-1;
        else l=m;
 }
 cout<<" "<<l-1<<endl;
}

cin.get();cin.get();
return 0;}
