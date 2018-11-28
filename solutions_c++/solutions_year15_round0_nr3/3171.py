#include <iostream>
#include <fstream>

using namespace std;

char data[10010];
int signal[10010];

void comb(int pointer, char forc, char latc){
    if (forc == '1') {
        switch(latc){
            case '1': data[pointer]='1'; signal[pointer] = signal[pointer - 1];return;
            case 'i': data[pointer]='i'; signal[pointer] = signal[pointer - 1];return;
            case 'j': data[pointer]='j'; signal[pointer] = signal[pointer - 1];return;
            case 'k': data[pointer]='k'; signal[pointer] = signal[pointer - 1];return;
        };
    }
    else if(forc == 'i') {
        switch(latc){
            case '1': data[pointer]='i'; signal[pointer] = signal[pointer - 1];return;
            case 'i': data[pointer]='1'; signal[pointer] = -signal[pointer - 1]; return;
            case 'j': data[pointer]='k'; signal[pointer] = signal[pointer - 1];return;
            case 'k': data[pointer]='j'; signal[pointer] = -signal[pointer - 1]; return;
        };
    }
    else if (forc == 'j') {
        switch(latc){
            case '1': data[pointer]='j'; signal[pointer] = signal[pointer - 1];return;
            case 'i': data[pointer]='k'; signal[pointer] = -signal[pointer - 1]; return;
            case 'j': data[pointer]='1'; signal[pointer] = -signal[pointer - 1]; return;
            case 'k': data[pointer]='i'; signal[pointer] = signal[pointer - 1];return;
        };
    }
    else if(forc == 'k') {
        switch(latc){
            case '1': data[pointer]='k'; signal[pointer] = signal[pointer - 1];return;
            case 'i': data[pointer]='j'; signal[pointer] = signal[pointer - 1];return;
            case 'j': data[pointer]='i'; signal[pointer] = -signal[pointer - 1]; return;
            case 'k': data[pointer]='1'; signal[pointer] = -signal[pointer - 1]; return;
        };
    }

}

int main()
{
    ifstream fin("C-small-attempt2.in");
    ofstream fout("ouput-small.txt");

    int T, L, X;
    fin >> T;
    int pointer = 0, flag = 0, suc = 0;
    char forc, latc;


    for (int i = 0; i < T; ++i){
        pointer = 0; flag = 0; suc = 0;
        fin >> L >> X;
        for (int j = 0; j < L; ++j){
            fin >> data[j];
            signal[j] = 1;
        }
        for (int j = 1; j < X; ++j){
            for (int k = 0; k < L; ++k){
                data[j*L + k] = data[k];
                signal[j*L + k] = 1;
            }
        }
        data[L*X] = '\0';

        for (pointer = 0; pointer < L*X; ++pointer){
            if (pointer == 0) {
                if (data[pointer] == 'i') {++suc;break;}
                else continue;
            }
            comb(pointer, data[pointer-1], data[pointer]);
//            for (int m = 0; m < L*X; ++m){
//                fout << data[m];
//            }
//            fout <<endl;
//            for (int m = 0; m < L*X; ++m){
//                fout << signal[m];
//            }
//            fout <<endl;
            if (data[pointer] == 'i' && signal[pointer] == 1) {
                    ++suc;
                    break;
            }
        }

        flag = pointer;
//        fout <<"FLAG: "<<flag<<endl;
        for (++pointer; pointer < L*X; ++pointer){
            if (pointer == flag + 1) {
                if (data[pointer] == 'j') {++suc;break;}
                else continue;
            }
            comb(pointer, data[pointer-1], data[pointer]);
//            for (int m = 0; m < L*X; ++m){
//                fout << data[m];
//            }
//            fout <<endl;
//            for (int m = 0; m < L*X; ++m){
//                fout << signal[m];
//            }
//            fout <<endl;

            if (data[pointer] == 'j' && signal[pointer] == 1){
                    ++suc;
                    break;

            }
        }

        flag = pointer;
//        fout <<"FLAG: "<<flag<<endl;
        for (++pointer; pointer < L*X; ++pointer){
            if (pointer == flag + 1) {
                if (data[pointer] == 'k') {++suc;}
                continue;
            }
            comb(pointer, data[pointer-1], data[pointer]);

//            for (int m = 0; m < L*X; ++m){
//                fout << data[m];
//            }
//            fout <<endl;
//            for (int m = 0; m < L*X; ++m){
//                fout << signal[m];
//            }
//            fout <<endl;
            if (data[pointer] == 'k' && signal[pointer] == 1){
                    ++suc;
            }
        }

        pointer = L*X -1;
//        cout << pointer<<endl;
        if (suc >= 3 && data[pointer] == 'k' && signal[pointer] == 1){
            fout <<"Case #" << i+1 <<": Yes"<<endl;
        }
        else{
            fout <<"Case #" << i+1 <<": No"<<endl;
        }
//        fout<<endl;
    }

    fin.close();
    fout.close();
    return 0;
}
