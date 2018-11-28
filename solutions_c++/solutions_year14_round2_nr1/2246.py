#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

string strip(string s){
    string r = s;
    for (int i = 0; i < r.length(); i++) {
        while( r[i] == r[i+1] )
            r.erase( i+1, 1 );
    }
    return r;
}

inline size_t min(size_t x, size_t y, size_t z)
{
    if (x < y)
        return x < z ? x : z;
    else
        return y < z ? y : z;
}

size_t edit_distance(const string& A, const string& B)
{
    size_t NA = A.size();
    size_t NB = B.size();

    vector<vector<size_t> > M(NA + 1, vector<size_t>(NB + 1));

    for (size_t a = 0; a <= NA; ++a)
        M[a][0] = a;

    for (size_t b = 0; b <= NB; ++b)
        M[0][b] = b;

    for (size_t a = 1; a <= NA; ++a)
        for (size_t b = 1; b <= NB; ++b)
        {
            size_t x = M[a-1][b] + 1;
            size_t y = M[a][b-1] + 1;
            size_t z = M[a-1][b-1] + (A[a-1] == B[b-1] ? 0 : 2);
            M[a][b] = min(x,y,z);
        }

    return M[A.size()][B.size()];
}

int main(int argc, const char *argv[])
{
    std::fstream fin( argv[1] );

    int cases;
    fin >> cases;
    for( int i = 1; i <= cases; i++ ){
        std::cout << "Case #" << i << ": ";

        int n;
        fin >> n;
        std::vector<string> s(n);
        for (int j = 0; j < n; j++) {
            fin >> s[j];
        }



        vector<string> s_strip(n);
        bool done = false;
        for (int j = 0; j < n; j++) {
            s_strip[j] = strip(s[j]);
            if( (j > 0) && (s_strip[j] != s_strip[0]) ){
                cout << "Fegla Won";
                done = true;
            }
        }
        if( !done ){
            string s_t = s[0];
            string s_c = s[1];
            int d = edit_distance( s_t, s_c );
            cout << d;
        }
        


        cout << endl;

    }

    return 0;
}
