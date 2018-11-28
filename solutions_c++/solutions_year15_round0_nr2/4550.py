

#include <cstdlib>
#include <cstdio>
#include <cassert>

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;


vector<int> mem;

typedef priority_queue<int> Queue;

int eat(Queue & q, int tm, int tc) {
    //if (mem.size() < M+1) {
    //    mem.resize(M+1, 0);
    //}
    //if (!mem[M]) {
        int M = q.top();
        q.pop();
        int x = M;
        // try to split
        if (M > 3)
        if (tc+1 < tm)
        for (int i = M / 2; i > 0; --i) {
            Queue r(q);
            r.push(i);
            r.push(M-i);
            int y = 1 + eat(r, tm, tc+1);
            if (y < x) {
                x = y;
            }
        }
        return x;
    //    mem[M] = x;
    //}
    //return mem[M];
}

int main(int argc, char ** argv)
{
    // read the tests count
    int T = 0;
    cin >> T;
    // run the test cases
    int t = 0;
    while (t < T)
    {
        ++t;
        // load the values
        int N;
        cin >> N;
        Queue q;
        // only keep the maximal number (others don't matter)
        int M = 0;
        for (int i = 0; i < N; ++i) {
            int K;
            cin >> K;
            q.push(K);
        }
        // solve
        cout << "Case #" << t << ": " << eat(q, q.top(), 0) << endl;
    }
    return EXIT_SUCCESS;
}
