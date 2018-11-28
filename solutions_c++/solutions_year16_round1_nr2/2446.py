#include <iostream>
#include <queue>
#include <string>
#include <map>
#include <cmath>
#include <cstring>

#define MAXN 51

using namespace std;

struct Node {
    int level;
    int shape[MAXN][MAXN];
    bool is_visit[2 * MAXN];

    Node(int _level, int _shape[MAXN][MAXN], bool _is_visit[2 * MAXN]) {
        level = _level;
        for (int i = 0; i < MAXN; ++i) {
            for (int j = 0; j < MAXN; ++j) {
                shape[i][j] = _shape[i][j];
            }
        }
        for(int i = 0; i < MAXN * 2; i++) {
            is_visit[i] = _is_visit[i];
        }
    }
};

int lists[2 * MAXN][MAXN];
int N;
queue<Node> bfs_queue;

Node bfs() {
    int shape[MAXN][MAXN] = {};
    bool is_visit[2 * MAXN] = {};
    int lists_count;
    Node init(0, shape, is_visit);
    bfs_queue.push(init);

    while (!bfs_queue.empty()) {
//        cout << "queue size: " << bfs_queue.size() << endl;
        Node top = bfs_queue.front();
        bfs_queue.pop();

        lists_count = top.level;
        for (int i = 0; i < MAXN; ++i) {
            for (int j = 0; j < MAXN; ++j) {
                shape[i][j] = top.shape[i][j];
            }
        }

//        for (int p = 0; p < N; ++p) {
//            for (int q = 0; q < N; ++q) {
//                cout << shape[p][q] << " ";
//            }
//            cout << endl;
//        }
//        cout << endl;

        for(int i = 0; i < MAXN * 2; i++) {
            is_visit[i] = top.is_visit[i];
        }
        if(lists_count == 2*N-1) {
            return top;
        }

        for(int i = 0; i < N; i++) {
            bool can_put_in = true;
            for (int j = 0; j < N; j++) {
                if(shape[i][j] != 0 && shape[i][j] != lists[lists_count][j]) {
                    can_put_in = false;
                    break;
                }
                if (can_put_in) {
                    for (int k = 0; k < N; k++) {
                        if(shape[k][j] != 0 && ((k < i && shape[k][j] > lists[lists_count][j])
                                || (k > i && shape[k][j] < lists[lists_count][j]))) {
                            can_put_in = false;
                            break;
                        }
                    }
                }
            }
            if(can_put_in && !is_visit[i]) {
                int tmp_shape[MAXN][MAXN];
                for (int p = 0; p < MAXN; ++p) {
                    for (int q = 0; q < MAXN; ++q) {
                        tmp_shape[p][q] = top.shape[p][q];
                    }
                }
                for (int j = 0; j < N; j++) {
                    tmp_shape[i][j] = lists[lists_count][j];
                }
                bool tmp_is_visit[2 * MAXN] = {};
                for(int j = 0; j < MAXN * 2; j++) {
                    tmp_is_visit[j] = is_visit[j];
                }
                tmp_is_visit[i] = true;
                Node next(lists_count+1, tmp_shape, tmp_is_visit);
//                cout << "Insert row" << endl;
                bfs_queue.push(next);
            }
        }

        for(int i = 0; i < N; i++) {
            bool can_put_in = true;
            for (int j = 0; j < N; j++) {
                if(shape[j][i] != 0 && shape[j][i] != lists[lists_count][j]) {
                    can_put_in = false;
                    break;
                }

                if (can_put_in) {
                    for (int k = 0; k < N; k++) {
                        if(shape[j][k] != 0 && ((k < i && shape[j][k] > lists[lists_count][j])
                           || (k > i && shape[j][k] < lists[lists_count][j]))) {
                            can_put_in = false;
                            break;
                        }
                    }
                }
            }

            if(can_put_in && !is_visit[N + i]) {
                int tmp_shape[MAXN][MAXN];
                for (int p = 0; p < MAXN; ++p) {
                    for (int q = 0; q < MAXN; ++q) {
                        tmp_shape[p][q] = top.shape[p][q];
                    }
                }
                for (int j = 0; j < N; j++) {
                    tmp_shape[j][i] = lists[lists_count][j];
                }
                bool tmp_is_visit[2 * MAXN] = {};
                for(int j = 0; j < MAXN * 2; j++) {
                    tmp_is_visit[j] = is_visit[j];
                }
                tmp_is_visit[N + i] = true;
                Node next(lists_count+1, tmp_shape, tmp_is_visit);
//                cout << "Insert column" << endl;
                bfs_queue.push(next);
            }
        }
    }

    return init;
}





int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {

        memset(lists, 0, sizeof(lists));
        while (!bfs_queue.empty()) {
            bfs_queue.pop();
        }


        cin >> N;
        for (int j = 0; j < 2 * N - 1; j++) {
            for (int k = 0; k < N; k++) {
                cin >> lists[j][k];
            }
        }

        Node result = bfs();
        int index = 0;
        for (; index < 2*N; index++) {
            if(!result.is_visit[index]) {
                break;
            }
        }
        if(index < N) {
            cout << "Case #" << i << ": ";
            for (int j = 0; j < N; j++) {
                cout << result.shape[index][j] << " ";
            }
            cout << endl;
        } else {
            cout << "Case #" << i << ": ";
            for (int j = 0; j < N; j++) {
                cout << result.shape[j][index - N] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}