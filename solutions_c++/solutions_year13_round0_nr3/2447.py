#include <map>
#include <climits>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define DBG(e) cout<<(#e)<<" : "<<e<<endl
#define FOR(i,s,e) for(int i=(s);i<(e);i++)
#define CLEAR(v,i) memset(v,i,sizeof v)
#define ALL(x) x.begin(),x.end()
#define pb  push_back
#define pr pair<int,int>
#define SZ(x) int((x).size())


typedef long long LL;
void fill();
map<LL,bool>mp;
bool pal(LL);
int main()
{

    int tests;
    fill();
    cin>>tests;
    FOR(tt,1,tests+1)
    {
        LL A,B;
        cin>>A>>B;
        int ct=0;
        EACH(it,mp) if(it->first>=A && it->first<=B) ct++;
        cout<<"Case #"<<tt<<": "<<ct<<"\n";
    }
}
void fill()
{

    FOR(i,1,10000001)
    {
        if(pal(i))
        {
            long long val=((LL)i)*i;
            if(pal(val)) mp[val]=1;
        }
    }
}
bool pal(LL x)
{
    LL temp=x;
    LL reverse=0;
    while( temp != 0 )
    {
        reverse = reverse * 10;
        reverse = reverse + temp%10;
        temp = temp/10;
    }
    if ( x == reverse ) return 1;
    return 0;
}
