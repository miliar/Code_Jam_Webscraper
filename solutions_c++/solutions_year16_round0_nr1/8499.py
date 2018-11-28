#include <stdio.h>

int main(){
    int a;
    //freopen("input.in","r",stdin);
    //freopen("input.out","w",stdout);
    scanf("%d",&a);
    bool ans;
    int num;
    for(int i = 0; i < a;i++){
        int b;
        bool arr[10] = {false};
        scanf("%d",&b);
        int x = 1;
        int prev = 1;

        while(x){
            num = b*prev;
            int l;

            for(int i = 1; i <= num;i*=10){
                arr[(num%(i*10))/i] = true;
            }
            for( l = 0; l < 10;l++){
                if(!arr[l])break;

            }
            if(l== 10){
                 x = 0;
                 ans = true;
                 continue;
            }
            prev++;
            if( b*prev == num){
                ans = false;
                break;
            }

        }
        printf("Case #%d: ",i+1);
        if(ans) printf("%d\n",num);
        else printf("INSOMNIA\n");
    }
    return 0;
}
