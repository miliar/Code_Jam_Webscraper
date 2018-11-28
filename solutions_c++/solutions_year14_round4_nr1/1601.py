#include <bits/stdc++.h>

int main ( void ) {

    int T, N, C, count, tc, a, i;

    std::multiset<int> A;
    std::multiset<int>::iterator it;

    std::cin >> T;

    for ( tc = 1 ; tc <= T ; ++ tc ) {
        std::cin >> N >> C;

        A.clear();
        for ( i = 0 ; i < N ; ++ i ) {
            std::cin >> a;
            A.insert(-a);
        }

        count = 0;
        while ( !A.empty() ) {
            ++ count;
            a = -(*A.begin());
            A.erase(A.begin());

            if ( (it = A.lower_bound(a - C)) != A.end() ) {
                // std::cout << a << " " << C - a << " " << -(*it) << std::endl;
                A.erase(it);
            }
        }

        std::cout << "Case #" << tc << ": " << count << "\n";
    }

    return 0;
}
