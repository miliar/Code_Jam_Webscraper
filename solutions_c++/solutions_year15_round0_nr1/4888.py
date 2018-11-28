#include<cstdio>
#include<iostream>
#include<cstring>
#include<ctime>
#include<queue>
#include<stack>
#include<stdlib.h>
#include<cmath>
#include<algorithm>
#include<map>
#define lowbit(x) (x)&(-x)
#define maxn 1000010
#define ls (o)<<1
#define rs ((o)<<1)|1
#define mod 142857
typedef long long ll;
using namespace std;
#define N 40000
int a,b,dp[maxn],prime[maxn],flag[maxn]={1,1,0},cnt=0;
void get_prime()
{
    for(int i=2;i<maxn;i++){
        if(!flag[i])prime[cnt++]=i;
        for(int j=0;j<cnt&&prime[j]*i<maxn;j++){
            flag[prime[j]*i]=1;
        }
    }
}
void dfs()
{
    int t;
    scanf("%d",&t);
    if(t==0)return;
    dfs();
    printf("%d ",t);
}
bool cmp(int a,int b)
{
    return a>b;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    char a[1005];
    int t,s,p=0;
    scanf("%d",&t);
    while(p++<t){
        scanf("%d%s",&s,a);
        int need,stand=a[0]-'0',ans=0;
        for(int i=1;i<s+1;i++){
            need = i;
            if(stand<need){
                ans+=need-stand;
                stand=need+a[i]-'0';
            }
            else stand+=a[i]-'0';
        }
        printf("Case #%d: %d\n",p,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
