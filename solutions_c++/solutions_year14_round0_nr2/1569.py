#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define F(i,L,R) for (int i = L; i < R; i++) //next four are for "for loops"
#define FE(i,L,R) for (int i = L; i <= R; i++)
#define FF(i,L,R) for (int i = L; i > R; i--)
#define FFE(i,L,R) for (int i = L; i >= R; i--)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define ALL(p) p.begin(),p.end()
#define ALLR(p) p.rbegin(),p.rend()
#define MP(x, y) make_pair(x, y)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)

#define ff first
#define ss second
#define ll long long
#define ull unsigned long long
#define ui unsigned int
#define us unsigned short
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >
#define vi vector < int >
#define vii vector < vector < int > >

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;
#define PI 3.1415926535897932384626

int main() {
    READ("B-large.in");
    WRITE("out.in");

    int tc;
    scanf("%d",&tc);
    for(int tci=1;tci<=tc;tci++)
    {
        double c,f,x;
        double t1,t2;
        scanf("%lf %lf %lf",&c,&f,&x);
        double co=2.0;
        double sum=0.0;
        while(1)
        {
            t1=x/co;
            t2=(c/co)+(x/(co+f));
            if(t2>t1)
                break;
            sum=sum+(c/co);
            co=co+f;
        }
        sum=sum+(x/co);
        printf("Case #%d: %.7lf\n",tci,sum);
    }
    return 0;
}


