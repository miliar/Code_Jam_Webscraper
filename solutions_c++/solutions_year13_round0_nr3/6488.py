#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;


int main (){
int casos, i, a, b, raiz2,raiz3, num, aux, k, pow, m, num1, num2, contador, numi, numi2;
float raiz,raizi;
fstream archivoin("C-small-attempt0.in");
fstream archivoout("output.out");


if((archivoin)&&(archivoout)){
    archivoin >> casos;
    for(i=0;i<casos;i++){
        contador=0;
        archivoin >> a;
        archivoin >> b;
        while(a<b+1){
            aux=a;
            k=0;
                while(true){
                    aux=aux/10;
                    k++;
                    if(aux==0) break;
                }
                numi=0;
                for(int j=0;j<k-1;j++){
                    pow=1;
                    m=0;
                    while(m<j){
                        pow=pow*10;
                        m++;
                    }
                    num1=(a/pow)%10;
                    

                    pow=1;
                    m=j;
                    while(m<k-1){
                        pow=pow*10;
                        m++;
                    }
                    num2=(a/pow)%10;
                    if(num1==num2){
                        numi++;
                    }
                }
                if(numi==k-1){
                









            raiz=sqrt(a);
            raizi=raiz*10;
            raiz2=(int)raizi;
            raiz3=(int)raiz;
            raiz3=raiz3*10;
            
            if(raiz2==raiz3){
                num=raiz2/10;
                aux=num;
                k=0;
                while(true){
                    aux=aux/10;
                    k++;
                    if(aux==0) break;
                }
                numi2=0;
                for(int j=0;j<k-1;j++){
                    pow=1;
                    m=0;
                    while(m<j){
                        pow=pow*10;
                        m++;
                    }
                    num1=(num/pow)%10;


                    pow=1;
                    m=j;
                    while(m<k-1){
                        pow=pow*10;
                        m++;
                    }
                    num2=(num/pow)%10;

                    if(num1==num2){
                        numi2++;
                    }
                }
                if(numi2==k-1){
                    contador++;
                }




            }        
            }
            a++;
        }
        archivoout << "Case #"<< i+1 << ": ";
        archivoout << contador;
        if(i!=casos-1) archivoout << endl;
    }
    archivoin.close();
    archivoout.close();
} else cout << "No se pudo abrir el archivo" << endl;

system("PAUSE");
return 0;
}
