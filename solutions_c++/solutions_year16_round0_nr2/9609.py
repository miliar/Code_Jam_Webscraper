#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("in.txt");
    streambuf *cinbuf = cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect cin to in.txt!
    ofstream out("out.txt");
    streambuf *coutbuf = cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
    int caseNumber;
    int charCounter, turns;
    bool allCakes[101];
    char temp;
    bool toBreak, forMirroring;
    int k, i, j;
    cin >> caseNumber;
    for (k = 0; k < caseNumber; k++){
        charCounter = 0;
        while(1){
            cin >> temp;
            if (temp == '+'){
                allCakes[charCounter++] = true;
            }
            else if (temp == '-'){
                allCakes[charCounter++] = false;
            }
            if (cin.peek() == '\n'){
                break;
            }
        }
        turns = 0;
        while(1){
            if (allCakes[0]){
                toBreak = false;
                for (i = 1; i < charCounter; i++){
                    if (!allCakes[i]){
                        for (j = 0; j < i; j++){
                            allCakes[j] = !allCakes[j];
                        }
                        toBreak = true;
                        break;
                    }
                }
                if (toBreak){
                    turns++;
                }
                else{
                    break;
                }
            }
            else{
                toBreak = false;
                for (i = charCounter - 1; i > 0; i--){
                    toBreak = true;
                    if (allCakes[i]){
                        charCounter--;
                    }
                    else{
                        for (j = 0; j < ((i + 1) / 2); j++){
                            forMirroring = allCakes[j];
                            allCakes[j] = !allCakes[i - j];
                            allCakes[i - j] = !forMirroring;
                        }
                        if (((i + 1) % 2)){
                            allCakes[j] = !allCakes[j];
                        }
                        turns++;
                        break;
                    }
                }
                if (!toBreak){
                    allCakes[0] = !allCakes[0];
                    turns++;
                    break;
                }
            }
        }
        cout << "Case #" << k + 1 << ": " << turns << endl;
    }
    return 0;
}
