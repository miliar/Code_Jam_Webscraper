#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        int n;
        cin >> n;
        vector <float> naomi(n), ken(n);
        for (int i = 0; i < n; i++)
            cin >> naomi[i];
        for (int i = 0; i < n; i++)
            cin >> ken[i];
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
                int ks = 0;
        int cur = 0;
        for (int i = 0; i < n; i++)
            for (; cur < n; cur++)
                if (ken[cur] > naomi[i]) {
                    cur++;
                    ks++;
                    break;
                }
        int nsdw = 0;
        for (int i = 0; i < n; i++)
            if (ken[i] < naomi[i])
                nsdw++;
            else
                for (int j = n-1; j > i; j--)
                    ken[j] = ken[j-1];
        cout << "Case #" << tc+1 << ": " << nsdw << " ";
        cout << n-ks << endl;
    }
    return 0;
}