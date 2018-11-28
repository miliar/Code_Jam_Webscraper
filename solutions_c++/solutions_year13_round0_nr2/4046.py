#include <iostream>
#include <vector>

using namespace std;

vector<vector<int> > mylawn;

int main()
{
    int t;

    cin >> t;

    bool myans[t];

    for (int i = 0; i < t; ++i){
        myans[i] = false;
        mylawn.clear();
        int n, m;
        cin >> n >> m;

        int mycheck[n][m];
        int maxrows[n], maxcols[m];
        for (int j = 0; j < n; ++j){
            maxrows[j] = 0;
        };
        for (int j = 0; j < m; ++j){
            maxcols[j] = 0;
        };

        for (int j = 0; j < n; ++j){
            vector<int> myadd;
            for (int k = 0; k < m; ++k){
                int tmp;
                cin >> tmp;
                myadd.push_back(tmp);
                if (tmp > maxrows[j]){
                    maxrows[j] = tmp;
                };
                if (tmp > maxcols[k]){
                    maxcols[k] = tmp;
                };
            };
            mylawn.push_back(myadd);
        };
        for (int j = 0; j < n; ++j){
            for (int k = 0; k < m; ++k){
                if ((mylawn[j][k] < maxrows[j]) and (mylawn[j][k] < maxcols[k])){
                    myans[i] = false;
                    goto here;
                };
            };
        };
        myans[i] = true;
        here:;
    };

    for (int i = 0; i < t; ++i){
        cout << "Case #" << i + 1 << ": ";
        if (myans[i] == true){
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        };
    };




    return 0;
}
