#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen ("output.txt","w",stdout);
    freopen ("input.txt","r",stdin);
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int c1, c2, aux, ch[4], pos = -1;
        cin >> c1;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) {
                if (i == c1-1)
                    cin >> ch[j];
                else
                    cin >> aux;
            }
        cin >> c2;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) {
                cin >> aux;
                if (i == c2-1) {
                    for (int k = 0; k < 4; k++)
                        if (aux == ch[k]) {
                            if (pos == -1)
                                pos = aux;
                            else
                                pos = -2;
                        }
                }
            }
        cout << "Case #" << tc << ": ";
        if (pos == -2)
            cout << "Bad magician!" << endl;
        else if (pos == -1)
            cout << "Volunteer cheated!" << endl;
        else
            cout << pos << endl;
    }
}
