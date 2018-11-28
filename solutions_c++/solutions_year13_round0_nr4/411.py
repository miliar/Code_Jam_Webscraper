// #include "common.h"

// -W -Wall -Werror -std=c++0x -Wno-sign-compare -Wfloat-equal

// alias valgrind='\valgrind --malloc-fill=AA --track-origins=yes
// --read-var-info=yes --num-callers=50 --db-attach=no --db-command="kdbg %f -p %p"'

// alias callgrind='\valgrind --tool=callgrind --simulate-cache=yes --dump-instr=yes'

// Valgrind with stdin + debug:
// valgrind --input-fd=3 --db-attach=yes build/foo <input 3</dev/tty

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <deque>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <utility>
#include <vector>
#include <stack>

typedef int Int;
#define int long long

using namespace std;

struct Solution {
    bool solved;
    int keys[40];
    vector<int> opened_boxes;
    
    Solution() {
        solved = false;
        for (int& x : keys)
            x = 0;
    }
};

struct Box {
    int key_to_open;
    int key_diff[40];
    
    Box() {
        for (int& x : key_diff)
            x = 0;
    }
};

bool better(const Solution& candidate, const Solution& current) {
    if (!current.solved)
        return true;
    for (size_t i = 0; i < current.opened_boxes.size(); i++)
        if (candidate.opened_boxes[i] < current.opened_boxes[i])
            return true;
        else if (candidate.opened_boxes[i] > current.opened_boxes[i])
            return false;
    return false;
}

void solve_test() {
    int k, n;
    cin >> k >> n;
    int nsols = (1 << n);
    vector<Solution> solution(nsols);
    solution[0].solved = true;
    for (int i = 0; i < k; i++) {
        int x;
        cin >> x;
        solution[0].keys[x-1]++;
    }
    vector<Box> boxes(n);
    for (Box& x : boxes) {
        int num_keys_inside;
        cin >> x.key_to_open >> num_keys_inside;
        --x.key_to_open;
        x.key_diff[x.key_to_open]--;
        for (int i = 0; i < num_keys_inside; i++) {
            int key;
            cin >> key;
            x.key_diff[key-1]++;
        }
    }
    for (int sol = 0; sol < nsols; sol++)
        for (int box = 0; box < n; box++)
            if ((sol & (1 << box)) == 0 && solution[sol].solved) {
                
                // Try opening box `box'.
                
                if (solution[sol].keys[boxes[box].key_to_open] == 0)
                    continue;
                
                // Create candidate solution.
                
                Solution x;
                x.solved = true;
                for (int i = 0; i < 40; i++)
                    x.keys[i] = solution[sol].keys[i] + boxes[box].key_diff[i];
                x.opened_boxes = solution[sol].opened_boxes;
                x.opened_boxes.push_back(box);
                
                Solution& other = solution[(sol | (1 << box))];
                
                if (better(x, other))
                    other = x;
            }
    if (!solution[nsols-1].solved)
        cout << "IMPOSSIBLE";
    else {
        for (int x : solution[nsols-1].opened_boxes) {
            cout << (x+1);
            if (x != solution[nsols-1].opened_boxes.back())
                cout << " ";
        }
    }
    cout << endl;
}

Int main() {
    
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Case #" << (i+1) << ": ";
        solve_test();
    }
    
    return 0;
}
