#include<iostream>
#include <string>

using namespace std;

int tab[4][4];
int tab2[4][4];
int fir, sec;

void solve(int cas){
    int ile=0;
    int wyn=0;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(tab[fir][i]==tab2[sec][j]){
                ile++;
                wyn=tab[fir][i];
            }
        }
    }
    /*cout << "***\n";
    cout << ile << " " << wyn << " " << fir << " " << sec << "\n";
    cout << "***\n";*/
    if(ile==0){
        cout << "Case #" << cas << ": " "Volunteer cheated!\n";
        return;
    }
    if(ile==1){
        cout << "Case #" << cas << ": " << wyn << "\n";
        return;
    }
    if(ile>1){
        cout << "Case #" << cas << ": " << "Bad magician!\n";
        return;
    }
}

int main(){
    int t;
    cin >> t;

    for(int i = 1; i<= t; i++){
        cin >> fir;
        for(int x = 0; x < 4; x++){
            for(int y = 0; y < 4; y++){
                cin >> tab[x][y];
            }
        }
        cin >> sec;
        for(int x = 0; x < 4; x++){
            for(int y = 0; y < 4; y++){
                cin >> tab2[x][y];
            }
        }
        fir--;
        sec--;
        solve(i);
    }
}
