#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef pair <int,int>  PII;
#define FOR(i,x,y)  for(int i = x;i < y;++ i)
#define IFOR(i,x,y) for(int i = x;i > y;-- i)
#define pb  push_back
#define mp  make_pair
#define fi  first
#define se  second

const int maxn = 110;
int dp[maxn];
char str[maxn];

void work(){
    int cnt = 0,len = strlen(str);
    char cur = str[0];
    cnt ++;
    FOR(i,1,len){
        if(str[i] != cur){
            cur = str[i];
            cnt ++; 
        }
    }
    if(str[len-1] == '-')   printf("%d\n",cnt);
    else    printf("%d\n",cnt-1);
}

int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int T,tCase = 0;  scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++tCase);
        scanf("%s",str);
        work();
    }
    return 0;
}
