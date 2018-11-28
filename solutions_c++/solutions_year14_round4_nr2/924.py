#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int cmp(const void *a,const void *b)
{
    return *(int *)a-*(int *)b;
}

int min(int a,int b)
{
    return a<b?a:b;
}

const double pi = 3.1415926535897932384626433832795;

int t,id,i,j,n;
char st[10000];
int a[1010][2],b[1010];
int max,ans;

int main()
{
    freopen("B-large.in","r",stdin);freopen("B.out","w",stdout);
    scanf("%d",&t);
    for (id=1;id<=t;id++)
    {
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%d",&a[i][0]);
            a[i][1]=i;
        }
        qsort(a,n,sizeof(a[0]),cmp);
        for (i=0;i<n;i++)b[a[i][1]]=i;
        ans=0;
        for (i=0;i<n-1;i++)
        {
            for (j=0;j<n-i;j++)
            {
                if (b[j]==i) break;
            }
            ans+=min(j,n-i-1-j);
            for (;j<n-i;j++)
            {
                b[j]=b[j+1];
            }
        }

        printf("Case #%d: %d\n",id,ans);
    }
	return 0;
}
