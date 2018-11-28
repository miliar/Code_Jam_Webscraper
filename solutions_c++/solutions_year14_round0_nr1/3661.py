#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main(int argc, char *argv[]) {
    int T = 0;
    cin >> T;
    int n1, n2;
    vector<vector<int> > result;
    int temp;
    for (int t=0; t<T; t++) {
        set<int> row;
        vector<int> resultForT;
        result.push_back(resultForT);
        cin >> n1;
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                cin >> temp;
                if (i == n1-1) row.insert(temp);
            }
        }

        cin >> n2;
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                cin >> temp;
                if (i == n2-1 && row.count(temp) > 0) {
                    result[t].push_back(temp);
                }
            }
        }
    }
    for (int t=0; t<T; t++) {
        cout << "Case #" << t+1 << ": ";
        if (result[t].size() == 0)
            cout << "Volunteer cheated!\n";
        else if (result[t].size() == 1)
            cout << result[t][0] << endl;
        else
            cout << "Bad magician!\n";
    }
}
