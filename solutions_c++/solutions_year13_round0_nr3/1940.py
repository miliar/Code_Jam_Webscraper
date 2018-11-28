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

vector<long long> ans;
long long answ,a,b,ts,tests;
vector<long long > v;

bool ispal(long long q)
{
     v.clear();
     
     while (q){v.push_back(q%10);q/=10;}
     for (int i=0;i<v.size();i++)
     if (v[i]!=v[v.size()-i-1])return false;
     return true;
}
int main(){
//freopen("icy.in","r",stdin);
//freopen("icy.out","w",stdout);
freopen("C:/input.txt","r",stdin);
freopen("C:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);

for (long long i=1;i<=10000000;i++)
{
    if (ispal(i)&&ispal(i*i))
    ans.push_back(i*i);
}

cin>>tests;
//cout<<ans.size()<<endl;

for (;tests;--tests)
{
    cin>>a>>b;
    ++ts;
    answ=0;
    for (int i=0;i<ans.size();i++)
    {
     if (ans[i]>=a&&ans[i]<=b)++answ;
    }
    cout<<"Case #"<<ts<<": "<<answ<<endl;
}
cin.get();cin.get();
return 0;}
