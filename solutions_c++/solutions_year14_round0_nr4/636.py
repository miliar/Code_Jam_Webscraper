/*
TASK: Deceitful War
LANG: C++
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<stack>
#include<bitset>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T;
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int tt=0;
    while(T--)
    {
        tt++;
        int a=0,b=0,c;
        scanf("%d ",&N);
        vi v1,v2;
        for(i=0;i<N;i++)
        {
            scanf("0.%d ",&k);
            v1.pb(k);
        }
        for(i=0;i<N;i++)
        {
            scanf("0.%d ",&k);
            v2.pb(k);
        }
        sort(ALL(v1));
        sort(ALL(v2));
        //for(i=0;i<N;i++)    printf("%d ",v1[i]);
        //printf("\n");
        //for(i=0;i<N;i++)    printf("%d ",v2[i]);
        //printf("\n");
        j=0;
        for(i=0;i<N;i++)
            for(;j<N;j++)
                if(v1[i]<v2[j])
                {
                    b++;    j++;
                    break;
                }
        i=0;
        for(j=0;j<N;j++)
            for(;i<N;i++)
                if(v1[i]>v2[j])
                {
                    a++;    i++;
                    break;
                }
        printf("Case #%d: %d %d\n",tt,a,N-b);
    }
}
