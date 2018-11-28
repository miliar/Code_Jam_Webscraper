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
    vector<int> first;
    vector<int> second;
    vector<int> ans;
    int T;
    scanf("%d", &T);
    for(int tc = 1;tc <= T;tc++)
    {
        first.clear();
        second.clear();
        ans.clear();
        int row1;
        scanf("%d", &row1);
        for(int i = 1;i <= 4;i++)
        {
            for(int j = 1;j <= 4;j++)
            {
                int tmp;
                scanf("%d", &tmp);
                if(row1 == i)
                {
                    first.PB(tmp);
                }
            }
        }
        scanf("%d", &row1);
        for(int i = 1;i <= 4;i++)
        {
            for(int j = 1;j <= 4;j++)
            {
                int tmp;
                scanf("%d", &tmp);
                if(row1 == i)
                {
                    second.PB(tmp);
                }
            }
        }
        for(int i = 0;i < first.size();i++)
        {
            for(int j = 0;j < second.size();j++)
            {
                if(first[i] == second[j])
                {
                    ans.PB(first[i]);
                }
            }
        }
        printf("Case #%d: ",tc);
        if(ans.size() == 0)printf("Volunteer cheated!\n");
        else if(ans.size() > 1)printf("Bad magician!\n");
        else printf("%d\n",ans[0]);
    }
return 0;
}

