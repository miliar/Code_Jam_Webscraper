
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int t;
    cin >> t;
    for (int c = 1; c<= t; c++)  {
        cout << "Case #" << c <<": ";
        int loc1[16];
        int loc2[16];
        int a1, a2;
        cin >> a1;
        for (int i = 0 ; i < 16; i++) {
           int t; cin >> t; loc1[t-1] = i/4 + 1;
        }
        cin >> a2;
        for (int i = 0 ; i < 16; i++) {
           int t; cin >> t; loc2[t-1] = i/4 + 1;
        }
        int ans = -1;
        int tot = 0;
        for (int i = 0 ; i < 16; i++)
        if (loc1[i]==a1 && loc2[i] == a2) {ans  = i+1; tot++;}
        if (tot==0)
            cout <<"Volunteer cheated!";
        if (tot==1)
            cout <<ans;
        if (tot>1)
            cout << "Bad magician!";
        cout << endl;

    }

}
