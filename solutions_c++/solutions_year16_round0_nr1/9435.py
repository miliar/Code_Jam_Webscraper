#include <algorithm>    // std::reverse
#include <vector>       // std::vector
#include<iostream>
#include<fstream>
#include <cmath>
#include <string>

using namespace std;

bool tutti_elem_true(bool arr[], long long int base=10){ //ritorna true sse tutti gli elementi dell'array sono a true
    bool ris = true;
    for (long long int i = 0; i < base && ris; ++i){
        if (!arr[i]){
            ris = false;
        }
    }
    return ris;
}

void inizializzo_arr(bool arr[], long long int base=10){
    for (long long int i = 0 ; i < base; i++)
        arr[i] = false;
}

void aggiungo_elemento_arr(bool arr[], long long int elem){
    string s = to_string(elem);

    for (long long int i=0; i<s.size();++i){
        long long int k = s[i] - '0';
        arr[k] = true;
    }
}


int main()
{
    ifstream INP("in");
    ofstream OUT("out");
    if(!INP || !OUT){
      cout<<"ERRORE nei FILE"<<endl;

    }
    else {
        long long int T;
        INP >> T;
        cout << T << endl;

            bool arr[10]; //la posizione i-esima è true sse ho già visto la cifra di valore i

            long long int elemento = 0;

            string sol = "INSOMNIA";

            long long int i = 0;
            for (long long int i = 0; i<T ; ++i) {
                INP>> elemento;
                cout << elemento << endl; //////////////////////////////////////////////////////////////////

                if (elemento != 0){
                   long long int N = 1;
                   inizializzo_arr(arr);
                   aggiungo_elemento_arr(arr,elemento);
                   while (!tutti_elem_true(arr)) {
                       ++N;
                       aggiungo_elemento_arr(arr,elemento*N);
                   }

                   sol = to_string(elemento*N);
                }

                if (i + 1 < T)
                    OUT <<"Case #"<<i+1<<": "<<sol<<endl;
                else
                    OUT <<"Case #"<<i+1<<": "<<sol;
            }

       INP.close();
       OUT.close();
    }
}
