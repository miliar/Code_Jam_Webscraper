#include<cstdio>

const int MAXNM = 100;
int map[MAXNM][MAXNM];

int noc,n,m;

int main(){
    scanf("%d",&noc);
    for (int tnoc=1;tnoc<=noc;++tnoc){
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;++i){
            for (int j=0;j<m;++j){
                scanf("%d",&map[i][j]);
            }
        }
        bool res = true;
        for (int i=0;i<n;++i){
            for (int j=0;j<m;++j){
                bool b1 = true;
                for (int k=0;k<n;++k){
                    if (map[k][j]>map[i][j]){
                        b1 = false;
                        break;
                    }
                }
                bool b2 = true;
                for (int k=0;k<m;++k){
                    if (map[i][k]>map[i][j]){
                        b2 = false;
                        break;
                    }
                }
                if ((!b1)&&(!b2)){
                    res = false;
                    break;
                }
            }
            if (!res){
                break;
            }
        }
        printf("Case #%d: %s\n",tnoc,(res)?"YES":"NO");
    }
    return 0;
}
