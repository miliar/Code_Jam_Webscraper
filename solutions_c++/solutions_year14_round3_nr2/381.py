/*
TASK: <Task>
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
bool co[127];
int len[15];
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
	scanf("%d",&T);
	char s[15][127];
	int tt=0;
	int v[15];
    while(T--)
    {
        scanf("%d",&N);
        for(i=0;i<N;i++)
        {
            scanf("%s",s[i]);
            len[i]=strlen(s[i]);
        }
        memset(co,0,sizeof co);
        int Mc=0;
        for(i=0;i<N;i++)
            v[i]=i;
        do
        {
            char ch=0;
            bool ok=true;
            memset(co,0,sizeof co);
            for(i=0;i<N;i++)
            {
                for(j=0;j<len[v[i]];j++)
                {
                    if(co[s[v[i]][j]]==0)
                    {
                        co[s[v[i]][j]]=1;
                        ch=s[v[i]][j];
                    }
                    else
                    {
                        if(s[v[i]][j]!=ch)
                        {
                            ok=false;
                            break;
                        }
                    }
                }
            }
            if(ok)
            {
                Mc++;
            }
        }while(next_permutation(&v[0],&v[N]));
        tt++;
        printf("Case #%d: %d\n",tt,Mc);
    }
}
