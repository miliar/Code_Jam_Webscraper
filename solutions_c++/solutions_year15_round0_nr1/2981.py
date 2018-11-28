#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<queue>
#include<algorithm>
#include<set>
#define ll long long
using namespace std;
char str[100100];
int main(){
    int t,cas=1;
    freopen("1.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        int n,ans=0,sum=0;
        scanf("%d",&n);
        scanf("%s",str);
        for(int i=0;i<=n;i++){
            if(sum<i) {
                ans+=i-sum;
                sum+=str[i]-'0'+i-sum;
            }
            else sum+=str[i]-'0';
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}
