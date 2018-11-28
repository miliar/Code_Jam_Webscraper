#include <iostream>
#include <stdio.h>

using namespace std;

int prov1[4][4], prov2[4][4],aux[2];

void imprime(int vect[]){

    for(int i = 0; i <4; i++){
        printf("%d ",vect[i]);
    }

}

void ctm(){

    int cont=0,numa = 0;

    for(int i = 0; i < 4; i++){


                            for(int l=0; l<4;l++){

                                   // cout<<prov1[0][i]<<endl;
                                if(prov1[0][i] == prov2[0][l]){
                                    cont++;
                                    numa = prov1[0][i];

                                }
                            }




    }
    //imprime(vect2);
    aux[0] = cont;
   aux[1] = numa;


}

int main()
{
   int tb1[4][4],tb2[4][4];
   int op1,op2, cont = 1,cs;

    cin>>cs;
    while(cont <= cs){
        cin>>op1;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                cin>>tb1[i][j];
                if(op1 == (i + 1)) prov1[0][j] = tb1[i][j];

            }
        }
        cin>>op2;
        for(int i=0; i<4 ; i++){
            for(int j=0; j<4; j++){
                cin>>tb2[i][j];
                if(op2 == (i + 1)) prov2[0][j] = tb2[i][j];
            }
        }


        ctm();
       // cout<<aux[1];

         if(aux[0] == 0) printf("Case #%d: Volunteer cheated!\n",cont);
         else if(aux[0] == 1) printf("Case #%d: %d\n",cont,aux[1]);
                else if(aux[0] > 1) printf("Case #%d: Bad magician!\n",cont);

        cont++;
    }


    return 0;
}
