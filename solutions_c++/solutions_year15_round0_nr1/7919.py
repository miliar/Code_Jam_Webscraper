#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,t,m;
    char peo[1005];
    cin>>t;
    for(int cas=1;cas<=t;cas++){
        int k=0;  //当前站起来的人数
        int ans=0;
        scanf("%d %s",&m,peo);
        for(i=0;i<strlen(peo);i++){
            int a=peo[i]-'0';
            if(k<i) ans+=i-k,k=i;
            k+=a;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
