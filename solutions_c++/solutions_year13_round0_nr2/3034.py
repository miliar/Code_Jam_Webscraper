#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <math.h>
#include <string.h>
#include <stack>

using namespace std;

string intToStr(int n) {
    if(n == 0) return "0";
    string ans = "";
    while(n > 0) {
        ans = (char) ((n % 10) + '0') + ans;
        n /= 10;
    }
    return ans;
}

int strToInt(string n) {
    int ans = 0;
    for(int i = 0; i < n.size(); i++){
        ans += (n[n.size() -i - 1] - '0') * pow(10, i);
    }
    return ans;
}

int n, row, col;
int laws[101][101];

int main(void){
    int test = 1;
    freopen("in.in.c", "r", stdin);
    freopen("out.out", "w", stdout);
    cin >> n;
    for(int o = 0; o < n; o++){
        cin >> row >> col;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                cin >> laws[i][j];
            }
        }
        bool can = 1;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                int now = laws[i][j];
                int cima = 0, baixo = 0, dir = 0, esq = 0;
                for(int k = 0; k < j; k++){
                    if(laws[i][k] > now) {
                        esq++;
                        break;
                    }
                }
                for(int k = j+1; k < col; k++){
                    if(laws[i][k] > now){
                        dir++;
                        break;
                    }
                }
                for(int k = 0; k < i; k++){
                    if(laws[k][j] > now){
                        cima++;
                        break;
                    }
                }
                for(int k = i+1; k < row; k++){
                    if(laws[k][j] > now){
                        baixo++;
                        break;
                    }
                }
                if((cima || baixo) && (dir || esq)){
                    can = false;
                }
                //cout << "Cima: " << cima << " baixo: " << baixo << ", esq: " << esq << " dir: " << dir << endl;
            }
        }
        cout << "Case #" << test++ << ": ";
        if(can){
            cout << "YES\n";
        }else{
            cout << "NO\n";
        }
    }
    return 0;
}
