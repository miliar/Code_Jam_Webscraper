#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <list>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <stack>
#include <queue>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for(int k = 1; k <= t; k++) {
        int x,y;
        int a[4][4], b[4][4];
        int count = 0;
        int num;

        cin >> x;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> a[i][j];
            }
        }

        cin >> y;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> b[i][j];
            }
        }

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (a[x-1][i] == b[y-1][j]) {
                    num = a[x-1][i];
                    count++;
                }
            }
        }

        if(count == 1) {
                cout << "Case #" << k << ": " << num << endl;
        } else if (count == 0) {
                cout << "Case #" << k << ": " << "Volunteer cheated!" << endl;
        } else {
                cout << "Case #" << k << ": " << "Bad magician!" << endl;
        }

    }

    return 0;
}
