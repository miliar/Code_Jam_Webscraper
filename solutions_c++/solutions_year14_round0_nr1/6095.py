#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cmath>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define all(c) c.begin(), c.end()
#define ITER(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define mod 1000000007
#define MAXN 1000010
#define EPS 1e-8
#define PI acos(-1)


int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
	freopen("sol.txt", "w", stdout);

    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
        int f1,f2;
        int ma1[4][4];
        int ma2[4][4];
        cin>>f1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>ma1[i][j];
        cin>>f2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>ma2[i][j];
        int c=0;
        int num=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(ma1[f1-1][i]==ma2[f2-1][j])
                {
                    c++;num=ma1[f1-1][i];
                }

            }
        }
        if(c>1)
            printf("Case #%d: Bad magician!\n",cas++);
        else
            if(c)
                printf("Case #%d: %d\n",cas++,num);
            else
                printf("Case #%d: Volunteer cheated!\n",cas++);
    }
    return 0;
}
