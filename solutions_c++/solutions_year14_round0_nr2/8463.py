#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <cassert>
#include <valarray>
#include <cmath>
#include <time.h>
#include <stack>
#include <queue>
#include <vector>
#define mood 1000000007
#define rep(a,n) for(LL i=a;i<=n;i++)
#define rep0(n) for(LL i=0;i<n;i++)
#define MIN(a,b) ((a)<(b))?(a):(b)
#define MAX(a,b) ((a)>(b))?(a):(b)
#define CHAR_TO_INDEX(c) ((int)c - (int)'a')
#define sqr(x) ((x)*(x))
#define gc getchar_unlocked
#define pc(x) putchar_unlocked(x);
typedef long L;
typedef long long LL;
typedef unsigned long long ULL;
typedef std::map <L,L> MapType;
typedef std::map<std::string,std::string> Mappy;
using namespace std;

int main()
{
    freopen("jamin2.txt","r",stdin);
    freopen("jamout2.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        double c,f,x,cs=0,ps=0,tt=0,temp=0;
        cin>>c>>f>>x;
        ps = x/2;
        cs = c/2 + x/(2+f);
        temp = c/2;
        while(ps>=cs)
        {
            tt++;
            ps = cs;
            temp = temp + c/(f*tt+2);
            cs = temp + x/(f*(tt+1)+2);
        }
        printf("Case #%d: %0.7lf\n",i,ps);
    }
}
