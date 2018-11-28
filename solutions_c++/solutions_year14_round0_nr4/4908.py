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

bool f(double i,double j)
{
    return i>j;
}

int main()
{
    freopen("read.txt","r",stdin);
    freopen("write.txt","w",stdout);
    
    int t,n;
    double a[20],b[20];
    cin>>t;
    FOR(tt,1,t+1)
    {
        cin>>n;
        FOR(i,0,n) cin>>a[i];
        FOR(i,0,n) cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        int ans1 = 0,ans2 = 0,h[10] = {0};
        FOR(i,0,n)
        {
            FOR(j,0,n)
            {
                if(b[j]>a[i] && h[j] == 0)
                {
                    ans2++;
                    h[j]=1;
                   // cout<<a[i]<<" "<<b[j]<<"\n";
                    break;
                }
            }
        }
        //cout<<n-ans2<<"\n";
        sort(b,b+n,f);
        int h1[10] = {0};
        FOR(i,0,n)
        {
            FOR(j,0,n)
            {
                if(a[j]>b[i] && h1[j] == 0)
                {
                    ans1++;
                    h1[j]=1;
                    //cout<<b[i]<<" "<<a[j]<<"\n";
                    break;
                }
            }
        }
        cout<<"Case #"<<tt<<": "<<ans1<<" "<<n-ans2<<"\n";
    }
    
    
    return 0;
}    
