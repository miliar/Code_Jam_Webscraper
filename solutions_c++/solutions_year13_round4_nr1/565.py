#include <cstdio>
#include <gmpxx.h>
#include <vector>
#include <algorithm>
#include <stack>
#include <cassert>
#include <iostream>

using namespace std;

struct event {
    int pos, number;
    event(int pos, int number) : pos(pos), number(number) { }

    bool operator<(const event& p) const {
        if(pos != p.pos) return pos < p.pos;
        return number > p.number;
    }
};

int N;
mpz_class cost(mpz_class dist) {
    return dist*N - dist*(dist-1)/2;
}

int main() {
    int t;
    scanf("%d", &t);

    for(int z = 1; z <= t; z++) {
        int M;
        scanf("%d %d", &N, &M);

        int o[M], e[M], p[M];
        vector<event> events;
        mpz_class original = 0;

        for(int i = 0; i < M; i++) {
            scanf("%d %d %d", &o[i], &e[i], &p[i]);
            events.push_back(event(o[i], p[i]));
            events.push_back(event(e[i], -p[i]));
            original += cost(e[i] - o[i]) * p[i];
        }

        sort(events.begin(), events.end());
        stack<event> left;
        mpz_class count = 0;

        for(int i = 0; i < events.size(); i++) {
            assert(events[i].number);
            if(events[i].number > 0)
                left.push(events[i]);
            else {
                int to_remove = -events[i].number;

                while(to_remove) {
                    assert(left.size());
                    int this_step = min(left.top().number, to_remove);

                    to_remove -= this_step;
                    left.top().number -= this_step;
                    count += cost(events[i].pos - left.top().pos) *
                        this_step;

                    if(left.top().number == 0)
                        left.pop();
                }
            }
        }

        cout << "Case #" << z << ": " << original - count << endl;
    }
}
