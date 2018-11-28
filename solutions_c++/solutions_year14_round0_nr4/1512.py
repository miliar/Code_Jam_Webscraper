#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <bitset>
#include <sstream>
#include <string>

#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m); i<(n); i++)
#define FORDOWN(i,m,n) for(int i=(m)-1; i>=(n); i--)

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define INF 2000000000
#define EPS 1e-11
#define PI acos(-1.0)
#define MAX_N 1000005
#define MOD 1000000007
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;

int
main()
{
    int T;
    scanf("%d", &T);

    for(int tc = 1;tc <= T;tc++)
    {
        int N;
        scanf("%d", &N);
        vector<double> ken;
        vector<double> naomi;
        for(int i = 0;i < N;i++)
        {
            double tmp;
            scanf("%lf", &tmp);
            naomi.PB(tmp);
        }
        sort(naomi.begin(),naomi.end());
        for(int i = 0;i < N;i++)
        {
            double tmp;
            scanf("%lf", &tmp);
            ken.PB(tmp);
        }
        sort(ken.begin(),ken.end());
        int ansbluff = 0;
        int ansnormal = 0;
        int posNaomi = 0;

        // bluff mode
        for(int i = 0;i < N;i++)
        {
            while(posNaomi < N && ken[i] > naomi[posNaomi])posNaomi++;
            if(posNaomi < N)
            {
                ansbluff++;
                posNaomi++;
            }

            if(posNaomi >= N)break;
        }
        // normal mode
        for(int j = N-1;j >= 0;j--)
        {
            // if his highest still low, then use the lowest, he lose anyway
            if(naomi[j] > ken[ken.size() - 1])
            {
                ken.erase(ken.begin());
                ansnormal++;
            }
            else
            {
                //if not use his minimal-but-still-high, binary search? @.@
                int ub = ken.size() - 1;
                int lb = 0;
                int mb;
                int posDeleted = ken.size() - 1;
                int scoreDeleted = ken[ken.size() - 1];
                while(ub > lb)
                {
                    mb = (ub + lb)/2;
                    if(ken[mb] > naomi[j])
                    {
                        if(scoreDeleted > ken[mb])
                        {
                            posDeleted = mb;
                            scoreDeleted = ken[mb];
                        }
                        ub = mb - 1;
                    }
                    else
                    {
                        lb = mb + 1;
                    }
                }
                ken.erase(ken.begin()+posDeleted);
            }
        }

        printf("Case #%d: %d %d\n",tc,ansbluff,ansnormal);
    }
}
