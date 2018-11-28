#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int T;
int s;
int main(){
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
        scanf("%d%d%d",&s,&s,&s);
        printf("Case #%d: ",cas);
        for (int i=1;i<s;i++) printf("%d ",i);printf("%d\n",s);
    }
    return 0;
}
