#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef vector < vector<int> > field_t;

bool checkField(int x, int y, int n, int m, field_t field)
{
    bool res = false; //By default it is impossible :) Let's try to prove that we wrong

    int z = field[x][y]; //cause i'm lazy.

    //Check given limits. The grass can't be out of 1 - 100
    if (  ( z > 100 )
       || ( z < 1 )
       ) {
        return false; //Booom didy bye bye. What a dirty thing to give numbers out of range :)
    }
    
    //row or col has to be smaller !
    // go over row
    res = true;
    for ( int a = 0 ; a < n ; a++ ) { //a => x
        if (field[a][y] > z) res = false; //failed on row
    }

    if (!res) { //row failed try with col
        res = true;
        for ( int a = 0 ; a < m ; a++ ) { //a => x
            if ( field[x][a] > z) res = false; //failed on col too
        }
    }

    return res;
}

bool checkGarden(int n, int m, field_t field)
{
    for ( int x = 0; x < n ; x++ ) {
        for ( int y = 0; y < m; y++ ) {
            if (!checkField(x,y, n, m, field)) {
                return false;
            }
        }
    }
    return true;
}


int main(void)
{
    ifstream inp("B-large.in", ifstream::in);
    ofstream out("test.out", ofstream::out);

    int tcs;

    inp >> tcs;

    for ( int tc = 0 ; tc < tcs ; tc++ ) {
        int n,m;
        inp >> n >> m;
        field_t field(n);
        //Construct the field in memory.
        for ( int x = 0; x < n; x++ ) {
            for ( int y = 0 ; y < m; y++ ) {
                field[x].resize(m);
                inp >> field[x][y];
            }
        }

        //Use the field data
        cout << "Case #" << tc+1 << ": " << (checkGarden(n,m,field) ? "YES" : "NO") << endl;
        out << "Case #" << tc+1 << ": " << (checkGarden(n,m,field) ? "YES" : "NO") << endl;

    }
}
