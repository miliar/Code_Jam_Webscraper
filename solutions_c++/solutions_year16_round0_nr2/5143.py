#include<cstdio>
#include<cstring>
int main(){
    int n,len,sum=0;
    char str[1000],cur_char,prev_char;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%s",str);
        len = strlen(str);
        sum=0;
        prev_char=str[0];
        for(int j=1;j<len;j++){
            cur_char=str[j];
            if(cur_char != prev_char){
                sum++;
            }
            prev_char=cur_char;
        }
        if(prev_char=='-')sum++;
        printf("Case #%d: %d\n",i+1,sum);
    }
    return 0;
}
