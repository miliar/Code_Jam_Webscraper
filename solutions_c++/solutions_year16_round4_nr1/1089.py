#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<time.h>
#include<cmath>
#include<vector>
#include <iomanip>
#define PB(u)  push_back(u);
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
using namespace std ;
#define MAX 130
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);

int a[5000];
int b[5000];


bool sus=false;


bool check(int n)
{
    memcpy(b,a,sizeof(a));
    while(n>0)
    {
        for(int i=0; i<(1<<n); i+=2)
        {
            if(b[i]==b[i+1])
                return false ;
            if(b[i]==2&&b[i+1]==0)
                b[i/2]=0;
            else if(b[i]==0&&b[i+1]==2)
                b[i/2]=0;
            else
                b[i/2]=max(b[i],b[i+1]);
        }
        n--;
    }
    return true ;

}

int n,R,P,S ;

void dfs(int id,int R,int P,int S)
{
    if(R<0||P<0||S<0) return ;
    if(R==0&&P==0&&S==0)
    {
        if(!sus&&check(n))
        {
            for(int i=0; i<(1<<n); i++)
            {
                if(a[i]==0)
                    printf("P");
                else if(a[i]==1)
                    printf("S");
                else  printf("R");
            }
            printf("\n");
            sus=1;
        }
        return ;
    }
    if(P>0)
    {
        a[id]=0;
        dfs(id+1,R,P-1,S);
    }
    if(R>0)
    {
        a[id]=2;
        dfs(id+1,R-1,P,S);
    }
    if(S>0)
    {
        a[id]=1;
        dfs(id+1,R,P,S-1);
    }
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        printf("Case #%d: ",cas++);
        sus=0;
        cin>>n>>R>>P>>S;
        dfs(0,R,P,S);
        if(!sus)
            printf("IMPOSSIBLE\n");
    }
    return 0 ;
}
