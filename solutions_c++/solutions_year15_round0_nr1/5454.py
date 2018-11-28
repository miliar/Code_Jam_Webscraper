

#include <cstdlib>
#include <cstdio>
#include <cassert>

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>

using namespace std;


int main(int argc, char ** argv)
{
    // read the tests count
    int T = 0;
    cin >> T;
    // run the test cases
    int t = 0;
    while (t < T)
    {
        ++t;
        // load the values
        int Sm;
        cin >> Sm;
        string P;
        cin >> P;
        // solve
        int x = 0;
        int N = 0;
        for (int i = 0; i < P.size(); ++i) {
            if (i > N) {
               x += i - N;
               N = i;
            }
            N += P[i] - '0';
        }
        cout << "Case #" << t << ": " << x << endl;
    }
    return EXIT_SUCCESS;
}
