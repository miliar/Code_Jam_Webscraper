#include <iostream>
#include <set>
using namespace std;

int main () {
    int t, instance = 1;
    int lawn[100][100];
    ios::sync_with_stdio (false);
    
    cin >> t;
    while (t--) {
        int m, n, _min = 1000;
        bool no = false;
        cin >> m >> n;
        set<int> values;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cin >> lawn[i][j];
                values.insert (lawn[i][j]);  
            }
        }

        for (set<int>::iterator it = values.begin(); it != values.end(); it++) {
            int val = *it;
            
            for (int i = 0; i < m; i++) {
                
                for (int j = 0; j < n; j++) {
                    if (lawn[i][j] < val) continue;

                    if (lawn[i][j] == val) {
                        bool ok1 = true, ok2 = true;
                        
                        for (int k = 0; k < m; k++) {
                            if (lawn[k][j] > val) { ok1 = false; break; }
						} if (ok1) for (int k = 0; k < m; k++) lawn[k][j] = 0;
						
						for (int k = 0; k < n; k++) {
                            if (lawn[i][k] > val) { ok2 = false; break; }
						} if (ok2) for (int k = 0; k < m; k++) lawn[i][k] = 0;
						
						no = !(ok1 | ok2);
                        if (no) break;
                    }
                    if (no) break;
                }
                if (no) break;
            }
            if (no) break;
        }
        
        cout << "Case #" << instance++;
        if (no) cout << ": NO\n";
        else    cout << ": YES\n";
    }

    return 0;
}
