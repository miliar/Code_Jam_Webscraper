#include<cstdio>

int z,n,m;
int t[100][100];
int tabimax[100];
int tabjmax[100];

int main(){
    scanf("%d", &z);
    int k = 0;
    while(z--){
        k++;
        scanf("%d %d", &n,&m);
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                scanf("%d", &t[i][j]);
                if(tabimax[i] < t[i][j]) tabimax[i] = t[i][j];
                if(tabjmax[j] < t[i][j]) tabjmax[j] = t[i][j];
            }
        }
        bool x = true;
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                if((t[i][j] < tabimax[i]) && (t[i][j] < tabjmax[j])){
                    x = false;
                }
            }
        }
        if(x){
            printf("Case #%d: YES\n", k);
        }else{
            printf("Case #%d: NO\n", k);
        }
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                t[i][j] = 0;
                tabimax[i] = 0;
                tabjmax[j] = 0;
            }
        }
    }
}
