#include <iostream>
#include <queue>

main() {
    int T;
    std::cin >> T;
    for(int t = 1; t <= T; t++) {
        std::cout << "Case #" << t << ": ";
        std::priority_queue<long long> Q;
        long long N, K;
        std::cin >> N >> K;
        Q.push(N);
        while(K > 1) {
            K--;
            long long maxDistance = Q.top() - 1;
            Q.pop();
            long long L_s = (long long) (maxDistance + 1) / 2;
            long long R_s = (long long) (maxDistance) / 2;
            Q.push(L_s);
            Q.push(R_s);
        }
        long long maxDistance = Q.top() - 1;
        Q.pop();
        long long L_s = (long long) (maxDistance + 1) / 2;
        long long R_s = (long long) (maxDistance) / 2;
        Q.push(L_s);
        Q.push(R_s);
        std::cout << L_s << ' ' << R_s << '\n';
    }
    return 0;
}
