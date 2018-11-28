#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<map>
#include<stack>
#include<queue>
#include<set>
#include<vector>
#include<set>
#include<deque>
#include<utility>
#include<algorithm>
#include<bitset>
#include<climits>
#include <sstream>
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define PB push_back
#define MP make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define INF 1000000000
#define M 1000000007
typedef long long int LL;
typedef long long               ll;
typedef unsigned int            uint;
typedef unsigned long long int     ull;
#define mem(a,b) memset(a,b,sizeof a)
using namespace std;
int main()
{
    int T;
    char str[10005];
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        int smax,cnt=0,p=0;
        cin>>smax;
        cin>>str;
        for(int i=0;i<smax+1;i++)
        {
            int x=str[i]-'0';
            if(p<i && x!=0)
            {
                cnt+=i-p;
                p=i;
            }
                p+=x;
        }
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}
