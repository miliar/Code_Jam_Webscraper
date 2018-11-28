#include <bits/stdc++.h>

char dir[256];
const int di[] = {-1, 1, 0, 0};
const int dj[] = {0, 0, -1, 1};

int R, C;
std::vector<std::string> map;

bool is_valid ( int i , int j ) {
    return (0 <= i && i < R && 0 <= j && j < C);
}

bool can_change ( int i , int j , int d ) {
    do {
        i = i + di[d]; j = j + dj[d];
    } while ( is_valid(i, j) && map[i][j] == '.' );
    return is_valid(i, j);
}


int main ( void ) {

    int T, d, i, j, t, count;

    dir['^'] = 0;
    dir['v'] = 1;
    dir['<'] = 2;
    dir['>'] = 3;

    std::cin >> T;

    for ( t = 1 ; t <= T ; ++ t ) { 
        std::cout << "Case #" << t << ": ";
        std::cerr << "Case #" << t << ": ";
        std::cin >> R >> C;

        map.resize(R);
        
        std::cerr << R << " " << C << std::endl;
        for ( i = 0 ; i < R ; ++ i ) {
            std::cin >> map[i];
            std::cerr << map[i] << std::endl;
        }

        count = 0;
        for ( i = 0 ; i < R ; ++ i ) {
            for ( j = 0 ; j < C ; ++ j ) {
                if ( map[i][j] != '.' ) {
                    if ( !can_change(i, j, dir[map[i][j]]) ) {
                        for ( d = 0 ; d < 4 ; ++ d ) {
                            if ( d != dir[map[i][j]] && can_change(i, j, d) ) {
                                ++ count;
                                break;
                            }
                        }
                        if ( d == 4 ) {
                            std::cout << "IMPOSSIBLE\n";
                            break;
                        }
                    }
                }
            }
            if ( j < C ) {
                break;
            }
        }
        if ( i == R ) {
            std::cout << count << "\n";
        }

    }

    return 0;
}
