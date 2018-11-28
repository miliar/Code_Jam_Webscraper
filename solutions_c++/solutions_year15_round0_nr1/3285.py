#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<queue>
#include<algorithm>
#include<set>
#define ll long long
using namespace std;
char s[10010];
int t,cas=1,n,sum,ans;
int main(){
    freopen("A-large (2).in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        scanf("%s",s);
        sum=ans=0;
        for(int i=0;i<strlen(s);i++){
            if(sum<i) {
                ans+=i-sum;
                sum+=i-sum+s[i]-'0';
            }
            else sum+=s[i]-'0';
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}
