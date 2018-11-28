#include <iostream>
#include <queue>
#include <algorithm>
#include <set>
#include <cstdio>

#define MOD 1000002013

long cost(long N, long i) {
    long s1 = (N*(N+1))/2;
    N -= i;
    long s2 = (N*(N+1))/2;
    return s1 - s2;
}

int main() {
    long T;
    std::cin >> T;
    for(long C = 1; C <= T; C ++) {
        long N, M;
        std::cin >> N >> M;

        std::priority_queue<std::pair<long, long>, std::vector<std::pair<long, long> >, std::greater<std::pair<long, long> > > oq, eq;
        std::priority_queue<std::pair<long, long>, std::vector<std::pair<long, long> >, std::less<std::pair<long, long> > > pq;

        long ocost = 0;
        for(long i = 0; i < M; i ++) {
            long o, e, p;
            std::cin >> o >> e >> p;

            ocost += p*cost(N, e-o);
            oq.push(std::make_pair(o, p));
            eq.push(std::make_pair(e, p));
        }

        long mcost = 0;
        while(oq.size() > 0 || eq.size() > 0) {
            while(oq.size() > 0 && oq.top().first <= eq.top().first) {
                pq.push(oq.top());
                oq.pop();
            }

            std::pair<long, long> e = eq.top(); eq.pop();

            long remaining = e.second;
            while(remaining > 0) {
                std::pair<long, long> pt = pq.top(); pq.pop();

                long sub = std::min(remaining, pt.second);
                remaining -= sub; pt.second -= sub;
                mcost += sub*cost(N, e.first - pt.first);
                //std::printf("Faking %i -> %i (%i passengers)\n", pt.first, e.first, sub);
                if(pt.second > 0) pq.push(pt);
            }
        }
        std::printf("Case #%li: %li\n", C, (ocost - mcost) % MOD);
        //std::cout << mcost - ocost << std::endl;
    }
    return 0;
}
