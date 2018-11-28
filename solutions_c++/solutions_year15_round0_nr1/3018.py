#include<stdio.h>
int main(){
    int T;scanf("%d",&T);
    for(int _ = 0 ; _ < T; _++){
        int n;scanf("%d",&n);getchar();
        int sum = 0, ans = 0;
        for(int i = 0; i <= n;i++){
            char ch;
            scanf("%c",&ch);
            ch -='0';
            if(i > sum && ch > 0){
                ans += i-sum;
                sum += i-sum;
                //printf("ans = %d\n",ans);
            }
            sum += ch;
        }
        printf("Case #%d: %d\n",_+1, ans);
    }
    return 0;
}
