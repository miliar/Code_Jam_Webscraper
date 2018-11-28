#include <iostream>
#include <vector>

using namespace std;

int main(){
    int cantidad_de_tests, N;

    cin >> cantidad_de_tests;

    for(int i = 0; i < cantidad_de_tests; i++){
        bool respuestas[10] = {false, false, false, false, false, false, false, false, false, false};
        bool seguir = true;

        cin >> N;

        if(N != 0){
            int acumulado = 0;

            for(int k = 0; seguir; k++){
                int aux;
                acumulado += N;
                aux = acumulado;

                for(int j = 0; aux > 0; j++){
                    respuestas[aux % 10] = true;
                    aux = aux / 10;
                }

                seguir = false;
                for(int j = 0; j < 10; j++){
                    if(respuestas[j] == false) seguir = true;
                }
            }

            cout << "Case #" << (i+1) << ": " << acumulado << endl;
        }else{
            cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
        }

    }

    return 0;
}
