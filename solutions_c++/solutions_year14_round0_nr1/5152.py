#include <stdio.h>
#include <fstream>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");



int solve_case(int t){
    int a1, a2, w, c = 0;
    int s1[4][4], s2[4][4], r1[4], r2[4];
    cin >> a1;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            cin >> s1[i][j];
            if(i == a1-1)
                r1[j] = s1[i][j];
        }
    }
    cin >> a2;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            cin >> s2[i][j];
            if(i == a2-1)
                r2[j] = s2[i][j];
        }
    }
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(r1[i]==r2[j]){
                c++;
                w = r1[i];
            }
        }
    }
    if(c == 1)
        return w;
    if(c == 0)
        return 0;
    if(c > 1)
        return -1;
}

int main(){
    int t;
    cin >> t;
    int c[t];
    for(int i = 1; i < t+1; i++){
        c[i-1] = solve_case(t);
    }
    for(int i = 0; i < t; i++){
        cout << "Case #";
        cout << i+1;
        cout << ":";
        switch (c[i]){
            case 0:
                cout << " Volunteer cheated!\n";
                break;
            case -1:
                cout << " Bad magician!\n";
                break;
            default:
                cout << " ";
                cout << c[i];
                cout << "\n";
        }
    }
    return 0;
}
