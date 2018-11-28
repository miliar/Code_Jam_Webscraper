#include<stdio.h>
int main(void){
    freopen("B-large.in", "r",stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    int i;
    scanf("%i", &T);
    char s[120];
    char c;
    int l;
    scanf("%c", &c);
    for(l=0;l<T;l++){
        int i;
        int N;
        int j;
        for(i=0;;i++){
            scanf("%c", &s[i]);
            if(s[i]=='\n'){N=i; break;}
        }
        int res=0;
        while(N>0){
            if(s[N-1]=='+') N--;
            else{
                res++;
                N--;
                for(j=0;j<N;j++){
                    if(s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
            }
        }
        printf("Case #%i: %i\n",l+1, res);
    }
    return 0;
}
