#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
    ifstream input("b.in");
    ofstream output;
    output.open ("b.out");
    int T, Sl, l, steps;
    string S;
    bool data[100];


    input >> T;
    for(int i = 0; i < T; i++) {
        input >> S;
        output << "Case #" << (i + 1) << ": ";
        Sl = S.length();
        steps = 0;
        for(int j = 0; j < Sl; j++) data[j] = S[j] == '+';
        while(true) {
            l = -1;
            for(int j = Sl - 1; j >= 0; j--) {
                if(!data[j]) {
                    l = j;
                    break;
                }
            }
            if(l == -1) {
                output << steps << endl;
                break;
            }
            if(data[0]) {
                for(int j = 1; j < Sl; j++) {
                    if(!data[j]) {
                        for(int k = 0; k < j; k++) {
                            data[k] = false;
                        }
                        steps++;
                        break;
                    }
                }
            }
            bool reverse[l + 1];
            for(int j = 0; j <= l; j++) {
                reverse[l - j] = !data[j];
            }
            for(int j = 0; j <= l; j++) data[j] = reverse[j];
            steps++;
        }
    }
    output.close();
    return 0;
}
