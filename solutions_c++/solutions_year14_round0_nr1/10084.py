#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#define File_in(input) freopen(input, "r", stdin)
#define File_out(output) freopen(output, "w", stdout)
#define all(x) x.begin(),x.end()
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair <int,int> point;

void printCase(int x){
    cout << "Case #" << x << ": ";
}


int main () {
    File_in("A.in"); File_out("A.out");
    int t, n = 4;
    cin >> t;
    for (int tt = 0; tt < t; tt++) {
        vector <int> v1,v2;
        int w1,w2,val;

        cin >> w1;
        w1--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++){
                cin >> val;
                if (i == w1)
                    v1.push_back(val);
            }
        }
        cin >> w2;
        w2--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++){
                cin >> val;
                if (i == w2)
                    v2.push_back(val);
            }
        }

        int ans = 0;
        int x  = 0;

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (v1[i] == v2[j])
                {
                    ans++;
                    x= v1[i];

                }

            }
        }
        printCase(tt+1);
        if (ans == 0)
            cout << "Volunteer cheated!";
        else if (ans == 1)
            cout << x;
        else
            cout << "Bad magician!";
        cout << endl;

    }
}

