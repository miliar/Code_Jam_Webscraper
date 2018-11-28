#include <iostream>
#include <set>
#include <cassert>
#include <limits>


long solve(long C, long D, long V, std::set<long> coins)
{
    assert(D == (int)coins.size());
    std::cerr << C << " " << D << " " << " " << V << " " << std::endl;

    int new_coins = 0;

    // we always need a coin with value 1
    if (coins.insert(1).second) { // returns true if actually inserted
        new_coins += 1;
    }

    // the continuous interval we can describe with coins up to mic, inclusive.
    // mic.. max interval coin
    // il .. interval length
    long mic = 1;
    /* int il = C; // we can pay everything up to C with only 1-coins. */
    long upto = C; // how far we ensured continuity, inclusive


    while (upto < V) {

        std::cerr << "upto=" << upto << std::endl;

        long coin = std::numeric_limits<long>::max();
        for (long c : coins) {
            if (c <= mic) continue;
            coin = c;
            break;
        }

        assert(coin > mic);

        if (coin <= upto + 1) {
            upto = coin * C + upto;
            mic = coin;
        } else {
            assert(coin > upto + 1);
            // we cannot reach upto + 1.
            // this means we need to add this coin
            coins.insert(upto + 1);
            new_coins += 1;
        }

    }

    return new_coins;
}


void run_test_case()
{
    long C, D, V;
    std::cin >> C >> D >> V;
    std::set<long> coins;
    for (long c = 0; c < D; ++c) {
        long coin;
        std::cin >> coin;
        coins.insert(coin);
    }

    std::cout << solve(C, D, V, coins);
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
