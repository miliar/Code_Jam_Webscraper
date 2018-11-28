#include <iostream>

using namespace std;

const int N = 4;
int a[N], b[N];

int main() {
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int tt = 0; tt < t; tt++) {
        int r;
        cin >> r;
        r--;
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++) {
                int c;
                cin >> c;
                if(i == r)
                    a[j] = c;
            }
        cin >> r;
        r--;
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++) {
                int c;
                cin >> c;
                if(i == r)
                    b[j] = c;
            }
        int ans = -1;
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                if(a[i] == b[j]) {
                    if(ans == -1)
                        ans = a[i];
                    else
                        ans = 0;
                }
        cout << "Case #" << tt + 1 << ": ";
        if(ans == -1)
            cout << "Volunteer cheated!\n";
        else if(ans == 0)
            cout << "Bad magician!\n";
        else
            cout << ans << '\n';
    }
    return 0;
}
