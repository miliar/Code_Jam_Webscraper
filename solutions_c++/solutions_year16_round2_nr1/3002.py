#include <bits/stdc++.h>
#define optimizar_ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

int num[10];
int let[26];

int main(){
    optimizar_

    ifstream cin2;
    ofstream cout2;
    cin2.open("a.in", ios::in);
    cout2.open("result.txt", ios::out);

    int T;
    char s[2002];
    cin2 >> T;

    for(int i = 1; i <= T; i++){
        cout2 << "Case #" << i << ": ";
        cin2 >> s;
        for(int j = 0; j < strlen(s); j++){
            let[s[j] - 'A']++;
        }
        while(let[25] > 0){
            num[0]++;
            let['Z' - 'A']--;
            let['E' - 'A']--;
            let['R' - 'A']--;
            let['O' - 'A']--;
        }
        while(let[22] > 0){
            num[2]++;
            let['T' - 'A']--;
            let['W' - 'A']--;
            let['O' - 'A']--;
        }
        while(let[20] > 0){
            num[4]++;
            let['F' - 'A']--;
            let['O' - 'A']--;
            let['U' - 'A']--;
            let['R' - 'A']--;
        }
        while(let[14] > 0){
            num[1]++;
            let['O' - 'A']--;
            let['N' - 'A']--;
            let['E' - 'A']--;
        }
        while(let[17] > 0){
            num[3]++;
            let['T' - 'A']--;
            let['H' - 'A']--;
            let['R' - 'A']--;
            let['E' - 'A'] -= 2;
        }
        while(let[5] > 0){
            num[5]++;
            let['F' - 'A']--;
            let['I' - 'A']--;
            let['V' - 'A']--;
            let['E' - 'A']--;
        }
        while(let[23] > 0){
            num[6]++;
            let['S' - 'A']--;
            let['I' - 'A']--;
            let['X' - 'A']--;
        }
        while(let[18] > 0){
            num[7]++;
            let['S' - 'A']--;
            let['E' - 'A'] -= 2;
            let['V' - 'A']--;
            let['N' - 'A']--;
        }
        while(let[6] > 0){
            num[8]++;
            let['E' - 'A']--;
            let['I' - 'A']--;
            let['G' - 'A']--;
            let['H' - 'A']--;
            let['T' - 'A']--;
        }
        while(let[13] > 0){
            num[9]++;
            let['N' - 'A'] -= 2;
            let['I' - 'A']--;
            let['E' - 'A']--;
        }

        for (int k = 0; k < 10; k++){
            while(num[k] > 0){
                cout2 << k;
                num[k]--;
            }
        }
        cout2 << endl;
    }

    cout2 << flush;
    cout2.flush();
    cout2 << endl;

    cin2.close();
    cout2.close();

    return 0;
}