
#include <iostream>

using namespace std;

class problem {
    int first;
    int second;

    int grid1[4][4];
    int grid2[4][4];
public:
    problem(istream &is) {
        is >> first;
        for (int i=0; i<4; ++i) {
            for (int j=0; j<4; ++j) {
                is >> grid1[i][j];
            }
        }

        is >> second;
        for (int i=0; i<4; ++i) {
            for (int j=0; j<4; ++j) {
                is >> grid2[i][j];
            }
        }
    }

    int solve() {
        int flags1[17] = {0};
        int flags2[17] = {0};
        int flags[17];

        for (int j=0; j<4; ++j) {
            flags1[grid1[first-1][j]] = 1;
            flags2[grid2[second-1][j]] = 1;
        }

        for (int i=1; i<=16; ++i) {
            flags[i] = flags1[i] & flags2[i];
        }

        int result = 0;
        for (int i=1; i<=16; ++i) {
            if (flags[i]) {
                if (result == 0) {
                    // first
                    result = i;
                }
                else if (result > 0) {
                    // bad magician
                    result = -1;
                }
            }
        }
        return result;
    }
};

void solve(istream &is, ostream &os)
{
    int t;
    is >> t;

    for (int i=1; i<=t; ++i) {
        problem p(is);
        int r;
        os << "Case #" << i << ": ";

        switch ((r = p.solve())) {
        case -1:
            os << "Bad magician!\n";
            break;

        case 0:
            os << "Volunteer cheated!\n";
            break;

        default:
            os << r << "\n";
            break;
        }
    }
}

int main(int argc, char *argv[])
{

    solve(cin, cout);
    
    return 0;
}
