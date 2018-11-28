#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
vector<int> sources[2000];
bool isancestor[2000][2000]; // j is an ancestor of i

int A[2000];
int B[2000];

bool done[2000];

int position;
int ans[2000];

void dfs(int main, int current) {
    for (vector<int>::iterator i = sources[current].begin(); i != sources[current].end(); i++) {
        if (!isancestor[main][*i]) {
            isancestor[main][*i] = true;
            dfs(main, *i);
        }
    }
}

void place(int node) {
    if (done[node]) return;
    vector<int> ancestors;
    for (int i = 0; i < N; i++) {
        if (isancestor[node][i]) place(i);
    }
    ans[node] = (++position);
    done[node] = true;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        for (int i = 0; i < N; i++) {
            cin >> B[i];
        }
        for (int i = 0; i < N; i++) {
            sources[i].clear();
            done[i] = false;
            for (int j = 0; j < N; j++) {
                isancestor[i][j] = 0;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = i-1; j >= 0; j--) {
                if (A[j] == A[i]) {
                    sources[j].push_back(i);
                    break;
                }
            }
            for (int j = i-1; j >= 0; j--) {
                if (A[j] == A[i]-1) {
                    sources[i].push_back(j);
                    break;
                }
            }
            for (int j = i+1; j < N; j++) {
                if (B[j] == B[i]) {
                    sources[j].push_back(i);
                    break;
                }
            }
            for (int j = i+1; j < N; j++) {
                if (B[j] == B[i]-1) {
                    sources[i].push_back(j);
                    break;
                }
            }
        }
        
        for (int i = 0; i < N; i++) {
            dfs(i, i);
        }
        position = 0;
        for (int i = 0; i < N; i++) {
            place(i);
        }
        cout << "Case #" << t << ':';
        for (int i = 0; i < N; i++) {
            cout << ' ' << ans[i];
        }
        cout << '\n';
    }
    return 0;
}
