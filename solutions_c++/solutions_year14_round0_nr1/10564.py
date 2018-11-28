#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <math.h>

using namespace std;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        int r1 , r2 , c1[4][4], c2[4][4];
        cin >> r1;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++)
                cin >> c1[j][k];
        }

        cin >> r2;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++)
                cin >> c2[j][k];
        }

        int count = 0;
        int x;
        bool check = true;
        for(int k = 0; k < 4; k++){
            for(int j = 0; j < 4; j++){
                if(c1[r1-1][k] == c2[r2-1][j]){
                    if(check){
                        x = c1[r1-1][k];
                        check = false;
                    }
                    count++;
                }
            }
        }
        if(count == 1)
            cout << "Case #" << i << ": " << x << "\n";
        else if(count > 1)
            cout << "Case #" << i << ": Bad magician!\n";
        else cout << "Case #" << i << ": Volunteer cheated!\n";
    }
    return 0;
}
