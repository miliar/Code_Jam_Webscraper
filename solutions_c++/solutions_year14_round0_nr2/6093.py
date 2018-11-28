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
    freopen("B-large.in", "r", stdin);
	freopen("sol.txt", "w", stdout);
	int t;
	cin>>t;
	int ca=1;
	while(t--)
    {
        double G,T,X;
        cin>>G>>T>>X;
        double mini=X/2.0;
        int i=1;
        double nue=X/(2.0+T*i)+G*i/2.0;
        while(mini>nue)
        {
            i++;
            mini=nue;
            nue=X/(2.0+T*i);
            for(int j=0;j<i;j++)
            {
                nue+=G/(2.0+j*T);
            }
        }
        printf("Case #%d: %.7f\n",ca++,mini);
    }
    return 0;
}
