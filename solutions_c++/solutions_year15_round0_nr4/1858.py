#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
    int t, T;
    int X, R, C;
    string ans, GA = "GABRIEL", RI = "RICHARD";

    cin >> T;

    for (t = 0; t < T; ++t) {
        cin >> X >> R >> C;

        if (X == 1) {
            ans = GA;
        } else if (X == 2) {
            if (R * C % X == 0) {
                ans = GA;
            } else {
                ans = RI;
            }
        } else if (X == 3) {
            if (R * C % X == 0) {
                if (R == 1 || C == 1) {
                    ans = RI;
                } else {
                    ans = GA;
                }
            } else {
                ans = RI;
            }
        } else {
            if (R * C % X == 0) {
                if (R <= 2 || C <= 2) {
                    ans = RI;
                } else {
                    ans = GA;
                }
            } else {
                ans = RI;
            }
        }

        cout << "Case #" << (t + 1) << ": " << ans << endl;
    }

    return 0;
}
