#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

string generate(int N, char s)
{
    vector<string> lineup;
    lineup.push_back(string(1, s));
    for (int i = 1; i <= N; i++) {
        lineup.push_back("");
        for (int j = 0; j < lineup[i-1].size(); j++) {
            if (lineup[i-1][j] == 'R') {
                lineup[i].push_back('R');
                lineup[i].push_back('S');
            }
            else if (lineup[i-1][j] == 'S') {
                lineup[i].push_back('P');
                lineup[i].push_back('S');
            }
            else if (lineup[i-1][j] == 'P') {
                lineup[i].push_back('P');
                lineup[i].push_back('R');
            }
        }
    }
    return lineup[N];
}

string sortP(int N, string lineup)
{
    vector<vector<string> > sorted(N+1, vector<string>());
    for (int i = 0; i < lineup.size(); i++) {
        sorted[0].push_back(string(1, lineup[i]));
    }
    for (int i = 1; i <= N; i++) {
        for (int k = 0; k < sorted[i-1].size(); k += 2) {
            if (sorted[i-1][k] > sorted[i-1][k+1]) {
                sorted[i].push_back(sorted[i-1][k+1] + sorted[i-1][k]);
            } else {
                sorted[i].push_back(sorted[i-1][k] + sorted[i-1][k+1]);
            }
        }
    }
    return sorted[N][0];
}

int main()
{
    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        cout << "Case #" << c << ": ";
        int N, R, P, S;
        cin >> N >> R >> P >> S;

        string lineup = generate(N, 'R');
        int Rc = 0, Pc = 0, Sc = 0;
        for (int i = 0; i < lineup.size(); i++) {
            if (lineup[i] == 'R') Rc++;
            else if (lineup[i] == 'P') Pc++;
            else if (lineup[i] == 'S') Sc++;
        }
        map<char, char> replace;
        if (R == Rc && P == Pc && S == Sc) {
            cout << sortP(N, lineup) << endl;
        }
        else if (R == Pc && P == Sc && S == Rc) {
            cout << sortP(N, generate(N, 'S')) << endl;
        }
        else if (R == Sc && P == Rc && S == Pc) {
            cout << sortP(N, generate(N, 'P')) << endl;
        }
        else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
