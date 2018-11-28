#include <bits/stdc++.h>

using namespace std;

static 
int computed[10000][10000];

int main() {
    std::ios::sync_with_stdio(false);

    int T, L, X, i, j, k, c, cc;
    char str[10010];

    cin >> T;

    char base_table[4][4] = {
        { 0, 1, 2, 3 }, { 1, 4, 3, 6 }, { 2, 7, 4, 1 }, { 3, 2, 5, 4 },
    };

    char table[8][8];
    for( i = 0; i < 4; i++ ) {
        for( j = 0; j < 4; j++ ) {
            table[i][j] = base_table[i][j];
            table[i][j+4] = (base_table[i][j] + 4) % 8;
            table[i+4][j] = (base_table[i][j] + 4) % 8;
            table[i+4][j+4] = base_table[i][j];
        }
    }


    for( int CASE = 1; CASE <= T; CASE++ ) {
        cin >> L >> X;

        c = cc = 0;
        while(cin.get() != '\n');
        for( i = 0; i < L; i++ ) {
            str[i] = cin.get() - 'i' + 1;
            c = table[c][str[i]];
        }
        i = 0;
        do {
            cc = table[cc][c];
            i++;
        } while( cc != 4 && i < X && i < 4);
        if( cc != 4 || (X % i != 0) || ((X/i) % 2) != 1 ) {
            //cout << X << " " << i << endl;
            goto NO;
        }

        char stre[10000];
        for( i = 0; i < X; i++ ) {
            for( j = 0; j < L; j++ ) {
                stre[i*L+j] = str[j];
            }
        }

        for( i = 0; i < L*X; i++ ) {
            c = 0;
            for( j = i; j < L*X; j++ ) {
                computed[i][j] = c;
                c = table[c][stre[j]];
            }
            computed[i][j] = c;
        }

        for( i = 1; i < L*X; i++ ) {
            for( j = i+1; j < L*X; j++ ) {
                if( computed[0][i] != 1 ) continue;
                if( computed[i][j] != 2 ) continue;
                if( computed[j][L*X] != 3 ) continue;
                goto YES;
            }
        }
        goto NO;

YES:
        std::cout << "Case #" << CASE << ": YES\n";
        continue;
NO:
        std::cout << "Case #" << CASE << ": NO\n";
    }

    return 0;
}
