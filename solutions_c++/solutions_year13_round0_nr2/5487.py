#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
	ifstream cin("B-small-attempt0.in");
	ofstream cout("output.txt");
    int T, N, M, lawn[11][11], row[11], col[11];
    bool flag;
    cin >> T;

    for( int i = 1; i <= T; ++i )
    {
        flag = true;
        memset(row, 0, sizeof row);
        memset(col, 0, sizeof col);

        cin >> N >> M;
        for( int j = 0; j < N; ++j )
        {
            for( int k = 0; k < M; ++k )
            {
                cin >> lawn[j][k];
                if( lawn[j][k] == 1 )
                {
                    row[j]++;
                    col[k]++;
                }
            }
        }

        for( int j = 0; j < N; ++j )
        {
            for( int k = 0; k < M; ++k )
            {
                if( lawn[j][k] == 1 )
                {
                    if( row[j] != M && col[k] != N ) flag = false;
                }
            }
        }

        if( flag ) cout << "Case #" << i << ": YES";
        else cout << "Case #" << i << ": NO";

        if( i != T ) cout << endl;
    }

}
