#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int a[4],b[4];
    int t,x,n,m;
    cin >> t;
    for (int k = 0; k < t; k++){
        cout << "Case #" << k + 1 << ": ";
        cin >> n;
        for (int i = 0; i < n-1; i++){
            for (int j = 0; j < 4; j++){
                cin >> x;
            }
        }
        for (int j = 0; j < 4; j++){
            cin >> a[j];
        }
        for (int i = n; i < 4; i++){
            for (int j = 0; j < 4; j++){
                cin >> x;
            }
        }

        cin >> m;
        for (int i = 0; i < m-1; i++){
            for (int j = 0; j < 4; j++){
                cin >> x;
            }
        }
        for (int j = 0; j < 4; j++){
            cin >> b[j];
        }
        for (int i = m; i < 4; i++){
            for (int j = 0; j < 4; j++){
                cin >> x;
            }
        }
        int fl = 0;
        for (int i = 0; i < 4; i++){
                for (int j = 0; j < 4; j++){
                    if (a[i] == b[j]){
                        x = a[i];
                        fl++;
                    }
                }
        }
        if (fl == 0){
        cout << "Volunteer cheated!" << endl;
        }
        if (fl == 1){
        cout << x << endl;
        }
        if (fl > 1){
        cout << "Bad magician!" << endl;
        }


    }

    return 0;
}
