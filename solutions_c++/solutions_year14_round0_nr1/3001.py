#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        map <int, int> a;
        a.clear();
        int p, x;
        cin >> p;
        for (int i=0;i<4;i++){
            for (int j=0;j<4;j++){
                cin >> x;
                if (i+1 == p)
                    a[x] = 1;
            }
        }
        cin >> p;
        int c = 0;
        int ans = 0;
        for (int i=0;i<4;i++){
            for (int j=0;j<4;j++){
                cin >> x;
                if ((i+1 == p) && (a[x] == 1)){
                    c++;
                    ans = x;
                }
            }
        }
        if (c == 0)
            cout << "Volunteer cheated!" << endl;
        if (c == 1)
            cout << ans << endl;
        if (c >= 2)
            cout << "Bad magician!" << endl;
    }
    return 0;
}
