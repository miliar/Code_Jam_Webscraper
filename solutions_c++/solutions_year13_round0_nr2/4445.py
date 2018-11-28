#include <vector>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<ull> vull;
#define FORN(i_, n_) for(int i_ = 0; i_ < (n_); ++i_)

inline bool is_good(int r, int c, vector<vi>& L)
{
    int val = L[r][c];
    bool goodrow = true, goodcol = true;
    FORN(i,L.size()){
        goodcol = (goodcol && (L[i][c] <= val));
    }
    FORN(i, L[0].size()){
        goodrow = (goodrow && (L[r][i] <= val));
    }
    return (goodrow || goodcol);
}

int main (int argc, char** argv)
{
    istream* is = &cin;
    ostream* os = &cout;

    if (argc >= 2) is = new ifstream(argv[1]);
    if (argc == 3) os = new ofstream(argv[2]);

    int T;
    *is >> T;
    FORN(i, T){
        int n, m;
        *is >> n >> m;
        vector<vi> L(n, vi(m, 100));
        FORN(r, n){
            FORN(c, m){
                *is >> L[r][c];
            }
        }
        bool goodpattern = true;
        for(int r = 0; ((r < n) && goodpattern); r++){
            for(int c = 0; ((c < m) && goodpattern); c++){
                goodpattern = is_good(r, c, L);
            }
        }
        string out = goodpattern ? "YES" : "NO";
        *os << "Case #" << i + 1 <<": " << out << endl;
    }
    if (is != &cin) delete is;
    os->flush();
    if (os != &cout) delete os;

    return 0;
}

