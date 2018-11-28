#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<iostream>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<stack>
#define LL long long
using namespace std;
const int M =1e3+5;
char s[M];
char ans[M*2];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("check.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        scanf("%s",s);
        int n=strlen(s);
        int l=n-1,r=n;
        ans[l--]=s[0];
        for(int j=1;j<n;j++){
            if(s[j]>=ans[l+1]){
                ans[l--]=s[j];
            }
            else{
                ans[r++]=s[j];
            }
        }
        printf("Case #%d: ",cas++);
        for(int j=l+1;j<r;j++) printf("%c",ans[j]);
        printf("\n");
    }
    return 0;
}
