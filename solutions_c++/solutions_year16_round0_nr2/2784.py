#include<cstdio>
char str[102];
int main(){
    int t,n,cnt;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int turn=1;turn<=t;turn++){
        for(int i=0;i<=101;i++) str[i]='\0';
        scanf("%s",str);
        cnt=(str[0]=='-');
        for(int i=1;str[i]!='\0';i++){
            if(str[i-1]!=str[i]&&str[i]=='-'){
                cnt+=2;
            }
        }
        printf("Case #%d: %d\n",turn,cnt);
    }
}
