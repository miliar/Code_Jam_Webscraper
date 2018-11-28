#include <iostream>
#include <sstream>

using namespace std;

int main(){
int t,row1,row2;
int cartas1[17];
int cartas2[17];
int i,k,p;
int qwe;
int cantidad;
string ans;
bool igual[4];

    cin >> t;
    for (i = 1; i <= t; i++){

        cin >> row1;
        for (k = 1; k <= 16; k++){
            cin >> cartas1[k];
        }

        cin >> row2;
        for (k = 1; k <= 16; k++){
            cin >> cartas2[k];
        }
    for (p = 1; p <= 4; p++){
        for (k = 1; k <= 4; k++){
            if (cartas1[k+(row1-1)*4] != cartas2[p+(row2-1)*4])igual[p] = false;
            else{
                igual[p] = true;
                break;
            }
        }
    }

        cantidad = 0;
        for (k = 1; k <= 4; k++){
            if (igual[k] == true){
                cantidad ++;
                qwe = cartas2[k+(row2-1)*4];
            }
        }

        if (cantidad == 1){
             stringstream aux;
             aux << qwe;
             ans = aux.str();
        }

        if (cantidad > 1) ans = "Bad magician!";

        if ((igual[1] == false) && (igual[2] == false) &&
        (igual[3] == false) && (igual[4] == false)){
            ans = "Volunteer cheated!";
        }


        cout << "Case #" << i << ": " << ans << endl;
    }


    return 0;
}
