// -*- mode:c++; tab-width:4; c-basic-offset:4; indent-tabs-mode:nil -*-  
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void absorb(long long current, long long target, long long & newMote, int & count)
{
    if (current > target) {
        newMote = current + target;
    }
    else {
        count++; // add a new mote of the size (current-1)
        current = current + current -1;
        absorb(current, target, newMote, count);
    }
}

int main()
{
    int T;
    int i, j, count, minCost;
    int A, N;
    long long current, newMote;
    vector<long long> motes(100);
    vector<int> costs(100);

    cin >> T;
    
    for (i=0; i<T; i++) {
        cin >> A >> N;
        for (j=0; j<N; j++) {
            cin >> motes[j];
        }
        if (A == 1) {
            minCost = N;
        }
        else {
            sort(motes.begin(), motes.begin()+N);
            current = A;
            for (j=0; j < N; j++) {
                count = 0;
                absorb(current, motes[j], newMote, count);
                current = newMote;
                if (j == 0)
                    costs[j] = count;
                else
                    costs[j] = costs[j-1]+count;
            }
            minCost = N;
            for (j=0; j<N; j++) {
                minCost = min(minCost, costs[j] + (N-j-1));
            }
        }
        cout << "Case #" << i+1 << ": " << minCost << endl;
    }
    return 0;
}
