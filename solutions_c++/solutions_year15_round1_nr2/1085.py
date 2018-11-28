#include <iostream>
#include <queue>
#include <cassert>


struct Barber
{
    long free_at;
    long index;
    long duration;
};

namespace std {
    template<>
    struct greater<Barber>
    {
        bool operator()(const Barber &lhs, const Barber &rhs) const
        {
            assert(lhs.index != rhs.index);
            return (lhs.free_at > rhs.free_at) || (lhs.free_at == rhs.free_at && lhs.index > rhs.index);
        }
    };
}


void run_test_case()
{
    // read input from stdin
    long B, N;
    std::cin >> B >> N;

    std::vector<Barber> barbers;
    double throughput = 0;

    for (int i = 1; i <= B; ++i) {
        long m;
        std::cin >> m;

        throughput += 1/(double)m;

        Barber b;
        b.index = i;
        b.free_at = 0;
        b.duration = m;
        barbers.push_back(b);
    }

    // approximate t where N will be served
    long t = (long)((double)N / throughput) - 1;
    assert(t >= 0);
    /* std::cerr << "t=" << t << "    throughput=" << throughput << std::endl; */

    // how much served until t?
    long min_free_at = -1;
    for (Barber b : barbers) {
        long served = t / b.duration;
        b.free_at = served * b.duration;
        if (b.free_at < min_free_at || min_free_at < 0) {
            min_free_at = b.free_at;
        }
        assert(b.free_at <= t);
    }

    long n = 0;

    std::priority_queue<Barber, std::vector<Barber>, std::greater<Barber>> q;

    for (Barber b : barbers) {
        long served = min_free_at / b.duration;
        n += served;
        b.free_at = served * b.duration;
        assert(b.free_at <= min_free_at);
        q.push(b);
    }
    
    /* std::cerr << "n=" << n << "    N=" << N << std::endl; */
    assert(n < N);

    // solve
    while (true) {
        // next customer
        ++n;
        // next free barber
        Barber b = q.top();
        q.pop();
        /* std::cerr << "barber " << b.index << " free at " << b.free_at << std::endl; */
        // serve customer n
        if (n == N) {
            std::cout << b.index;
            return;
        } else {
            b.free_at += b.duration;
            q.push(b);
        }
    }
}


int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        std::cout << "Case #" << t << ": ";
        run_test_case();
        std::cout << '\n';
    }

    return 0;
}
