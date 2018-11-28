#include <iostream>

int h[100][100];

int main ( void ) {

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(static_cast<std::ostream*>(nullptr));

    int n, m;
    int i, j, k;
    int n_cases, tc;
    bool is_possible;
    bool horizontal, vertical;

    std::cin >> n_cases;

    for ( tc = 1 ; tc <= n_cases ; ++ tc ) {

        std::cin >> n >> m;

        for ( i = 0 ; i < n ; ++ i ) {
            for ( j = 0 ; j < m ; ++ j ) {
                std::cin >> h[i][j];
            }
        }

        is_possible = true;

        for ( i = 0 ; i < n ; ++ i ) {
            for ( j = 0 ; j < m ; ++ j ) {

                vertical = true;
                for ( k = 0 ; k < n ; ++ k ) {
                    if ( h[k][j] > h[i][j] ) {
                        vertical = false;
                        break;
                    }
                }

                horizontal = true;
                for ( k = 0 ; k < m ; ++ k ) {
                    if ( h[i][k] > h[i][j] ) {
                        horizontal = false;
                        break;
                    }
                }

                is_possible &= vertical || horizontal;
            }
        }

        std::cout << "Case #" << tc << ": " << (is_possible ? "YES" : "NO") << std::endl;

    }


    return 0;
}
