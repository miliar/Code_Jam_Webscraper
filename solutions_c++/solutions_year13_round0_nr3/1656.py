#include <algorithm>
#include <fstream>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

struct big_int
{
    string s;

    bool is_palindrome()
    {
        for (int i = 0, j = s.size() - 1; i < j; ++i, --j)
            if ( s[i] != s[j] )
                return false;

        return true;
    }
};

vector<big_int> sq_pals;

void load_precalc()
{
    //const int PRECALC_N = 1846;
    const int PRECALC_N = 47;

    ifstream pals( "palindromes.txt" );

    sq_pals.resize( PRECALC_N );
    for (int i = 0; i < PRECALC_N; ++i)
        pals >> sq_pals[i].s;
}

bool operator<(big_int const& a, big_int const& b)
{
    if ( a.s.size() < b.s.size() )
        return true;
    else
        if ( a.s.size() > b.s.size() )
            return false;
        else
            return strcmp( a.s.c_str(), b.s.c_str() ) < 0;
}

bool operator==(big_int const& a, big_int const& b)
{
    return a.s == b.s;
}

int main()
{
    load_precalc();

    ifstream in ( "input.txt"  );
    ofstream out( "output.txt" );

    //for (int i = 0; i < 15; ++i)
    //    out << "sq_pals[" << i << "] = " << sq_pals[i].s << endl;

    int T; in >> T;

    for (int i = 0; i < T; ++i)
    {
        big_int A, B;
        in >> A.s >> B.s;

        // return amount of number in [A..B]
        int low, up;

        low = lower_bound( sq_pals.begin(), sq_pals.end(), A ) - sq_pals.begin();
        up  = lower_bound( sq_pals.begin(), sq_pals.end(), B ) - sq_pals.begin();

        if (sq_pals[up] == B)
            ++up;

        out << "Case #" << (i + 1) << ": " << ( up - low ) << endl;
    }

    return 0;
}
