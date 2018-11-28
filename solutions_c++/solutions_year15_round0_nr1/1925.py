#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

char c[2333];
int T,smax,snum[2333],ans,now;

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
for(int t=1;t<=T;t++){
    ans=now=0;
    scanf("%d",&smax);scanf("%s",c);
    for(int i=0;i<=smax;i++)snum[i]=c[i]-'0';
    for(int i=0;i<=smax;i++){
        if(now>=i)now+=snum[i];
        else{
            ans+=i-now;now=i+snum[i];
        }
    }
    printf("Case #%d: %d\n",t,ans);

}
    return 0;
}
