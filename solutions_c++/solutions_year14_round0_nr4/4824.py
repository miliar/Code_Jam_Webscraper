#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <algorithm>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SET(v,x) memset(v,x,sizeof v)
#define FOR(i,a,b) for(int _n(b),i(a);i<_n;i++)
#define EACH(it,v) for(typeof((v).begin()) it = (v).begin();it!=(v).end();it++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define SZ(v) int(v.size())
#define SI ({int x;scanf("%d",&x);x;})




	int main(){

    freopen("A-small-practice.in", "rt", stdin);
    freopen("A-small.out", "wt", stdout);
    int t,i,j,n,k;
	double ken[2000],naomi[2000];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
    {
        cin>>n;
        for(i=0;i<n;i++)
            cin>>naomi[i];
        for(i=0;i<n;i++)
            cin>>ken[i];
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        int d_war=0,war=0;
        i=0,j=0;
        while(i<n&&j<n)
        {
            if(naomi[i]>ken[j])
            {
                d_war++;
                i++;
                j++;
            }
            else
                i++;
        }
        i=0,j=0;
        while(i<n&&j<n)
        {
            if(naomi[i]<ken[j])
            {
                war++;
                i++;
                j++;
            }
            else
                j++;
        }
        printf("Case #%d: %d %d\n",k,d_war,n-war);
    }

	return 0;
}
