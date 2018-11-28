#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<limits.h>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-9
#define asdf exit(0);


typedef long long LL;





int a[10010];
int cnt[1000];
int main()
{
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int T,cs,i,j,k,n,x;


    scanf("%d",&T);

    for(cs=1;cs<=T;cs++)
    {
        printf("Case #%d: ",cs);

        scanf("%d %d",&n,&x);


        memset(cnt,0,sizeof(cnt));
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            cnt[a[i]]++;
        }

        int ans=0;


        while(n)
        {
            ans++;
            for(i=700;i>=0;i--)
            {
                if(cnt[i]) break;
            }
            cnt[i]--;
            n--;


            j=i;
            if(n==0) break;

            for(i=700;i>=0;i--)
            {
                if(cnt[i] && (i+j)<=x ) break;
            }
            if(i>=0)
            {
                cnt[i]--;
                n--;
            }
        }



        printf("%d\n",ans);
    }
    return 0;
}
