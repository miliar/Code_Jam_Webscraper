#define ll long long
#define vi vector <int>
#define pii pair <int,int>
#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

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
#include <cassert>


using namespace std;



int main()
{

    freopen("A-small-attempt0.in","r",stdin);
    freopen("oa1.txt","w",stdout);
    int T,i,j,k;
    cin>>T;

    for(int cs=1;cs<=T;cs++)
    {
        set<int>s;
        int a,b;
        cin>>a;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++){cin>>k;if(i==a)s.insert(k);}
        }
        cin>>b;
        int ans=-1;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>k;
                if(i==b)
                {
                    if(s.find( k )!=s.end())
                    {
                        s.erase(k);
                        ans=k;
                    }
                }
            }
        }
        printf("Case #%d: ",cs);
        if(s.size()==4)printf("Volunteer cheated!\n");
        else if(s.size()==3)printf("%d\n",ans);
        else printf("Bad magician!\n");

    }

    return 0;
}











