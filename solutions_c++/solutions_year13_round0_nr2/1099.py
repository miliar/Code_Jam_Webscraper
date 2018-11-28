/*
TASK: Lawnmower
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
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
typedef pair<int,int> PII;
typedef long long LL;

int N,M,T;
int tb[127][127];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int ii=0;
    while(T--)
    {
        ii++;
        vector<int> Mc_row(127),Mc_col(127);
        scanf("%d%d",&N,&M);
        for(i=1;i<=N;i++)
            for(j=1;j<=M;j++)
            {
                scanf("%d",&tb[i][j]);
                Mc_row[i]=max(Mc_row[i],tb[i][j]);
                Mc_col[j]=max(Mc_col[j],tb[i][j]);
            }
        bool ok=true;
        for(i=1;i<=N;i++)
        {
            for(j=1;j<=M;j++)
            {
                if(tb[i][j]<Mc_row[i] && tb[i][j]<Mc_col[j])
                    ok=false;
            }
        }
        printf("Case #%d: %s\n",ii,ok? "YES":"NO");
    }
}
