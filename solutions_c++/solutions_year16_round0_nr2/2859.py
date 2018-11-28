#include<cstdio>
#include<cstring>
#include<cstdlib>

char s[110];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,tc,n,m,i;
    scanf("%d",&T);
    for(tc=1;tc<=T;++tc){
        scanf("%s",s);
        n=0;
        m=strlen(s);
        for(i=m-1;i>=0;--i){
            if(s[i]=='-'){
                n+=1;
                i-=1;
                break;
            }
        }
        while(i>=0){
            if(s[i] != s[i+1]){
                n+=1;
            }
            i-=1;
        }
        printf("Case #%d: %d\n",tc,n);
    }
    return 0;

}
