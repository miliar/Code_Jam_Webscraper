#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ifstream cin ("A-small-attempt0.in");
    ofstream cout("A-small-attempt0.out");

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        int r[17] = {};
        for (int j = 0; j < 2; j++){
            int a;
            cin >> a;
            for (int l = 1; l <= 4; l++){
                for (int i = 1; i <= 4; i++){
                    int x;
                    cin >> x;
                    if (l == a){
                        r[x]++;
                    }
                }
            }
        }

        int y, n2s = 0;
        for (int k = 1; k < 17; k++){
            if (r[k] == 2){
                n2s++;
                y = k;
            }
        }

        cout << "Case #" << t << ": ";
        switch(n2s){
            case 0: cout << "Volunteer cheated!"; break;
            case 1: cout << y; break;
            default: cout << "Bad magician!"; break;
        }

        cout << endl;

    }

    return 0;
}
