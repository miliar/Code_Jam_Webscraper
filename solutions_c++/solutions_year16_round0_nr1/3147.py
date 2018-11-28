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
#define MAX 15
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);

bool used[MAX];

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
        int T ;
        cin>>T;
        if(T==0)
            printf("Case #%d: INSOMNIA\n",cas++);
        else
        {
            int n=0;
            int w=n,num=0;
            memset(used,0,sizeof(used));
            while(num<10)
            {
                n+=T;
                w=n;
                while(w)
                {
                    if(!used[w%10])
                    {
                        num++;
                        used[w%10]=1;
                    }
                    w/=10;
                }
            }
            printf("Case #%d: %d\n",cas++,n);
        }
    }
    return 0;
}


