#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

#define Nmax 1024
#define nao v[0]
#define ken v[1]

using namespace std;

int T, N, v[2][1024];

int main(){

    freopen("fis.in", "r", stdin);
    freopen("fis.out", "w", stdout);

    cin >> T;


    for(int t = 1; t <= T; ++t){

        cin >> N;
        int war = 0;
        int dwar = 0;

        for(int p = 0; p < 2; ++p){
            for(int i = 1; i <= N; ++i){
                double x;
                cin >> x;
                x = x * 100000;

                v[p][i] = (int)x;
            }
        }

        sort(v[0] + 1, v[0] + N + 1);
        sort(v[1] + 1, v[1] + N + 1);

        // War
        int u = N;

        for(int i = N; i >= 1; --i){
            if(nao[i] > ken[u]){
                war++;
            }

            else u--;

        }
            
        // D war
        u = N;
        int p = 1;

        int lost = 0;
        for(int i = 1; i <= N; ++i){
            if(nao[i] < ken[p]){
                lost++;
                u--;
            }
            else {
                p++;
            }
        }

        dwar = N - lost;

        cout << "Case #" << t << ": " << dwar << " " << war << '\n';
    }
    return 0;
}