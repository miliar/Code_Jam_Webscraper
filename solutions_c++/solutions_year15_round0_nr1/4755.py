#include<stdio.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<queue>
#include<string.h>
#include<stdlib.h>
using namespace std;
#define pi acos(-1.0)
#define maxn 1005
char s[maxn];
int main(){
    int T;
    int cas=1;
    scanf("%d",&T);
    while(T--){
        int n,ans=0,sum=0,all=0;
        scanf("%d",&n);
        scanf("%s",s);
        for(int i=0;i<=n;i++) all+=s[i]-'0';
        for(int i=0;i<=n;i++){
            if(sum<i&&sum<all+ans) {ans+=i-sum;sum=i;}
            if(sum>=i) sum+=s[i]-'0';
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}