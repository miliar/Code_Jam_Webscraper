#include <iostream>
#include <set>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int firstAnswer, secondAnswer;
        int dummy;
        cin >> firstAnswer;
        int limit = (firstAnswer - 1) * 4;
        for (int j = 0; j < (limit); j++)
            cin >> dummy;
        int fline[4];
        cin >> fline[0];
        cin >> fline[1];
        cin >> fline[2];
        cin >> fline[3];
        for (int j = 0; j < 12 - limit; j++)
            cin >> dummy;
        cin >> secondAnswer;
        limit = (secondAnswer - 1) * 4;
        for (int j = 0; j < limit; j++)
            cin >> dummy;
        int sline[4];
        cin >> sline[0];
        cin >> sline[1];
        cin >> sline[2];
        cin >> sline[3];
        for (int j = 0; j < 12 - limit; j++)
            cin >> dummy;
        set<int> result;
        for (int k = 0; k < 4; k++)
        {
            for (int l = 0; l < 4; l++)
            {
                if (fline[k] == sline[l])
                {
                    result.insert(fline[k]);
                }
            }
        }
        if (result.size() == 1) {
            cout << "Case #" << i << ": " << *result.begin() << endl;
        } else if (result.size() > 1) {
            cout << "Case #" << i << ": " << "Bad magician!" << endl;
        } else {
            cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
        }
        result.clear();
    }
}
