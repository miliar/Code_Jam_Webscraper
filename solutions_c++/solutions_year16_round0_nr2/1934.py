#include <cstdio>
#include <cstring>


const int maxn = 101;
char a[maxn];
int main(){
    int t;
    scanf("%d",&t);
    int at=0;
    for(int i=0;i<t;i++){
            scanf("%s",a);
            int len=strlen(a);
            char at=a[0];
            int change=1;
            for(int j=1;j<len;j++){ 
                    if(at!=a[j]){
                        change++;
                        at=a[j];    
                    }
            }
            if(a[len-1]=='+')printf("Case #%d: %d\n",i+1,change-1);
            else printf("Case #%d: %d\n",i+1,change);
    }    

}
