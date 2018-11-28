#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <set>
#include <map>
#include <stack>
using namespace std;

int main() {
    freopen("input.txt","r", stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    int grid[10][10];
    int n, m;
    set<int> tb;
    for (int t=1;t<=T;++t) {
        cout<<"Case #"<<t<<": ";
        tb.clear();
        cin>> n;
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <=4; ++j)
                cin >> grid[i][j];
        for (int i = 1; i <= 4; ++i)
            tb.insert(grid[n][i]);
        cin>> m;
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <=4; ++j)
                cin >> grid[i][j];
        int ans;
        ans = 0;
        for (int i = 1; i <= 4; ++i) {
            if (tb.find(grid[m][i]) != tb.end()) {
                if (ans == 0)
                    ans = grid[m][i];
                else {
                    ans = - ans;
                    cout << "Bad magician!" << endl;
                    break;
                }
            }
        }
        if (ans == 0) {
            cout << "Volunteer cheated!" << endl;
        }
        if (ans > 0)
            cout << ans << endl;


    }
    return 0;
}




