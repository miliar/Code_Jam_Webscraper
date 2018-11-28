#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int T;
int N;
int main(){
    cin >> T;//numero de casos de teste
    for (int caso = 1; caso <= T; caso++){
        cin >> N; //numero inicial
        cout << "Case #" << caso << ": ";

        if (N == 0)
            cout << "INSOMNIA";
        else{

            vector<int> digits;
            digits.assign(10, 0);
            int cont = 0;
            int j = 1;

            while (cont < 10){
                stringstream convert;
                convert << (N*j++);
                string number = convert.str();
                for(int i = 0; i<number.size(); i++){
                    if (!digits[number[i]-'0'] ){
                        digits[number[i]-'0'] = 1;
                        cont++;
                    }
                }
            }
            cout << N*(j-1);
        }
        cout << "\n";
    }

    return 0;
}
