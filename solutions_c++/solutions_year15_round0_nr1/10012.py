#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;



int main (void ) {

    FILE *in = fopen("A-small-attempt2.in", "r+");
    FILE *out = fopen("A-small-attempt2.out","w+");
    char linha[100],N[9];
    int  testes, timidez,casos,resultado,nvMaximo;


    fscanf(in,"%[^\n]",linha);
    fgetc(in);
    testes = atoi(linha);



    for (int z=1;z<=testes;z++){


        fscanf(in,"%[^\n]",linha);
        fgetc(in);
        timidez = atoi(linha);

        if(timidez == 0){
            fprintf(out,"Case #%d: 0",z);
        }else{

            resultado = 0;
            nvMaximo  = 0;


            for(int i = 0;i<=timidez;i++){
                N[i]=linha[i+2];

                if(N[i]!='0' && i<=nvMaximo){
                    nvMaximo += N[i]-'0';

                }
                if(N[i]!='0' && i>nvMaximo){
                    resultado = resultado + i-nvMaximo;
                    nvMaximo =  N[i]-'0'+i;

                }



              //  cout<< "caso: "<<z<<"nvMax: "<<nvMaximo << "  - resultado: "<<resultado<<"  N[i]: "<<N[i]<<"  i: "<<i<<endl;

            }

            if(resultado == 0){
                fprintf(out,"Case #%d: 0",z);
            }else{
                fprintf(out,"Case #%d: %d",z,resultado);
            }
        }
        if(z<testes){
            fprintf(out,"\n");
        }
    }





    fclose(in);
    fclose(out);
}

