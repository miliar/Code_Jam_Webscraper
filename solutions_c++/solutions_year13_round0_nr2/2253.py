#include <stdio.h>
#define MAXN 105
using namespace std;

inline int Max(int a, int b){ return (a>b?a:b); }

int X[MAXN];
int Y[MAXN];

int mapa[MAXN][MAXN];

int main(){
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        bool chosto=true;
        printf("Case #%d: ",i);
        int a,b;
        scanf("%d %d",&a,&b);
        for(int j=1;j<=a;j++)
            for(int k=1;k<=b;k++)
                scanf("%d",&mapa[j][k]);
        for(int j=1;j<=100;j++)
            X[j]=Y[j]=0;
        for(int j=1;j<=a;j++){
            int maxi=0;
            for(int k=1;k<=b;k++){
                maxi=Max(maxi,mapa[j][k]);
            }
            if(Y[j]==0){
                Y[j]=maxi;
            }else if(Y[j]!=maxi) chosto=false;
            for(int k=1;k<=b;k++){
                if(mapa[j][k]!=maxi){

                    if(X[k]==0){
                        X[k]=mapa[j][k];
                    }else if(X[k]!=mapa[j][k]) chosto=false;
                }
            }
        }
        for(int j=1;j<=b;j++){
            int maxi=0;
            for(int k=1;k<=a;k++){
                maxi=Max(maxi,mapa[k][j]);
            }
            if(X[j]==0){
                X[j]=maxi;
            }else if(X[j]!=maxi) chosto=false;
            for(int k=1;k<=a;k++){
                if(mapa[k][j]!=maxi){

                    if(Y[k]==0){
                        Y[k]=mapa[k][j];
                    }else if(Y[k]!=mapa[k][j]) chosto=false;
                }
            }
        }
        if(chosto)
            printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
