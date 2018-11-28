#include<cstdio>
#include<algorithm>
using namespace std;
const int MAXN=1010;
int pos[MAXN];
int main(){
    int N;
    double Na[MAXN],Ke[MAXN];
    int pass[MAXN];
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        int T;
        scanf("%d",&T);
        int valw=T;
        int vald=0;
        for(int j=0;j<T;j++){
            scanf("%lf",&Na[j]);
            pass[j]=0;
        }    
        for(int j=0;j<T;j++){
            scanf("%lf",&Ke[j]);
        }
        sort(&Na[0],&Na[T]);
        sort(&Ke[0],&Ke[T]);
        int ini=0,fim=T;
        for(int j=0;j<T&&ini<fim;j++){
            if(Na[j]>Ke[ini]){
               ini++;     
               vald++;
            }    
            else fim--;
        }
        for(int j=0;j<T;j++){
            for(int k=0;k<T;k++){
                if(Na[j]<Ke[k]&&pass[k]==0){
                    pass[k]=1;
                    valw--;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",i+1,vald,valw);
    }
    
}
