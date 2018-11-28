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
int SI(string st) {int ans; stringstream s; s<<st; s>>ans; return ans;}
string IS(int n) {string str; stringstream s; s<<n; s>>str; return str;}

int main()
{
    freopen("read.txt","r",stdin);
    freopen("write.txt","w",stdout);
    int t,tt = 1;
    int x,r,c;
    cin>>t;
    while(t--)
    {
        cin>>x>>r>>c;
        string ans;
        if(x == 1) ans = "GABRIEL";
        if(x == 2)
        {
            if( (r*c % 2) == 1) ans = "RICHARD";
            else ans = "GABRIEL";
        }
        if(x == 3)
        {
            if(r == 3 && c != 1) ans = "GABRIEL";
            else if(r != 1 && c == 3) ans = "GABRIEL";
            else ans = "RICHARD";
        }
        if(x == 4)
        {
            if((r ==3 && c == 4) || (r == 4 && c == 3) || (r == 4 && c == 4))
            ans = "GABRIEL";
            else ans = "RICHARD";
        }
        cout<<"Case #"<<tt++<<": "<<ans<<"\n";
    }
    
}
