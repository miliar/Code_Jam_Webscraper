#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<iostream>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#define ULL unsigned long long
#define LL long long
using namespace std;
char s[105];
char A[3005];
int main(){
    freopen("data.in","r",stdin);
    freopen("check.out","w",stdout);
    A['+']=0;
    A['-']=1;
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        scanf("%s",s);
        int n=strlen(s);
        printf("Case #%d: ",cas++);
        int ans=0;
        for(int j=n-1;j>=0;j--){
            if((ans+A[s[j]])%2) ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
