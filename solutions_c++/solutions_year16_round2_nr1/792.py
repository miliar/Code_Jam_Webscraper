#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

int u[100];
int cnt[1000];

void solve(){
    memset(u,0,sizeof(u));
    memset(cnt,0,sizeof(cnt));
    string s;
    cin >> s;
    for (int i = 0; i < s.length(); i++) cnt[s[i]]++;
    while (cnt['Z']) {
        u[0]++;
        cnt['Z']--, cnt['E']--, cnt['R']--, cnt['O']--;
    }
    while (cnt['W']){
        u[2]++;
        cnt['T']--, cnt['W']--, cnt['O']--;
    }
    while (cnt['X']){
        u[6]++;
        cnt['S']--, cnt['I']--, cnt['X']--;
    }
    while (cnt['G']){
        u[8]++;
        cnt['E']--, cnt['I']--, cnt['G']--, cnt['H']--, cnt['T']--;
    }
    while (cnt['S']){
        u[7]++;
        cnt['S']--, cnt['E']--, cnt['V']--, cnt['E']--, cnt['N']--;
    }
    while (cnt['U']){
        u[4]++;
        cnt['F']--, cnt['O']--, cnt['U']--, cnt['R']--;
    }
    while (cnt['F']){
        u[5]++;
        cnt['F']--, cnt['I']--, cnt['V']--, cnt['E']--;
    }
    while (cnt['O']){
        u[1]++;
        cnt['O']--, cnt['N']--, cnt['E']--;
    }
    while (cnt['R']){
        u[3]++;
        cnt['T']--, cnt['H']--, cnt['R']--, cnt['E']-= 2;
    }
    while (cnt['N']){
        u[9]++;
        cnt['N'] -= 2, cnt['I']--, cnt['E']--;
    }
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < u[i]; j++) cout << i;
    cout << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ": ";
        solve();
    }
    return 0;
}
