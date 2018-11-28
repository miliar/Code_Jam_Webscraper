#include <cstring>
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
#include <memory.h>

using namespace std;
#define FOR(i,a)    for(int i = 0;i < a;i++)
#define REP(i,a,b)  for(int i = a;i < b;i++)
#define vi vector<int>

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    REP(a,1,t+1)
    {
        int r,c,w;
        int ans=0;
        cin>>r>>c>>w;
        if(w==1)
        {
            cout<<"Case #"<<a<<": "<<r*c<<endl;
            continue;
        }
        ans=(floor((double)(c-1)/(w)))+w;
        ans+=((double(c-1)/(w))*(r-1));
        cout<<"Case #"<<a<<": "<<ans<<endl;
    }
    return 0;
}
