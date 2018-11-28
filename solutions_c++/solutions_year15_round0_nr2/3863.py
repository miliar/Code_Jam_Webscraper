#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>
#include<queue>
#include<cmath>
#include<map>
#include<stack>
#include<bitset>
using namespace std;
#define REPF( i , a , b ) for ( int i = a ; i <= b ; ++ i )
#define REP( i , n ) for ( int i = 0 ; i < n ; ++ i )
#define CLEAR( a , x ) memset ( a , x , sizeof a )
typedef long long LL;
typedef pair<int,int>pil;
const int INF = 0x3f3f3f3f;
const int maxn=1100;
int d[maxn];
int t,n;
int main()
{
//    freopen("D:\\360Downloads\\B-small-attempt1.in","r",stdin);
//    freopen("F:\\ANS\\out.txt","w",stdout);
    scanf("%d",&t);int cas=1;
    while(t--)
    {
        scanf("%d",&n);int sum=0;
        REPF(i,1,n)
        {
            scanf("%d",&d[i]);
            sum+=d[i];
        }
        sort(d+1,d+1+n);
        int ans=sum;
        for(int i=0;i<=sum;i++)
        {
            for(int j=i;j>=(int)ceil(i*1.0/n);j--)
            {
                int sy=i-j;
                int temp=(int)ceil(d[n]*1.0/(j+1));
                for(int k=n-1;k>=1;k--)
                {
                    if(sy==0)
                    {
                        temp=max(temp,d[k]);
                        break;
                    }
                    if(sy>=j)
                    {
                        sy-=j;
                        temp=max(temp,(int)ceil(d[k]*1.0/(j+1)));
                    }
                    else
                    {
                        temp=max(temp,(int)ceil(d[k]*1.0/(sy+1)));
                        sy=0;
                    }
                }
                ans=min(ans,temp+i);
            }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
