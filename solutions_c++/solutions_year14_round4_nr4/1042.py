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
int Mc,co;
int use[15];
char s[15][15];
void gen(int x)
{
    if(x==N)
    {
        int i,j,k;
        int a,b,c;
        a=0;
        for(i=1;i<=M;i++)
        {
            vector<string> v;
            for(j=0;j<N;j++)
            {
                if(use[j]==i)
                    v.pb(s[j]);
            }
            if(v.size()==0)
                return;
            set<string> ss;
            for(j=0;j<v.size();j++)
            {
                string temp="";
                for(k=0;k<v[j].size();k++)
                {
                    temp+=v[j][k];
                    ss.insert(temp);
                }
            }
            a+=(ss.size()+1);
        }
        //printf("%d %d\n",a,0);
        if(Mc<a)    Mc=a,co=1;
        else if(Mc==a)  co++;
        return;
    }
    for(int i=1;i<=M;i++)
    {
        use[x]=i;
        gen(x+1);
    }
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
	scanf("%d",&T);
	int tt=1;
    while(T--)
    {
        scanf("%d%d",&N,&M);
        for(i=0;i<N;i++)
            scanf("%s",s[i]);
        Mc=0;
        co=0;
        gen(0);
        printf("Case #%d: %d %d\n",tt,Mc,co);
        tt++;
    }
}
