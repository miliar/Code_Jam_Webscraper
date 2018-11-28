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
    READ("D-large.in");
    WRITE("out.in");

    int tc;
    scanf("%d",&tc);
    for(int tci=1;tci<=tc;tci++)
    {
        int n;
        scanf("%d",&n);
        vector < double > nom1,nom2,ken1,ken2;
        for(int i=0;i<n;i++)
        {
            double k;
            scanf("%lf",&k);
            nom1.PB(k);
            nom2.PB(k);
        }
        for(int i=0;i<n;i++)
        {
            double k;
            scanf("%lf",&k);
            ken1.PB(k);
            ken2.PB(k);
        }
        sort(ALL(nom1));
        sort(ALL(ken1));
        sort(ALL(nom2));
        sort(ALL(ken2));

        int ans1=0,ans2=0;

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(nom2[i]<ken2[j])
                {
                    nom2[i]=0;
                    ken2[j]=0;
                    ans2++;
                    break;
                }
            }
        }
        ans2=n-ans2;

        while(1)
        {
            int flg=1;
            for(int i=0;i<n;i++)
            {
                if(nom1[i]<ken1[i])
                {
                    int j;
                    for(j=i;j<n-1;j++)
                    {
                        nom1[j]=nom1[j+1];
                    }
                    nom1[j]=1001;
                    flg=0;
                }
                if(flg==0)
                    break;
            }
            if(flg==1)
                break;
        }
        for(int i=0;i<n;i++)
        {
            if(nom1[i]==1001)
                continue;
            if(nom1[i]>ken1[i])
                ans1++;
        }

        printf("Case #%d: %d %d\n",tci,ans1,ans2);
    }
    return 0;
}



