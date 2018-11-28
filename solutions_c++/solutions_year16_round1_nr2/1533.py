//
// Created by 강경완 on 16. 4. 16..
//

#include <iostream>

using namespace std;

int main() {

    int n, m;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> m;
        int ary[2600] = {0,};
        int t;
        for (int j = 0; j < 2 * m - 1; j++) {
            for(int k=0; k<m; k++){
                cin >> t;
                ary[t]++;
            }
        }
        cout << "Case #" << i+1 << ":";
        for(int h=1; h<=2500; h++){
            if((ary[h] % 2 )== 1)
                cout << " "<< h ;
        }
        cout << endl;
    }
}