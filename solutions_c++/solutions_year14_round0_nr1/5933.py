#include <algorithm>
#include <iterator>
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

int main(void)
{
    int T;
    string tmps;

    cin >> T;
    set<int> s[2];
    for (int t = 1; t <= T; t++){
        int l;
        for (int si = 0; si < 2; si++){
            cin >> l;
            getline(cin, tmps);
            for (int i = 1; i <= 4; i++){
                getline(cin, tmps);
                if (i == l){
                    istringstream iss(tmps);
                    s[si] = set<int>(
                            (istream_iterator<int>(iss)),
                            istream_iterator<int>()
                            );

                }
            }
        }
        vector<int> v;
        set_intersection(s[0].begin(), s[0].end(),
                         s[1].begin(), s[1].end(),
                         back_inserter(v));
        cout << "Case #" << t << ": ";
        switch (v.size()){
            case 1:
                cout << v[0] << endl;
                break;
            case 0:
                cout << "Volunteer cheated!\n";
                break;
            default:
                cout << "Bad magician!\n";
        }
    }

    return 0;
}
