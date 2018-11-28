/*
TASK: Osmos
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
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int tt=0;
    while(T--)
    {
        scanf("%d%d",&M,&N);
        vector<int> v;
        for(i=0;i<N;i++)
        {
            scanf("%d",&k);
            v.push_back(k);
        }
        sort(ALL(v));
        k=0;
        j=1000000;
        tt++;
        bool ok=false;
        for(i=0;i<N;i++)
        {
            if(M>v[i])
            {
                M+=v[i];
            }
            else
            {
                k++;
                M+=(M-1);
                if(M>v[i])  M+=v[i];
                else
                {
                    j=min(j,k+N-i-1);
                    i--;
                }
            }
            if(k>j) break;
        }
        printf("Case #%d: %d\n",tt,min(j,k));
    }
}
