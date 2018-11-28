#include <cstdio>
inline int max(int a, int b){
    return a>b?a:b;
}

int t[102][102], n;
struct p{
    int l,p,g,d;
    void zero(){
        l = p = g = d = 0;
    }
} w[102][102];
void alg(int i){

    int a,b;
    scanf("%d%d", &a, &b);
    for(int j = 1; j<=a; j++){
        t[j][b+1] = 0;
        w[j][b+1].zero();
        for(int k=1; k<=b; k++){
            scanf("%d", &t[j][k]);
            t[a+1][k] = 0;
            w[a+1][k].zero();
        }
    }
    t[a+1][b+1] = 0;
    w[a+1][b+1].zero();
    for(int j = 1; j<=a; j++){
        for(int k = 1; k<=b; k++){
            w[j][k].g = max(t[j][k], w[j-1][k].g);
            w[j][k].p = max(t[j][k], w[j][k-1].p);
        }
    }

    for(int j = a; j>0; j--){
        for(int k = b; k>0; k--){
            w[j][k].d = max(t[j][k], w[j+1][k].d);
            w[j][k].l = max(t[j][k], w[j][k+1].l);
        }
    }
    /*
    printf("---------\n");
    for(int j=0; j<=a; j++){
        for(int k=0; k<=b; k++){
            printf("%d ", w[j][k].l);
        }
        printf("\n");
    }
    printf("---------\n");
    for(int j=0; j<=a; j++){
        for(int k=0; k<=b; k++){
            printf("%d ", w[j][k].g);
        }
        printf("\n");
    }
    printf("---------\n");
    for(int j=0; j<=a; j++){
        for(int k=0; k<=b; k++){
            printf("%d ", w[j][k].p);
        }
        printf("\n");
    }
    printf("---------\n");
    for(int j=0; j<=a; j++){
        for(int k=0; k<=b; k++){
            printf("%d ", w[j][k].d);
        }
        printf("\n");
    }

    printf("---------\n");
    printf("---------\n");
    */
    for(int j=0; j<=a; j++){
        for(int k = 0; k<=b; k++){
            if((w[j][k].l>t[j][k] || w[j][k].p>t[j][k]) && (w[j][k].g>t[j][k] || w[j][k].d>t[j][k])){

                printf("Case #%d: NO\n", i);
                return;
            }
        }
    }
    
    printf("Case #%d: YES\n", i);
}


int main(){

    scanf("%d", &n);
    for(int i=0; i<n; i++){
        alg(i+1);
    }
    return 0;
}
