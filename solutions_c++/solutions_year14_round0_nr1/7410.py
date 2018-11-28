//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<cmath>
#include<climits>
#include<string>
#include<map>
#include<queue>
#include<vector>
#include<stack>
#include<set>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
#define pb(a) push(a)
#define INF 0x1f1f1f1f
#define lson idx<<1,l,mid
#define rson idx<<1|1,mid+1,r
#define PI  3.1415926535898
template<class T> T min(const T& a,const T& b,const T& c) {
    return min(min(a,b),min(a,c));
}
template<class T> T max(const T& a,const T& b,const T& c) {
    return max(max(a,b),max(a,c));
}
void debug() {
#ifdef ONLINE_JUDGE
#else

    freopen("in.txt","r",stdin);
    //freopen("d:\\out1.txt","w",stdout);
#endif
}
int getch() {
    int ch;
    while((ch=getchar())!=EOF) {
        if(ch!=' '&&ch!='\n')return ch;
    }
    return EOF;
}

int vis[17];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
        memset(vis,0,sizeof(vis));
        const int n=4;
        for(int d=0;d<2;d++)
        {
            int r;
            scanf("%d",&r);
            for(int i=1;i<=n;i++)
            {
                for(int j=1;j<=n;j++)
                {
                    int a;
                    scanf("%d",&a);
                    if(r==i)
                        vis[a]++;
                }
            }
        }
        int cnt=0;
        int num;
        for(int i=1;i<=16;i++)
        {
            if(vis[i]>=2)
            {
                cnt++;
                num=i;
            }
        }
        printf("Case #%d: ",ca);
        if(cnt==1)
            printf("%d\n",num);
        if(cnt<1)
            printf("Volunteer cheated!\n");
        if(cnt>1)
            printf("Bad magician!\n");

    }
    return 0;
}
