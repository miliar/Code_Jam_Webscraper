#include <iostream>

using namespace std;

int main() {

    int nbTest;

    cin >> nbTest;

    char s[101];

    for(int i = 0; i < nbTest; ++ i){

        cin >> s;
        int ctr = 0;
        int k = 0;
        char plus = (s[k] == '-') ? 0 : 1;



        while (true){

            if(s[k] == '-' && plus != 0){
                plus = 0;
                ctr++;
            }
            else if(s[k] == '+' && plus == 0){
                plus = 1;
                ctr++;
            }
            else if(s[k] == '\0'){
                if(plus == 0) ctr++;
                break;
            }

            k++;
        }

        cout << "Case #" << 1+i << ": " << ctr << endl;

    }

    return 0;
}