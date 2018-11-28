#include <iostream>

using namespace std;

int readCards(int *ans1, int *ans2){
    int equals = 0, out, resp, lixo;

        cin >> resp;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                if(j + 1 == resp){
                    cin >> ans1[k];
                }else{
                    cin >> lixo;
                }
            }
        }
        cin >> resp;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                if(j + 1 == resp){
                    cin >> ans2[k];
                    for(int l = 0; l < 4; l++){
                        if(ans1[l] == ans2[k]){
                            equals++;
                            out = ans2[k];
                        }
                    }
                }else{
                    cin >> lixo;
                }
            }
        }
    return (equals > 1)?(0):((equals == 0)?(-1):(out));
}

int main(){

    int testes, resposta, cont = 1;
    int ans1[4], ans2[4];

    cin >> testes;
    for(int i = 0; i < testes; i++){
        resposta = readCards(ans1, ans2);
        if(resposta == -1){
            cout << "Case #" << cont << ": " << "Volunteer cheated!" << endl;
        }else if(resposta == 0){
            cout << "Case #" << cont << ": " << "Bad magician!" << endl;
        }else{
            cout << "Case #" << cont << ": " << resposta << endl;
        }
        cont++;
    }

    return 0;
}
