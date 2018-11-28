#include <bits/stdc++.h>

using namespace std;
const int N = 105, P = 257, M = 1000007;
int n;
string slowo[N];
vector<int> hashes[20];
vector<int> Hashes[20];
int hSize[2];
// map<int, bool> Mapa[2];
bool Mapa[2][1000007];
int lang[N];
void testCase() {
    cin >> n;
    for(int i = 0; i <= n; i++) {
        getline(cin, slowo[i]);
    }
        for(int j = 1; j <= n; j++) {
            hashes[j].clear();
            int hash = 0;
            for(int k = 0; k < slowo[j].length(); k++) {
                if(slowo[j][k] == ' ') {

                    hashes[j].push_back(hash);
 
                    hash = 0;
                } else {
                    hash = ((long long)hash * P % M + slowo[j][k] - 96) % M;
                }
            }
            hashes[j].push_back(hash);
        }
    int wynik = 1000000000;
    for(int i = 0; i < (1 << (n - 2)); i++) {
//         Mapa[0].clear();
//         Mapa[1].clear();
        Hashes[0].clear();
        Hashes[1].clear();
        lang[1] = 0;
        lang[2] = 1;
        for(int j = 3; j <= n; j++) {
            lang[j] = (i & (1 << (j - 3))) == (1 << (j - 3));
        }
        
        for(int j = 1; j <= n; j++) {
            int hash = 0;
            for(int k = 0; k < hashes[j].size(); k++) {
                    hash = hashes[j][k];
                    if(Mapa[lang[j]][hash] == false) {
                        Hashes[lang[j]].push_back(hash);
                        Mapa[lang[j]][hash] = true;
                    }
            }
        }
        int ans = 0;
//         sort(Hashes[0].begin(), hashes[0] + hSize[0]);
// //         sort(hashes[1].begin(), hashes[1] + hSize[1]);
        int wsk = 0;
        for(int j = 0; j < Hashes[0].size(); j++) {
            if(Mapa[1][Hashes[0][j]])
                ans++;
            Mapa[0][Hashes[0][j]] = false;
        }
        for(int j = 0; j < Hashes[1].size(); j++) {
            Mapa[1][Hashes[1][j]] = false;
        }
        wynik = min(wynik, ans);
    }
    cout << wynik << endl;
    cerr << wynik << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for(int test = 1; test <= t; test++) {
        cout << "Case #" << test << ": ";
        
        cerr << "Case #" << test << ": ";
        testCase();
    }
    return 0;
}