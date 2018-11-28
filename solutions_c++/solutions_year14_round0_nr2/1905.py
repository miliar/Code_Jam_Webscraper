#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
#define pb push_back
#define MP make_pair
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define DWN(i,h,l) for(int i=(h);i>=(l);--i)
typedef long long LL;
typedef pair<int,int> PII;


int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int casnum;
    cin>>casnum;
    double c,f,x;
    FOR(cas,1,casnum){
        cin>>c>>f>>x;
        double ans=x/2.0;
        double pretime=0;

        for(int i=1;i<=1000000;++i){
            pretime+=c/(2+(i-1.0)*f);
            ans=min(ans,pretime + x / (2 + i*f));
        }
        printf("Case #%d: %.7lf\n",cas,ans);
    }


    return 0;
}
