#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
    ifstream file("donnees.txt");
    int N;
    ostringstream os;
    file >> N;
    os << file.rdbuf();
    string str;
    str = os.str();
//    cout << str;
    cout << N;
    cout << endl << endl;
    int cursor = str.find('\n', 0);
//    cout << cursor;
    int **tab = new int*[4];
    for(int i=0; i<4; i++)
        tab[i] = new int[4];

    bool notComplete = false;
    bool solution;

    for(int i=0; i<=N+1; i++){
        solution = false;
        notComplete = false;
        for(int j=0; j<16; cursor++){// remplir le tableau des donnŽes
            if(str.at(cursor) == 'T'){
                tab[j/4][j%4] = 1;
                j++;
            }
            else if(str.at(cursor) == 'X'){
                tab[j/4][j%4] = 3;
                j++;
            }
            else if(str.at(cursor) == 'O'){
                tab[j/4][j%4] = 15;
                j++;
            }
            else if(str.at(cursor) == '.'){
                tab[j/4][j%4] = -50;
                j++;
            }
        }


        int totL = 0; // total ligne
        int totC = 0; // total colonne
        for(int j=0; j<4; j++){
            totL = 0;
            totC = 0;
            for(int k=0; k<4; k++){
                totL += tab[j][k];
                totC += tab[k][j];
            }
            if(totL == 12 || totC == 12 || totL == 10 || totC == 10){
                cout << "Case #" << i+1 << ": X won" << endl;
                solution = true;
                break;
            }
            else if(totL == 60 || totC == 60 || totL == 46 || totC == 46){
                cout << "Case #" << i+1 << ": O won" << endl;
                solution = true;
                break;
            }
            if(totL < 0 || totC < 0)
                notComplete = true;
        }

        int totD1 = 0; // premire digonale
        int totD2 = 0; // deuxime diagonale
        for(int j=0; j<4; j++){
            totD1 += tab[j][j];
            totD2 += tab[j][3-j];
        }

        if(totD1 == 12 || totD2 == 12 || totD1 == 10 || totD2 == 10){
            cout << "Case #" << i+1 << ": X won" << endl;
            solution = true;
            continue;
        }
        else if(totD1 == 60 || totD2 == 60 || totD1 == 46 || totD2 == 46){
            cout << "Case #" << i+1 << ": O won" << endl;
            solution = true;
            continue;
        }

        if(totD1 < 0 || totD2 < 0)
            notComplete = true;

        if(notComplete && !solution)
            cout << "Case #" << i+1 << ": Game has not completed" << endl;

        if(!notComplete && !solution)
            cout << "Case #" << i+1 << ": Draw" << endl;
    }
    return 0;
}
