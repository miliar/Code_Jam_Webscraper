#include<bits/stdc++.h>
using namespace std;
#define Enter putchar(10)
#define Space putchar(32)
#define MAX(x,y) (((x)>(y))?(x):(y))
#define MIN(x,y) (((x)<(y))?(x):(y))
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sqr(x) ((x)*(x))
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef long long ll;
typedef unsigned long long ull;
template<typename N>N gcd(N a,N b){return b?gcd(b,a%b):a;}
template<typename N>inline int sgn(N a){return a>0?1:(a<0?-1:0);}
const int dx[5]={1,0,-1,0,0},dy[5]={0,1,0,-1,0};
const double pi=acos(-1);
const double eps=1e-8;
const int maxn=1e5+7;
void getre(){int x=0;printf("%d\n",1/x);}
void gettle(){int res=1;while(1)res<<=1;printf("%d\n",res);}
void getole(){char ole[1<<16];for(int i=0;i<1<<16;++i){ole[i]='o';}while(1)puts(ole);}
void getwa(){printf("wawawawawawawawaawa\n");}

int T;
char s[maxn];
int k;
queue<int> que;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("data.out","w",stdout);
#endif
    scanf("%d\n",&T);
    int ans;
    for (int ti=1;ti<=T;++ti){
        scanf("%s",s);
        scanf("%d",&k);
        printf("Case #%d: ",ti);
        ans=0;
        int len=strlen(s);
        while(!que.empty()) que.pop();
        bool flips=0;
        for(int i=0;i+k-1<len;++i){
            if(!que.empty()&&que.front()<i-k+1) que.pop(),flips=!flips;
            if(s[i]=='-'^flips){
                flips=!flips;
                ans++;
                que.push(i);
//                printf("%d\n",i);
            }
        }
        bool can=1;
        for(int i=len-k+1;i<len;++i){
            if(!que.empty()&&que.front()<i-k+1) que.pop(),flips=!flips;
            if(s[i]=='-'^flips){can=0;break;}
        }
        if(can) printf("%d\n",ans);
        else puts("IMPOSSIBLE");
    }
	return 0;
}


