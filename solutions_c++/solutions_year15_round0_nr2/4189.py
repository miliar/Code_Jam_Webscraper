#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
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
#include <queue>
#include <string>
#define rep(i,n) for(int i=0;i<n;i++)
#define F first
#define S second
#define mp make_pair
#define LL long long
#define pb push_back
using namespace std;
#define sz 300005
#define inf 0x7fffffff

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    rep(cas,T)
    {
        int n;
        cin>>n;
        vector <int> p;
        int en;
        rep(i,n)
        {
            cin>>en;
            p.pb(en);
        }
        int ret = 1000;
        for (int mx=1;mx<=1000;mx++)
        {
            int tm = mx;
            rep(i,p.size())
            {
                if(mx == 1)
                {
                    tm+=p[i]-1;
                }
                else
                {
                    tm+= (p[i]+mx-1)/mx - 1;
                }
            }
            //cout <<mx <<" " << tm << endl;
            ret = min(ret, tm);
        }
        cout << "Case #" << cas+1 << ": "<< ret << endl;
    }
}
