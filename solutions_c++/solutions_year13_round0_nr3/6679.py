#include <math.h>
#include <iostream>
using namespace std;

int main (){

    int a,b, qtd, aux ,reverso,count, flag;
    int i;

    cin >> qtd;

    for(i=0 ; i<qtd ; i++){

        cin >> a >> b;
        count=0;

        while (a<=b){

            double result = sqrt(a);

            if((result * result) == a){

                aux = a;
                reverso = 0;

                while (aux != 0) {
                    reverso = reverso * 10 + aux % 10;
                    aux = aux / 10;
                }

                if (reverso == a){

                    aux = result;
                    reverso = 0;

                    while (aux != 0) {
                        reverso = reverso * 10 + aux % 10;
                        aux = aux / 10;
                    }

                    if (reverso == result )
                        count++;
                }
            }
            a++;

        }

        cout << "Case #" << i << ": " << count << "\n";

    }


    return 0;
}
