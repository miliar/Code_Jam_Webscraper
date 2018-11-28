#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int T, nr, line[5], line2[5];

int main(){

    freopen("fis.in", "r", stdin);
    freopen("fis.out", "w", stdout);

    cin >> T;

    for(int t = 1; t <= T; ++t){

        int opt, x;
        cin >> opt;

        for(int i = 1; i <= 4; ++i){
            for(int j = 1; j <= 4; ++j){
                cin >> x;
                if(i == opt)
                    line[j] = x;

            }
        }

        cin >> opt;

        for(int i = 1; i <= 4; ++i){
            for(int j = 1; j <= 4; ++j){
                cin >> x;
                if(i == opt)
                    line2[j] = x;

            }
        }
        
        int nr = 0;
        int sol = 0;

        for(int i = 1; i <= 4; ++i){
            for(int j = 1; j <= 4; ++j){
               if(line[i] == line2[j]){
                   ++nr;
                   sol = line[i];
               }
            }
        }

        cout << "Case #" << t << ": ";

        switch(nr){
            case 0:
                cout << "Volunteer cheated!";
                break;
            case 1:
                cout << sol;
                break;
            default:
                cout << "Bad magician!";

        }
        cout << '\n';
    }
    return 0;
}