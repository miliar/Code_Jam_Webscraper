#include<cstdio>
#include<cstring>
int main(){
    //freopen("in.txt","r",stdin);
    //freopen("B-small-attempt0.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    char pancake[200],np;
    scanf("%d\n",&T);
    for(int t=1;t<=T;t++){
        scanf("%s",pancake);
        //printf("%d>>%s",t,pancake);
        np=strlen(pancake);

        int cnt=0;
        for(int i=1;i<np;i++){
            if(pancake[i-1]!=pancake[i]) cnt++;
        }
        if(pancake[np-1]=='-') cnt++;
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}
