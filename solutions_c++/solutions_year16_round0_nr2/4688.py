#include <iostream>

using namespace std;

int main(){
    int cantidad_de_tests, result = 0;
    char ultimoVisto;
    string pancakes = "";

    cin >> cantidad_de_tests;

    for(int i = 0; i < cantidad_de_tests; i++){
        cin >> pancakes;

        ultimoVisto = pancakes[0];
        result++;

        for(unsigned int j = 1; j < pancakes.size(); j++){
            if(ultimoVisto != pancakes[j]){
                ultimoVisto = pancakes[j];
                result++;
            }
        }

        if(pancakes[pancakes.size() - 1] == '+') result--;


        cout << "Case #" << (i+1) << ": " << result << endl;
        result = 0;
    }

    return 0;
}
