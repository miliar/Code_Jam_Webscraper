#include<iostream>

using namespace std;

int main(){

    int T, A, B, K, counter, testes = 1, x;

    cin >> T;

    for(int i = 0; i < T; i++){
        counter = 0;

        cin >> A >> B >> K;

        for(int j = 0; j < A; j++){
            for(int k = 0; k < B; k++){
                x = j&k;
                if(x < K){
                    counter++;
                }
            }
        }

        cout << "Case #" << testes << ": " << counter << endl;
        testes++;
    }

    return 0;
}
