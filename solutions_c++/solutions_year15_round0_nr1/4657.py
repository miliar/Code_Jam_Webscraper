#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<cmath>
#include<deque>
#include<time.h>
#pragma comment(linker, "/STACK:1024000000,1024000000")
using namespace std;
#define cl(x,v); memset(x,v,sizeof(x));
#define llINF 1ll<<60
#define INF 1<<29
#define EPS 1e-8
#define MID int mid=(l+r)>>1; int ls=o<<1; int rs=o<<1|1;
#define pii pair<int,int>
#define pli pair<long long,int>
#define pll pair<long long,long long>
#define pss pair<short,short>
#define F first
#define S second
#define PB push_back
#define BR puts("");
#define SCn scanf("%d",&n)
#define SCnm scanf("%d%d",&n,&m)
#define rep(i,s,n) for(int i=(s);i<=(n);++i)
#define rrep(i,s,n) for(int i=(s);i>=(n);--i)
#define TSC int T; scanf("%d",&T);
#define PI acos(-1.0)
#define test printf("test\n");
#define db double
typedef unsigned long long ull;
typedef long long ll;
int n;
char str[1005];
int main()
{
    int T;
    scanf("%d",&T);
    int Case=1;
    while(T--)
    {
        scanf("%d%s",&n,str);
        int len=strlen(str);
        int ans=0;
        int temp=0;
        for(int i=0;i<len;i++){
            if(str[i]=='0')continue;
            if(temp>=i){
                temp+=str[i]-'0';
            }else{
                ans+=i-temp;
                temp=str[i]-'0'+i;
            }
           // printf("%d %d %d\n",i,temp,ans);
        }
        printf("Case #%d: %d\n",Case++,ans);
    }
    return 0;
}
