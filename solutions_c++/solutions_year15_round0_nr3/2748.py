#include<set>
#include<stdio.h>
#include<string.h>
int mult[4][4] = {4,1,2,3,1,-4,3,-2,2,-3,-4,1,3,2,-1,-4};
char compute(char* s,int n){
    int now = 4;
    for(int i=0;i<n;i++){
        if(now>0){
            now = mult[now%4][s[i]];
        }
        else{
            now = -mult[(-now)%4][s[i]];
        }
    }
    return now;
}
int main() {
    int T,m,n,amin,l,x;
    char bye;
    scanf("%d",&T);
    char ans[5];
    for(int t=0;t<T;t++){
        scanf("%d %d",&l,&x);
        char str[l+1];
        char strn[x*l+1];
        scanf("%s",str);
        strcpy(strn,str);
        for(int i=1;i<x;i++) strcat(strn,str);
        for(int i=0;i<l*x;i++) strn[i]-='h';
        char r = compute(strn,l*x);
        if(r!=-4){
            strcpy(ans,"NO");
        }
        else{
            char fnow = 4;
            int k;
            int j;
            for(k=0;k<l*x;k++){
                if(fnow>0){
                    fnow = mult[fnow%4][strn[k]];
                }
                else{
                    fnow = -mult[(-fnow)%4][strn[k]];
                }
                if(fnow==1) break;
            }
            //printf("%dhey\n",k);
            if(k==l*x) strcpy(ans,"NO");
            else{
                char fmid = 4;
                for(j=k+1;j<l*x;j++){
                    if(fmid >0){
                        fmid  = mult[fmid%4][strn[j]];
                    }
                    else{
                        fmid  = -mult[(-fmid)%4][strn[j]];
                    }
                    if(fmid==2) break;
                }
                if(j==l*x) strcpy(ans,"NO");
                else strcpy(ans,"YES");
            }
        }
        printf("Case #%d: %s\n",t+1,ans);
    }
    return 0;
}


