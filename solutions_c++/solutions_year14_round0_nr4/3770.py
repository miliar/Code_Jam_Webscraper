#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

    int loop=0;
    int i=0;
    int j=0;
    //int k=0;
    int tamanho=0;
    int iniN=0;
    int iniK=0;
    int fimN=0;
    int fimK=0;

    //pontos WAR
    int y=0;

    //pontos DECEITFUL WAR
    int z=0;

    double temp=0.00000;

    scanf("%d", &loop);

    for(i=0;i<loop;i++){

        scanf("%d", &tamanho);

        vector<double> vN;

        for(j=0;j<tamanho;j++){
            scanf("%lf", &temp);
            vN.push_back(temp);
        }

        vector<double> vK;

        for(j=0;j<tamanho;j++){
            scanf("%lf", &temp);
            vK.push_back(temp);
        }

        sort(vN.begin(), vN.end());
        sort(vK.begin(), vK.end());

        // PRINT VECTORS AREA
        /*
        for(j=0;j<vK.size();j++){
            cout << vN[j] << " ";
        }
        cout << "\n";

        for(j=0;j<vN.size();j++){
            cout << vK[j] << " ";
        }
        cout << "\n";
        */

        //WAR
        iniN=0;
        iniK=0;
        fimN=tamanho-1;
        fimK=tamanho-1;
        temp=0.00000;
        z=0;
        while(iniN<=fimN){

            //printf("Inicio: iniN:%d | iniK:%d | fimN: %d | fimK: %d | temp: %lf\n", iniN, iniK, fimN, fimK, temp);
            //printf("Inicio: vN[iniN]:%lf | vN[fimN]:%lf | vK[iniK]:%lf | vK[fimK]:%lf | z: %d \n", vN[iniN], vN[fimN], vK[iniK], vK[fimK], z);

            temp=vN[fimN];
            fimN=fimN-1;

            if(vK[fimK]>temp) fimK=fimK-1;
            else{
                iniK=iniK+1;
                z=z+1;
            }

            //printf("Fim: iniN:%d | iniK:%d | fimN: %d | fimK: %d | temp: %d\n", iniN, iniK, fimN, fimK, temp);
            //printf("Fim: vN[iniN]:%lf | vN[fimN]:%lf | vK[iniK]:%lf | vK[fimK]:%lf | z: %d \n", vN[iniN], vN[fimN], vK[iniK], vK[fimK], z);
            //printf("\n");
        }

        //DECEITFUL WAR
        iniN=0;
        iniK=0;
        fimN=tamanho-1;
        fimK=tamanho-1;
        temp=0.00000;
        y=0;

        while(iniN<=fimN){
            if(vN[iniN]<vK[iniK]){
                iniN=iniN+1;
                temp = vK[fimK]-0.00001;
                for(j=0;j<tamanho;j++){
                    if(vK[j]==temp){
                        temp=temp-0.00001;
                        j=0;
                    }
                }
                if(vK[fimK]>temp) fimK=fimK+1;
            }
            else{
                iniN=iniN+1;
                temp=vK[fimK]+0.00001;
                if(vK[fimK]<temp){
                    iniK=iniK+1;
                    y=y+1;
                }
            }
        }
        /*
        while(iniN<=fimN){

            //printf("Inicio: iniN:%d | iniK:%d | fimN: %d | fimK: %d | temp: %lf\n", iniN, iniK, fimN, fimK, temp);
            //printf("Inicio: vN[iniN]:%lf | vN[fimN]:%lf | vK[iniK]:%lf | vK[fimK]:%lf | y: %d \n", vN[iniN], vN[fimN], vK[iniK], vK[fimK], y);

            if(vN[fimN]>vK[fimK]){
                fimN=fimN-1;
                iniK=iniK+1;
                y=y+1;
            }
            else{
                temp=vK[fimK]-0.00001;
                for(j=0;j<tamanho;j++){
                    if(vK[i]==temp){
                        temp=temp-0.00001;
                        j=0;
                    }
                }
                iniN=iniN+1;
                if(vK[fimK]>temp){
                    fimK=fimK-1;
                }
                else{
                    //printf("erro!\n");
                    iniK=iniK+1;
                }
            }

            //printf("Fim: iniN:%d | iniK:%d | fimN: %d | fimK: %d | temp: %lf\n", iniN, iniK, fimN, fimK, temp);
            //printf("Fim: vN[iniN]:%lf | vN[fimN]:%lf | vK[iniK]:%lf | vK[fimK]:%lf | y: %d \n", vN[iniN], vN[fimN], vK[iniK], vK[fimK], y);
            //printf("\n");

        }
        */

        printf("Case #%d: %d %d\n", i+1, y, z);

    }

}
