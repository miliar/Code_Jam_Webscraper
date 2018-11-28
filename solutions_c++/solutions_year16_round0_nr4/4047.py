#include<cstdio>

int main(){
    int t;
    scanf("%d", &t);
    for(int i=0;i<t;i++){
        printf("Case #%d: ", i+1);
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        for(int j=0;j<k;j++){
            printf("%d ", j+1);
        }
        printf("\n");
    }
}
