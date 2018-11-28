#include <iostream>

using namespace std;
char plansza [4][4];

int row [4];
int col [4];
int diag;
int antidiag;

void alg(){
    char c;
    bool jest_puste = false;
    int pozycjaT [2];
    bool jestT = false;
    bool won = false;
    bool d;
    bool ad;
    diag = 0;
    antidiag = 0;
    for(int i = 0; i < 4; ++i){
        col[i] = 0;
        row[i] = 0;
    }
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j){
            d = false;
            ad = false;
            cin >> c;
            if(i == j){
                d = true;
            }
            else if(i + j == 3){
                ad = true;
            }

            if(c == 'O') {
                row[j]++;
                col[i]++;
                if(ad)
                    antidiag++;
                else if(d)
                    diag++;
            }
            else if(c == 'X'){
                row[j]--;
                col[i]--;
                if(ad)
                    antidiag--;
                else if(d)
                    diag--;
            }
            else if(c == 'T'){
                jestT = true;
                pozycjaT[0] = i;
                pozycjaT[1] = j;
            }
            else
                jest_puste = true;
        }
        if(jestT){
            if(row[pozycjaT[1]] < 0)
                row[pozycjaT[1]]--;
            else
                row[pozycjaT[1]]++;
            if(col[pozycjaT[0]] < 0)
                col[pozycjaT[0]]--;
            else
                col[pozycjaT[0]]++;
            if(pozycjaT[0] == pozycjaT[1]){
                if(diag > 0)
                    diag++;
                else
                    diag--;
            }
            else if(pozycjaT[0] + pozycjaT[1] == 3){
                if(antidiag > 0)
                    antidiag++;
                else
                    antidiag--;
            }
        }
        if(diag == 4 || antidiag == 4){
            cout << "O won" << endl;
            won = true;
        }
        else if(diag == -4 || antidiag == -4){
            cout << "X won" << endl;
            won = true;
        }
        else {
            int i = 0;
            while(!won && i < 4){
                if (row[i] == -4){
                    won = true;
                    cout << "X won" << endl;
                }
                else if(row[i] == 4){
                    won = true;
                    cout << "O won" << endl;
                }
                ++i;
            }
            if(!won){
                i = 0;
                while(!won && i < 4){
                    if (col[i] == -4){
                        won = true;
                        cout << "X won" << endl;
                    }
                    else if(col[i] == 4){
                        won = true;
                        cout << "O won" << endl;
                    }
                    ++i;
                }
            }
            if(!won && jest_puste)
                cout << "Game has not completed" << endl;
            else if(!won && !jest_puste)
                cout << "Draw" << endl;
        }
        cin.get();
}

int main() {
    int t;
    cin >> t;
    for (int case_no = 1; case_no <= t; ++case_no) {
        cout << "Case #" << case_no << ": ";
        alg();
    }
}
