#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

const int MAXN = 100000 + 10;
const int INF = 1<<30;
const double eps = 1e-8;

int n,m;
int a[105][105];

int main()
{
    freopen("boutB.txt","w",stdout);
    freopen("B-large.in","r",stdin);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        bool f=true;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                int t1=-1,t2=-1;
                for(int k=0;k<n;k++)
                {
                    if(k!=i&&a[k][j]>t1)
                    {
                        t1=a[k][j];
                    }
                }
                for(int k=0;k<m;k++)
                {

                    if(k!=j&&a[i][k]>t2)
                    {
                        t2=a[i][k];
                    }
                }
              //  printf("*%d %d %d %d %d\n",a[i][j],t1,t2,i,j);
                if(t1>a[i][j]&&t2>a[i][j])
                {
                    f=false;
                    break;
                }
            }
            if(!f)
            {
                break;
            }
        }
        if(f)
        {
            printf("Case #%d: YES\n",cas);
        }
        else
        {
            printf("Case #%d: NO\n",cas);
        }
    }
	return 0;
}
