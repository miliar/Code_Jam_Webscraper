#include <iostream>
#include <algorithm>
#include <cmath>

#include <vector>
#include <set>
#include <utility>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("entrada.in");
    ofstream cout("salida.txt");

    int T, a, b, carta=0;
    int A[5][5], B[5][5];
    bool bad = false, Carta=false;
    cin >> T;
    for(int q=1; q<=T; q++){
        carta =0;
        bad=false;
        Carta=false;
        cin >> a;
        for(int i = 1; i<5; i++){
            for(int j=0; j<4; j++){
                cin >> A[i][j];
            }
        }
        cin >> b;
        for(int i = 1; i<5; i++){
            for(int j=0; j<4; j++){
                cin >> B[i][j];
                if(i==b){
                    if(B[i][j]==A[a][0] || B[i][j]==A[a][1] || B[i][j]==A[a][2] || B[i][j]==A[a][3]){
                        if(Carta == false){
                            carta=B[i][j];
                            Carta = true;
                        } else {
                            bad = true;
                        }

                    }
                }
            }
        }
        cout << "Case #" << q << ": ";
        if(carta==0) cout << "Volunteer Cheated!";
        else if(bad == true) cout  << "Bad magician!";
        else cout << carta;
        cout << endl;
    }

    return 0;
}
