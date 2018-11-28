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
char str[maxn];
int t,n;

int main()
{
//    freopen("D:\\360Downloads\\A-large.in","r",stdin);
//    freopen("F:\\ANS\\out.txt","w",stdout);
    int len;int cas=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%s",&len,str);
        len=strlen(str);
        int sum=0,ans=0;
        REPF(i,0,len)
        {
            if(sum>=i)
                sum+=str[i]-'0';
            else
            {
                ans+=i-sum;
                sum=(i+str[i]-'0');
            }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
