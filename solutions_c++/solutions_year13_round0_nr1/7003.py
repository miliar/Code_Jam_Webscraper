#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <utility>
#include <stack>
#include <sstream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b)				for (i=a;i<b;i++)
#define s(n)					scanf("%d",&n)
#define p(n)					printf("%d\n",n)
#define pl(n)					printf("%lld\n",n)
#define sd(n)					int n;scanf("%d",&n)
#define sl(n)					scanf("%lld",&n)
#define sld(n)					long long int n;scanf("%lld",&n)
#define pb(n)                                   push_back(n)
#define all(c)                                  (c).begin(),(c).end()
#define tr(container,it)                        for (typeof(container.begin()) it=container.begin();it!=container.end();it++ )
#define sz(a)                                   int((a).size())
#define clr(a)                                  memset(a,0,sizeof(a))
#define mp(a,b)                                 make_pair(a,b)

typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vstr;

bool didwin(vstr &v,char c)
{
    int i,j;
    //rows
    FOR(i,0,4)
    {
        int cnt=0;
        FOR(j,0,4)
        {
            if (v[i][j]==c||v[i][j]=='T') cnt++;
        }
        if (cnt==4) return true;
    }
    //columns
    FOR(j,0,4)
    {
        int cnt=0;
        FOR(i,0,4)
        {
            if (v[i][j]==c||v[i][j]=='T') cnt++;
        }
        if (cnt==4) return true;
    }
    //diagonals
    int cnt=0;
    FOR(i,0,4) if (v[i][i]==c||v[i][i]=='T') cnt++;
    if (cnt==4) return true;
    cnt=0;
    FOR(i,0,4) if (v[i][3-i]==c||v[i][3-i]=='T') cnt++;
    if (cnt==4) return true;
    return false;
}

int main()
{
    sd(t);
    int i,j,k;
    
    FOR(i,0,t)
    {
        vstr v;
        bool incomp=false;
        FOR(j,0,4)
        {
            string str;
            cin>>str;
            v.pb(str);
            FOR(k,0,4) if (str[k]=='.') incomp=true;
        }
        string ans;
        if (didwin(v,'X')) ans="X won";
        else
        {
            if (didwin(v,'O')) ans="O won";
            else
            {
                if (incomp) ans="Game has not completed";
                else ans="Draw";
            }
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
        
    }
}
