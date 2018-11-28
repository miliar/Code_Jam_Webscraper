#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    int nun_testes;
    cin>> nun_testes;
    int amigos_necessarios=0;
    int Smax;


    for(int a=1;a<=nun_testes;a++){
        amigos_necessarios=0;
        cout << endl;
        cin >> Smax;
        char vetor[Smax+1];
        cin.ignore();

        int nivelT[Smax+1];

        cin.getline(vetor,Smax+2);


        for(int i=0;i<Smax+1;i++){
            nivelT[i] = vetor[i] - 48;
        }
        int r=0;
        for(int i=1;i<Smax+1;i++){
            int cont_parcial=0;
            for(int j=0;j<i;j++){
                cont_parcial+=nivelT[j];
            }
            cont_parcial+=r;
            while(cont_parcial<i){
                r++;
                cont_parcial++;
                amigos_necessarios++;
            }
        }
        cout << "Case #" << a << ": " <<  amigos_necessarios;
    }
    return 0;
}
