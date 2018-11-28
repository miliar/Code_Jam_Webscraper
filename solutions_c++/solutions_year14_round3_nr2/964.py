// Author : Muhammad Rifayat Samee
// Problem :B
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7
#define mod 1000000007

#define i64 long long

using namespace std;
struct Node{
    char str[105];

}N[15];
i64 memo[1<<15][15];
i64 done[1<<15][15],cc=1;
i64 n,m;

i64 isposs(i64 mask,i64 prev,i64 cur){
    i64 i,j,len;
    i64 f[27];
    memset(f,0,sizeof(f));
    for(i=0;i<n;i++){
        if(mask&(1<<i)){
            len = strlen(N[i].str);
            for(j=0;j<len;j++){
                f[N[i].str[j] - 'a'] = 1;
            }
        }
    }
    len = strlen(N[prev].str);
    char last = N[prev].str[len-1];
    len = strlen(N[cur].str);
    //printf("last %c\n",last);
    //printf("--%d\n",f['c'-'a']);
    i64 fa = 0;
    for(j=0;j<len && N[cur].str[j]==last;j++){
       //printf("%d cur %c %c\n",i,N[cur].str[i],last);
    }
    for(i=j;i<len;i++){
        //printf("%d cur %c %lld\n",i,N[cur].str[i],f[N[cur].str[i]-'a']);
        if(f[N[cur].str[i] - 'a'])return 0;
    }
    return 1;
}

i64 dp(i64 mask,i64 prev){
    if(mask == ((1<<n)-1)){
        //printf("---\n");
        return 1;
    }
    if(done[mask][prev]==cc)
        return memo[mask][prev];
    //printf("--%d %lld\n",mask,prev);
    i64 i,res = 0;
    if(mask == 0){
        for(i=0;i<n;i++){
            res  = (res + dp(mask|(1<<i),i))%mod;
        }
    }
    else{
        for(i=0;i<n;i++){
            if((mask&(1<<i))==0){
                if(isposs(mask,prev,i)){
                    res = (res + dp(mask|(1<<i),i))%mod;
                }
            }
        }
    }
    done[mask][prev] = cc;
    memo[mask][prev] = res;
    return res;
}

int main(){

	freopen("B.in","r",stdin);
	freopen("ans.out","w",stdout);
    i64 cases,i,j,k,c,ct=1;
    char str[105];
    scanf("%lld",&cases);
    while(cases--){
        scanf("%lld",&n);
        for(i=0;i<n;i++){
            scanf("%s",N[i].str);
        }
        int f = 0;
        for(i=0;i<n;i++){
            int len = strlen(N[i].str);
            for(j=0;j<len;j++){
                for(k=j+1;k<len&&N[i].str[j]== N[i].str[k];k++){}
                for(c=k;c<len;c++){
                    if(N[i].str[j]== N[i].str[c])f = 1;
                }
            }
        }

        //printf("%d\n",isposs(2,1,0));
        i64 res;
        if(f==1)res = 0;
        else
            res = dp(0,0);
        printf("Case #%lld: %lld\n",ct++,res);
        cc++;

    }
	return 0;
}
