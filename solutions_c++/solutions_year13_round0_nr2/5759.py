#include <cstdio>
#include <string.h>


int matrix[11][11];
int transform[11][11];
int n,m;

void corteh (int k){
    int cont=0;
    for (int s=0;s<n;++s){
        cont=0;
        for (int j=0;j<m;++j){
            if (matrix[s][j]<=k){
                cont++;
            }
            
        }
        if (cont==m){
             for (int j=0;j<m;++j){
                transform[s][j]=k;
        }
    }
    
}
}

void cortev (int k){
    int cont=0;
    for (int s=0;s<m;++s){
        cont=0;
        for (int j=0;j<n;++j){
            if (matrix[j][s]<=k){
                cont++;
            }
            
        }
        if (cont==n){
             for (int j=0;j<n;++j){
                transform[j][s]=k;
        }
    }
    
}
}

int main(){
    int t;
    scanf("%d",&t);
    
    for (int i=1;i<=t;++i){
        printf("Case #%d: ",i);
        
        scanf("%d %d",&n,&m);
        
        for (int o=0;o<n;++o){
            for (int s=0;s<m;++s){
                int dd;
                scanf("%d",&dd);
                matrix[o][s]=dd;
            }
        }
        
        memset(transform,100,sizeof(transform));
        
        for (int k=2;k>0;--k){
            
            corteh(k);
            cortev(k);
            
        }
        bool identico=true;
           for (int o=0;o<n;++o){
            for (int s=0;s<m;++s){
                if (matrix[o][s]!=transform[o][s]){
                identico=false;
                
                }
            }
        }
        
        if (identico)
        printf("YES\n");
        else
        printf("NO\n");
    }
    
    return 0;
}