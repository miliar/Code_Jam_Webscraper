#include <bits/stdc++.h>

using namespace std;

const int X = 11;
int jp[X][X], js[X][X], ps[X][X];

vector <pair<pair <int, int>, int>> answer;
vector <pair<pair <int, int>, int>> cur;

void gen(int ln, int a, int b, int c, int J, int P, int S) {
    if(ln > answer.size()) {
        answer = cur;
    }
    for (int i = a; i < J; i++) {
        for (int j = (i == a) ? b : 0; j < P; j++) {
            for (int z = ((j == b) ? c + 1 : 0); z < S; z++) {
                if (jp[i][j] && js[i][z] && ps[j][z]) {
                    jp[i][j]--;
                    js[i][z]--;
                    ps[j][z]--;
                    cur.push_back({{i, j}, z});
                    gen(ln + 1, i, j, z, J, P, S);
                    jp[i][j]++;
                    js[i][z]++;
                    ps[j][z]++;
                    cur.pop_back();
                }
            }
        }
    }
}

void solution() {
    int J, P, S, k;
    cin >> J >> P >> S >> k;
    
    for (int i = 0; i < X; i++) {
        for (int j = 0; j < X; j++) {
            jp[i][j] = js[i][j] = ps[i][j] = k;
        }
    }
    answer.clear();
    gen(0, 0, 0, -1, J, P, S);
    cout << answer.size() << '\n';
    
    for (int i = 0; i < answer.size(); i++) {
        cout << answer[i].first.first + 1 << ' ' << 
            answer[i].first.second + 1 << ' ' << 
            answer[i].second + 1 << '\n';
    }
    
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        solution();
    }
    return 0;
}
