/*

*/

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <unistd.h>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>
#include <cctype>
#include <climits>
#include <iterator>


using namespace std;

int T,t,i;
double x,c,f,ans;

void solve()
{
    scanf("%d",&T);
    for(t=1;t<=T;++t)
    {
        ans=0;
        scanf("%lf %lf %lf",&c,&f,&x);
        for(i=1;i<=(((x*f)-(2*c))/(c*f));++i)
            ans+=c/(2+(i-1)*f);
        ans+=x/(2+((i-1)*f));
        printf("Case #%d: %.7lf\n",t,ans);
    }
}

int main(int argc,char *argv[])
{
	solve();
    return 0;
}
