#include <iostream>

using namespace std;

int main(){
    int table[200][200];
    int t;
    int n, m;

    cin >> t;

    for(int w = 0; w < t; w++){
        cin >> n >> m;

        bool possible = true;

        for(int x = 0; x < n; x++){
            for(int y = 0; y < m; y++){
                cin >> table[x][y];
            }
        }

        for(int x = 0; x < n; x++){
            for(int y = 0; y < m; y++){
                if(table[x][y] != 100){
                    bool ok = true;

                    for(int w = 0; w < m; w++){
                        ok = ok && (table[x][w] <= table[x][y]);
                    }

                    if(!ok){
                        ok = true;

                        for(int w = 0; w < n; w++){
                            ok = ok && (table[w][y] <= table[x][y]);
                        }
                    }

                    possible = possible && ok;
                }
            }
        }

        if(possible)
            cout << "Case #" << (w+1) << ": YES" << endl;
        else
            cout << "Case #" << (w+1) << ": NO" << endl;
    }

    return 0;
}
