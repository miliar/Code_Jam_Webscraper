#include <iostream>
#include <cstdio>
#include <queue>
#include <fstream>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

int grid[101][101];

int main() {
    int T;
    in >> T;
    for( int test=1; test<=T; test++ ) {
        int H, W;
        string status = "YES";
        in >> H >> W;
        for( int i=0; i<H; i++ ) {
            for( int j=0; j<W; j++ ) {
                in >> grid[i][j];
            }
        }

        for( int i=0; i<H; i++ ) {
            for( int j=0; j<W; j++ ) {
                bool ok = true;
                for( int k=0; k<W; k++ ) {
                    if( grid[i][k] > grid[i][j] ) ok =false;
                }
                if( ok ) continue;
                ok = true;
                for( int k=0; k<H; k++ ) {
                    if( grid[k][j] > grid[i][j] ) ok = false;
                }
                if( ok ) continue;
                //not ok
                status = "NO";
            }
            if( status == "NO" ) break;
        }


        out << "Case #" << test << ": " << status << endl;
    }

    return 0;
}
