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
#define eps 1e-9
//#define M_PI 3.141592653589793
//#define mx 1000000000000ll
#define bs 1000000007
//#define free asdfasdfsdadsg
//#define szz 400
//#define pb push_back
#define MAXN 10000
#define free afdshjioey
//#define SIZE 60
#define bsize 3

using namespace std;

long long tests;
double b;
long long n,t[1000];
vector<long long> v;
double ans;
long long usd,inv;
long long ts;
long long m,l,r;

int main(){
//freopen("palindrome.in","r",stdin);
//freopen("palindrome.out","w",stdout);
freopen("C:/input.txt","r",stdin);
freopen("C:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);

cin>>tests;
for (;tests;--tests)
{
 ++ts;
     cin>>b>>n;
     for (int i=0;i<=36;i++)
         t[i]=0;
     for (int i=0;i<n;i++)
     {cin>>t[i];}
     
     ans=0;
     for (int sames=1;sames<=36;sames++)
     {
         l=0;
         r=100000000000000000ll;
         while (l<r)
         {
             m=l+r+1;m/=2;
             usd=0;
             inv=0;
             v.clear();
             for (int i=0;i<37;i++)
             v.push_back(t[i]);
             sort(v.begin(),v.end());
             for (int i=0;i<sames;i++)
             {if (v[i]<=m){usd+=m-v[i];inv+=m-v[i];}
             else usd=-100000000000000000ll;}
             
             for (int i=sames;i<v.size();i++)
             if (v[i]<=m){usd+=m+1-v[i];}
             if (usd>b){r=m-1;}
             else l=m;
           //  cout<<m<<" "<<usd<<endl;
         }
         
        // cout<<"!"<<sames<<" "<<l<<endl;
             m=l;
             usd=0;
             inv=0;
             v.clear();
             for (int i=0;i<37;i++)
             v.push_back(t[i]);
             long fl=0;
             sort(v.begin(),v.end());
             for (int i=0;i<sames;i++)
             {if (v[i]<=m){usd+=m-v[i];inv+=m-v[i];}else fl=1;}
             for (int i=sames;i<v.size();i++)
             if (v[i]<=m){usd+=m+1-v[i];}
             if (usd>b)fl=1;
         if (fl==0)
        // if (-usd+inv*36.0/sames>ans){cout<<inv<<" "<<sames<<" "<<ans<<endl;}
         ans=max(ans,-usd+inv*36.0/sames);
     }
     
     cout.precision(10);
     cout<<fixed<<"Case #"<<ts<<": "<<ans<<endl;
     
}

cin.get();cin.get();
return 0;}
