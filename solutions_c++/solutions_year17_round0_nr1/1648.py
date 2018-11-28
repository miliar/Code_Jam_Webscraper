#include <iostream>
#include <string>
using namespace std;

int main(){
    int nCases;
    cin >> nCases;

    string cakes;
    int lenCakes, nK;

    for(int i = 0; i < nCases; i ++){
        cin >> cakes >> nK;
        lenCakes = cakes.size();
        int cntK = 0;
        for(int j = 0; j <= lenCakes - nK; j ++){
            if(cakes[j] == '+')
                continue;
            cntK ++;
            for(int k = j; k < j + nK; k ++){
                if(cakes[k] == '+')
                    cakes[k] = '-';
                else
                    cakes[k] = '+';
            }
        }

        bool flag = false;
        for(int j = 0; j < lenCakes; j ++){
            if(cakes[j] == '-'){
                flag = true;
                break;
            }
        }

        cout << "Case #" << i + 1 << ": ";
        if(flag)
            cout << "IMPOSSIBLE\n";
        else
            cout << cntK << endl;
    }
    return 0;
}

