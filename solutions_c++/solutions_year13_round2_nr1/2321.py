/* Codejam 2013 round 1B
 * Problem A. Osmos
 */
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned int uint;

uint motes[128];
uint n;


uint solve(uint &mote_idx, uint &size, uint ops)
{
    if (mote_idx == n) {
        return ops;
    }
    
    uint smallest = motes[mote_idx];
    if (smallest < size) {
        size += smallest;
        mote_idx++;
        //printf("size: %d, idx: %d, ops: %d\n", size, mote_idx, ops);
        return solve(mote_idx, size, ops);
    } else {
        ops++;
        // try adding the largest possible mote that we can absorb
        uint mote_idx_add = 69;
        uint size_add = 69;
        uint ops_add = 69;
        if (size > 1) {
            mote_idx_add = mote_idx;
            size_add = size + size - 1;
            ops_add = solve(mote_idx_add, size_add, ops);
        }
        
        // try removing the obstructing mote
        uint mote_idx_remove = mote_idx + 1;
        uint size_remove = size;
        uint ops_remove = solve(mote_idx_remove, size_remove, ops);
        
        
        if (size <= 1 || ops_remove < ops_add) {
            mote_idx = mote_idx_remove;
            size = size_remove;
            return ops_remove;
        } else {
            mote_idx = mote_idx_add;
            size = size_add;
            return ops_add;
        }
    }
}


int main()
{
    uint t, a, current, ops, mote_idx;
    vector<uint> motes_vec;
    scanf("%d", &t);
    for (uint case_num = 1; case_num <= t; case_num++) {
        motes_vec.resize(0);
        scanf("%d %d", &a, &n);
        for (uint i = 0; i < n; i++) {
            scanf("%d", &current);
            motes_vec.push_back(current);
        }
        sort(motes_vec.begin(), motes_vec.end());
        copy(motes_vec.begin(), motes_vec.end(), motes);
        
        mote_idx = 0;
        ops = solve(mote_idx, a, 0);
        printf("Case #%d: %d\n", case_num, ops);
    }

    return 0;
}
