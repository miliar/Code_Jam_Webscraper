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
#define mminf(u)  memset(u,0x3f,sizeof(u))
using namespace std ;
#define MAX 105
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);

char s[MAX];

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T ;
    cin>>T;
    int cas=1;
    while(T--)
    {
        int k,c,s;
        cin>>k>>c>>s;
        ll num=pow(k,c-1)+0.2;
        printf("Case #%d: 1",cas++);
        ll ans=1;
        for(int i=1;i<s;i++)
        {
            ans+=num;
            printf(" %I64d",ans);
        }
        printf("\n");
    }
    return 0;
}


