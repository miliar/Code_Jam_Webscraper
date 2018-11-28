#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

const int KEY_TYPES=201;
const int DEBUG_SHOWKEYS=10;

short keys[1000][KEY_TYPES]; // keys in each step, change to short for large (400)
int K, N;

struct Chest {
    int key_needed;
    int keys_inside;
    int keys[400];

};

Chest chests[201];

char solution[201];

bool chest_in_solution(int c, int step) {
    for (int i=0; i<step; ++i) {
        if (solution[i] == c) return true;
    }

    return false;
}


short total_needed[KEY_TYPES];
short total_present[KEY_TYPES];


bool backtrack(int s)
{
#ifdef DEBUG
    cout << "s=" << s << "; partial solution: ";
    for (int i=0; i<s; ++i) {
        cout << int(solution[i]) << " ";
    }
    cout << endl;
    cout << "keys: ";
    for (int i=1; i<=DEBUG_SHOWKEYS; ++i) {
        cout << int(keys[s][i]) << " ";
    }
    cout << endl;
#endif
    
    for (int i=0; i<KEY_TYPES; ++i) {
        total_present[i] = keys[s][i];
        total_needed[i] = 0;
    }
    for (int c=0; c<N; ++c) {
        if (!chest_in_solution(c,s)) {
            ++total_needed[chests[c].key_needed];
            for (int i=0; i<chests[c].keys_inside; ++i) {
                ++total_present[chests[c].keys[i]];
            }
        }
    }
#ifdef DEBUG
    cout << "total_needed: ";
    for (int i=1; i<=DEBUG_SHOWKEYS; ++i) {
        cout << int(total_needed[i]) << " ";
    }
    cout << endl;
    cout << "total_present: ";
    for (int i=1; i<=DEBUG_SHOWKEYS; ++i) {
        cout << int(total_present[i]) << " ";
    }
    cout << endl;
#endif
    for (int i=0; i<KEY_TYPES; ++i) {
        if (total_needed[i] > total_present[i])  {
            return false;
        }
        // worst heuristic ever
        if (total_present[i] == 1) {
            for (int c=0; c<N; ++c) {
                if (!chest_in_solution(c,s)) {
                    for (int k=0; k<chests[c].keys_inside; ++k) {
                        if (chests[c].keys[k] == i && chests[c].key_needed == i) return false;
                    }
                }
            }
        }
    }
    

    for (int c=0; c<N; ++c) { // chest
        if (!chest_in_solution(c, s) && keys[s][chests[c].key_needed] > 0) {
            solution[s] = c;

            if (s == N-1) return true;
            for (int i=0; i<KEY_TYPES; ++i) {
                keys[s+1][i] = keys[s][i];
            }
            --keys[s+1][chests[c].key_needed];
            for (int i=0; i<chests[c].keys_inside; ++i) {
                ++keys[s+1][chests[c].keys[i]];
            }
            if (backtrack(s+1)) return true;
        }
    }
    return false;
}

int main() {
    int T;

    cin >> T;
    for (int t=0; t<T; ++t) {
        cin >> K >> N;
        for (int i=0; i<KEY_TYPES; ++i) {
            keys[0][i] = 0;
            total_needed[i] = 0;
            total_present[i] = 0;
        }
        for (int k=0; k<K; ++k) {
            int key_type;
            cin >> key_type;
            ++keys[0][key_type];
            ++total_present[key_type];
        }

        for (int c=0; c<N; ++c) {
            cin >> chests[c].key_needed >> chests[c].keys_inside;
            ++total_needed[chests[c].key_needed];
            for (int i=0; i<chests[c].keys_inside; ++i) {
                int key_type;
                cin >> key_type;
                chests[c].keys[i] = key_type;
                ++total_present[key_type];
            }
        }

        bool possible = true;
        bool solution_exists = false;
        // check if there are enough keys in total
        for (int i=0; i<KEY_TYPES; ++i) {
            //cout << "type: " << i << " needed: " << total_needed[i] << " present: " << total_present[i] << endl;
            if (total_needed[i] > total_present[i]) possible = false;
        }
        
        if (possible) {
            // launch backtracking
            for (int i=0; i<N; ++i)
                solution[i] = 0;

            solution_exists = backtrack(0);
        }

        if (solution_exists) {
            cout << "Case #" << t+1 << ": ";
            for (int i=0; i<N-1; ++i)
                cout << int(solution[i])+1 << " ";
            cout << int(solution[N-1])+1 << "\n";
        } else {
            cout << "Case #" << t+1 << ": IMPOSSIBLE\n";
        }

    }

}

