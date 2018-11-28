/*
TASK: Magic Trick
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
    freopen("A-small-attempt0.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int tt=0;
    while(T--)
    {
        tt++;
        int tb[5][5];
        int num[20];
        memset(num,0,sizeof num);
        for(k=1;k<=2;k++)
        {
            scanf("%d",&N);
            for(i=1;i<=4;i++)
                for(j=1;j<=4;j++)
                    scanf("%d",&tb[i][j]);
            for(i=1;i<=4;i++)
                num[tb[N][i]]++;
        }
        int co=0,Mc=1;
        for(i=1;i<=16;i++)
            if(num[i]==2)
                co++,Mc=i;
        if(co==0)       printf("Case #%d: Volunteer cheated!\n",tt);
        else if(co>1)   printf("Case #%d: Bad magician!\n",tt);
        else            printf("Case #%d: %d\n",tt,Mc);
    }
}
