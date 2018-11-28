#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <cassert>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include<stdio.h>



#define uniq(c) (c).resize(unique(c.begin(),c.end())-(c).begin());
#define all(a) a.begin(),a.end()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define PI 3.14159265
#define eps 1e-10
#define LL long long
#define ULL unsigned long long
#define MOD 1000000007



using namespace std;
int SI(string str) {int ans; stringstream s; s<<str; s>>ans; return ans;}
string IS(int n) {string str; stringstream s; s<<n; s>>str; return str;}

bool equal(double a, double b)
{
    //cout<<fabs(a-b)<<" "<<eps<<"\n";
    return fabs(a - b) > eps;
}

int main()
{
    freopen("read.txt","r",stdin);
    freopen("write.txt","w",stdout);
    //cout<<equal(2.000000000000000001,2.0000000000000015555);
    int t;
    double time,c,f,x;
    double maxx = 0.0;
    double co,fo,xo;
    cin>>t;
    
    FOR(i,1,t+1)
    {
        cin>>co>>fo>>xo;
        time = 0.0;
        x = xo;
        f = 2.0;
        c = 0.0;
        maxx = x /f;
        //cout<<maxx<<"..\n";
        while(1)
        {
           if(time + ((x-c)/f) > maxx) break; 
           if((time + (x-c)/f < maxx) )
           {
              maxx = time*1.0 + (x-c)*1.0/(f*1.0) ;
              //cout<<maxx<<"...\n";
           }
           c = co;
           time = time + c/f;
           c = 0;
           f += fo;
           //cout<<time<<" "<<maxx<<"\n"; //<<" "<<c<<" "<<f<<" "<<maxx<<"\n";
        }    
        //cout<<"Case #"<<i<<": "<<maxx<<"\n";
        printf("Case #%d: %0.7f\n",i,maxx);
    }    
    
    //int aa;cin>>aa;
    return 0;
}
