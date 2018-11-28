#include <iostream>
#include <stdio.h>

using namespace std;

int matriz1[4][4];
int matriz2[4][4];

int main(int argc, char *argv[]) {
    int T;
    int optionone;
    int optiontwo;
    int answer;

    cin >> T;

    for(int w = 0; w < T; w++) {
            cin >> optionone;
            optionone--;

            for(int i = 0; i<4; i++) {
                for(int j=0; j<4; j++) {
                    cin>>matriz1[i][j];
                }
            }

            cin>>optiontwo;
            optiontwo--;

            for(int i = 0; i < 4; i++) {
                for(int j = 0; j < 4; j++) {
                    cin >> matriz2[i][j];
                }
            }

            int cont = 0;
            for(int i = 0; i < 4; i++) {
                for(int j = 0; j < 4; j++) {
                    if(matriz1[optionone][i] == matriz2[optiontwo][j]){
                        cont++;
                        answer = matriz1[optionone][i];
                        if(cont > 1) {
                            answer=999;
                        }
                    }
                    else if(cont == 0) {
                        answer = 888;
                    }
                }
            }

            cout<<"Case #" << w+1 << ": ";
            if(answer == 999)
                cout<<"Bad magician!"<<endl;
            else if(answer == 888)
                cout<<"Volunteer cheated!"<<endl;
            else
                cout<<answer<<endl;
    }
}
