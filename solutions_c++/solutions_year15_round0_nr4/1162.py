#include <iostream>
#include <string>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <vector>


/* #define DEBUG(x) do { x; } while (false) */

#ifndef DEBUG
#   define DEBUG(x) do { } while (false)
#endif


constexpr auto RICHARD = "RICHARD";
constexpr auto GABRIEL = "GABRIEL";


// returns "GABRIEL" if board can be filled with every given omino.
// returns "RICHARD" if "impossible" omino can be chosen
std::string omino(int X, int R, int C)
{
    DEBUG(std::cerr << "\n\n\n\n\nX=" << X << "  R=" << R << "  C=" << C << std::endl);
    assert(X >= 1);
    assert(R >= 1);
    assert(C >= 1);

    // without loss of generality, let R <= C.
    if (R > C) { std::swap(R, C); }
    assert(R <= C);

    if (X == 1) {
        // The only omino for X=1 is the 1-cell. Can always fill the field with those.
        return GABRIEL;
    }

    if (X >= 7) {
        // Can choose an omino with a 1-hole in it => cannot be filled with an X-omino where X > 1.
        // Example omino with 1-hole for X=7:
        //      ***
        //      * *
        //      **
        return RICHARD;
    }

    // Every omino has X elements. Being able to fill the field means the number of tiles is divisible by X.
    if ((R*C) % X != 0) {
        return RICHARD;
    }

    // Make the "biggest-spanning" omino and see if it fits in the field:
    // for X=4:
    //      ***
    //      *
    {
        int w = 1 + (X-1)/2 + (1-X%2);
        int h = 1 + (X-1)/2;
        if ( (w > R || h > C) && (w > C || h > R) ) {
            return RICHARD;
        }
    }

    // At this point, the field is divisible by X. Thus it can always be filled for X=2.
    if (X == 2) {
        return GABRIEL;
    }

    if (X == 3) {
        // Both X=3 ominoes can be placed in a corner (after the previous checks).
        return GABRIEL;
    }

    assert(4 <= X && X <= 6);

    // Gabriel will win if he can place Richard's omino in such a way that
    // the remaining tiles form one connected region.
    //
    // Better formulation:
    // Gabriel will win if and only if he can place Richard's omino in such a way that all connected regions of free cells
    // arising from the placement are divisible by X.

    // Thus, as Richard, begin by spanning the field (through the larger side) to divide the field.
    // Bars (****) won't work, shift it like this:
    //    **
    // ****





    if (X <= R && X <= C) {
        // can't split the field
        return GABRIEL;
    }

    assert(R <= C);
    // try to span short side (need at least 2*R-1 cells or it can just be rotated and fit)
    if (X >= 2*R-1) {
        // make a cross shape (here: w=9, h=5, p=1, q=0)
        // *********
        //  *
        //  *
        //  *
        //  *
        int h = R;
        int w = X - R + 1;
        assert(w >= R);
        assert(w <= C);
        assert(h + w - 1 == X);
        for (int p = 1; p <= w/2; ++p) {
            // p is the position of the intersection of the T shape (horizontally)

            for (int q = 0; q <= h/2; ++q) {
                // q is the position of the intersection of the T shape (vertically)

                if (w == R && C > R && q == 0) {
                    // a T won't work in this case, as we can rotate it by 90 degrees and always fill the field
                    // checking for q=0 might yield a false RICHARD
                    continue;
                }

                bool can_fill = false;
                for (int offset = 0; offset <= C - w; ++offset) {
                    // offset is the horizontal position of the omino

                    std::vector<int> fields;
                    if (offset == 0) {
                        // two fields on the left side
                        fields.push_back(q*p);
                        fields.push_back((R-q-1)*p);
                    } else {
                        // one field on the left side
                        fields.push_back(R*offset + (R-1)*p);
                    }
                    if (offset + w == C) {
                        // two fields on the right side
                        fields.push_back(q*(w-p-1));
                        fields.push_back((R-q-1)*(w-p-1));
                    } else {
                        // one field on the right side
                        fields.push_back(R*(C-w-offset) + (R-1)*(w-p-1));
                    }
                    assert(std::accumulate(std::begin(fields), std::end(fields), 0) + X == R*C);

                    if (std::all_of(std::begin(fields), std::end(fields), [X](int n) { return n%X == 0; })) {
                        can_fill = true;
                        break;
                    }
                }

                if (!can_fill) {
                    // found an omino!
                    return RICHARD;
                }

            }
        }
    }

    // try to span long side

    return GABRIEL;
}

int main()
{
    int T;
    std::cin >> T;

    for (int t = 1; t <= T; ++t) {
        int X, R, C;
        std::cin >> X >> R >> C;

        auto result = omino(X, R, C);
        std::cout << "Case #" << t << ": " << result << std::endl;
    }

    return 0;
}
