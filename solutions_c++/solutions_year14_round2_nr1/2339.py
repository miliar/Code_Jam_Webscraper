//RandomUsername(Nikola Jovanovic)
//Google CodeJam Round B1
//A

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#define MAXN 150
#define forr(i) for(int i=1;i<=r;i++)
#define forc(i) for(int i=1;i<=c;i++)

using namespace std;

struct str
{
    char x[MAXN];
    char h[MAXN];
    int cnt[MAXN];
};

str a[MAXN];
int itt=-1;

int aps(int x)
{
    if(x<0) return -x;
    return x;
}
int n;
int len;
int t;
        int pom[MAXN];
        int sum;
//USING GOTO HEHE
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        itt=-1;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%s",a[i].x);
            int len=strlen(a[i].x);
            int it=1;
            int cnt=1;
            a[i].h[it]=a[i].x[0];
            for(int j=1;j<len;j++)
            {
                if(a[i].x[j]!=a[i].x[j-1])
                {
                    a[i].cnt[it++]=cnt;
                    a[i].h[it]=a[i].x[j];
                    cnt=0;
                }
                cnt++;
            }
            //cout<<it<<endl;
            a[i].cnt[it]=cnt;
            if(itt==-1) itt=it;
            else if(itt!=it)
            {
                printf("Case #%d: Fegla Won\n",tt);
                goto exit;
            }
        }
        //uslo sve
        for(int i=2;i<=n;i++)
        {
            for(int j=1;j<=itt;j++)
            {
                if(a[i].h[j]!=a[i-1].h[j])
                {
                    printf("Case #%d: Fegla Won\n",tt);
                    goto exit;
                }
            }
        }
        sum=0;
        //nadji min
        for(int j=1;j<=itt;j++)
         {
             for(int i=1;i<=n;i++)
             {
                pom[i-1]=a[i].cnt[j];
             }
              sort(pom,pom+n);
             //pom[n/2]
             for(int i=0;i<n;i++)
             {
                 sum+=aps(pom[i]-pom[n/2]);
             }
         }
         printf("Case #%d: %d\n",tt,sum);
         exit: {}
         //cout<<"PRODJE"<<endl;
    }
    return 0;
}
