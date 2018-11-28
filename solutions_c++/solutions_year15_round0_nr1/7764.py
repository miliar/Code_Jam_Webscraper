#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef long long LL;

const int MAXN=1010;
const int MAXNODE=MAXN*4;
const LL MOD=1000000007;

int T,N;
char str[MAXN];

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    int cas=0;
    while(T--){
        scanf("%d",&N);
        scanf("%s",str);
        int ans=0,t=0,cnt=0;
        for(int i=0;i<=N;i++){
            if(i>cnt){
                ans+=i-cnt;
                cnt+=i-cnt;
            }
            t=str[i]-'0';
            cnt+=t;
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
