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

pair<long long, long long> temp;
stack<pair<long long, long long> > s;
long long op[10000],n,m,cl[10000];
long long st,ans;
long long tests,a[10000],b[10000],c[10000];
long long ts;
long long ps,hs,spand;

map<long long,long long> fromor,toor;
set<long long> has;
vector<long long> vv;
long long gs(long long a,long long b)
{
 return (b-a)*(b-a+1)/2%bs;    
}

void remapp(long long q)
{
     if (has.find(q)!=has.end())return;
     has.insert(q);
     fromor[q]=has.size();
     toor[has.size()]=q;
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
    cin>>n>>m;
    ts++;
    
    fromor.clear();
    toor.clear();
    has.clear();
    
    for (int i=0;i<=4000;i++)
    op[i]=cl[i]=0;
    
    st=0;
    vv.clear();
    for (int i=0;i<m;i++)
    {
        cin>>a[i]>>b[i]>>c[i];
        vv.push_back(a[i]);
        vv.push_back(b[i]);
    }
         
         sort(vv.begin(),vv.end());
         for (int i=0;i<vv.size();i++)
         remapp(vv[i]);
         
    for (int i=0;i<m;i++)
    {
        
        st+=gs(a[i],b[i])%bs*c[i]%bs;
        st%=bs;
            op[fromor[a[i]]]+=c[i];
            cl[fromor[b[i]]]+=c[i];
    }
       
    ans=0;
    
    for(int i=0;i<=4*m;i++)
    {
if (op[i]>0)s.push(make_pair(i,op[i]));
     
     if (cl[i]==0)continue;
     while (cl[i]>0)
     {
         temp=s.top();
      // cout<<toor[temp.first]<<" "<<temp.second<<" "<<cl[i]<<" "<<toor[i]<<
      // " "<<s.size()<<endl;
         ps=temp.first;
         hs=temp.second;
         if (hs<=cl[i]){cl[i]-=hs;spand=hs;
         s.pop();}
         else {s.top().second-=cl[i];spand=cl[i];cl[i]=0;}
         ans+=gs(toor[ps],toor[i])%bs*spand%bs;
     }
    }
    cout<<"Case #"<<ts<<": "<<(ans+1ll*bs*10-st)%bs<<endl;
}
cin.get();cin.get();
return 0;}
