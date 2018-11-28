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

const double pi = 3.1415926535897932384626433832795;

int t,id,i,j;
char st[10000];
int n,x,ans;
int s[10010];

int main()
{
    freopen("A-large.in","r",stdin);freopen("A.out","w",stdout);
    scanf("%d",&t);
    for (id=1;id<=t;id++)
    {
        scanf("%d%d",&n,&x);
        for (i=0;i<n;i++)scanf("%d",&s[i]);
        qsort(s,n,sizeof(s[0]),cmp);
        ans=0;
        for (i=n-1,j=0;i>=j;i--)
        {
            if (s[i]+s[j]<=x)j++;
            ans++;
        }

        printf("Case #%d: %d\n",id,ans);
    }
	return 0;
}
