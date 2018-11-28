#include<cstdio>
int a,b,c;
int main(){
    int t,n,cnt;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int turn=1;turn<=t;turn++){
        scanf("%d %d %d",&a,&b,&c);
        printf("Case #%d:",turn);
        for(int i=1;i<=a;i++) printf(" %d",i);
        printf("\n");
    }
}
