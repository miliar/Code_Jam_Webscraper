#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream fin("A-large.in");
    ofstream fout("outputLarge.txt");
    int T;
    char c;
    int charHash[10];
    int numbers[10];
    bool isEnter;
    int occ;
    fin >> T;
    fin.get();
    for(int i = 0; i < T; i++) {
        //cout << "\nin Loop : iteration = " << i+1 ;
        for(int j = 0; j < 10; j++){
            charHash[j] = 0;
            numbers[j] = 0;
        }
        isEnter = false;
        do{
            c = fin.get();
            switch(c){
            case 'Z': charHash[0]++;
                break;
            case 'O': charHash[1]++;
                break;
            case 'W': charHash[2]++;
                break;
            case 'R': charHash[3]++;
                break;
            case 'U': charHash[4]++;
                break;
            case 'F': charHash[5]++;
                break;
            case 'X': charHash[6]++;
                break;
            case 'V': charHash[7]++;
                break;
            case 'G': charHash[8]++;
                break;
            case 'N': charHash[9]++;
                break;
            case 'E':
                break;
            case 'T':
                break;
            case 'H':
                break;
            case 'S':
                break;
            case 'I':
                break;
                default : isEnter = true;
                    break;
            }
        }while(!isEnter);
        if(charHash[0]){
            occ = charHash[0];
            numbers[0] = occ;
            charHash[1] -= occ;
            charHash[3] -= occ;
        }
        if(charHash[2]){
            occ = charHash[2];
            numbers[2] = occ;
            charHash[1] -= occ;
        }
        if(charHash[4]){
            occ = charHash[4];
            numbers[4] = occ;
            charHash[1] -= occ;
            charHash[3] -= occ;
            charHash[5] -= occ;
        }
        if(charHash[6]){
            occ = charHash[6];
            numbers[6] = occ;
        }
        if(charHash[8]){
            occ = charHash[8];
            numbers[8] = occ;
        }
        if(charHash[1]){
            occ = charHash[1];
            numbers[1] = occ;
            charHash[9] -= occ;
        }
        if(charHash[3]){
            occ = charHash[3];
            numbers[3] = occ;
        }
        if(charHash[5]){
            occ = charHash[5];
            numbers[5] = occ;
            charHash[7] -= occ;
        }
        if(charHash[7]){
            occ = charHash[7];
            numbers[7] = occ;
            charHash[9] -= occ;
        }
        if(charHash[9]){
            occ = charHash[9]/2;
            numbers[9] = occ;
        }
        fout << "Case #" << i+1 << ": ";
        for(int j = 0; j < 10; j++){
            for(int k = 0; k < numbers[j]; k++){
                fout << j;
            }
        }
        fout << "\n";
    }
    return 0;
}
