#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
    //freopen("in.txt","r",stdin);
    int t;
    scanf("%d",&t);
    int m[4][4];
    int numLinea, coincidencias, res;
    vector<int> uno,dos;
    /*Repetir para todos los casos*/
    for(int i=0;i<t;i++){
        /*Inicializar para cada caso*/
        for(int p=0;p<4;p++){
            for(int q=0;q<4;q++)
                m[p][q] = 0;
        }
        uno.clear();
        dos.clear();
        coincidencias = 0;
        /*Leer las 2 matrices*/
        for(int v=0;v<2;v++){
            scanf("%d",&numLinea);
            //printf("Linea: %d\n",numLinea);
            for(int l=0;l<4;l++){
                for(int j=0;j<4;j++)
                    scanf("%d",&m[l][j]);
            }
            /*for(int l=0;l<4;l++){
                for(int j=0;j<4;j++)
                    printf("%d ",m[l][j]);
                printf("\n");
            }*/
            /*Guardar las lineas en los vectors*/
            for(int k=0;k<4;k++){
                if(v==0)
                    uno.push_back(m[numLinea-1][k]);
                else dos.push_back(m[numLinea-1][k]);
            }
            /*printf("Vector:\n");
            for(int k=0;k<4;k++){
                if(v==0)
                    printf("%d ",uno[k]);
                else printf("%d ",dos[k]);
            }
            printf("\n");*/
        }
        for(int r=0;r<4;r++){
            for(int w=0;w<4;w++){
                if(uno[r]==dos[w]){
                    coincidencias++;
                    res = uno[r];
                }
            }
        }
        printf("Case #%d: ",i+1);
        if(coincidencias==1)
            printf("%d\n", res);
        else if(coincidencias!=0)
            printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
    return 0;
}
