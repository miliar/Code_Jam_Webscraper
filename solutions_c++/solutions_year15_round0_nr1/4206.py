#include<set>
#include<stdio.h>


int main() {
    int T,m,n,smax;
    char bye;
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        scanf("%d",&smax);
        char s[smax+1];
        //int t[smax+1];
        scanf("%s",s);
        //scanf("%c",&bye);
        int required = 0;
        int stdnow = s[0]-'0';
        //printf("%d-",stdnow);
        for(int i=1;i<=smax;i++){
            //printf("%d-",s[i]-'0');
            if(stdnow>=i) stdnow+=(s[i]-'0');
            else if(s[i]-'0'>0){
                required += (i-stdnow);
                stdnow = i+(s[i]-'0');
            }
            //printf("i = %d , s[i] = %d , stdnow = %d , required = %d \n",i,s[i]-'0',stdnow,required);
        }
        //printf("\n");
        printf("Case #%d: %d\n",t+1,required);
    }
    return 0;
}

