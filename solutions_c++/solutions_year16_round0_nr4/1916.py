#include <bits/stdc++.h>

using namespace std;

#define FOR(i,x,y)  for(int i = x;i < y;++ i)

int k,c,s;

int main(){
    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("D-small-attempt0.out","w",stdout);
    int T,tCase = 0;    scanf("%d",&T); 
    while(T--){
        printf("Case #%d:",++tCase);
        scanf("%d%d%d",&k,&c,&s);
        FOR(i,1,s+1)    printf(" %d",i);
        printf("\n");
    }
    return 0;
}
