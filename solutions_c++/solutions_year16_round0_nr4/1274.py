#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>

using namespace std;

int main(int argc, char** argv)
{
    int T = 0;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int K, C, S;
        cin >> K >> C >> S;

        vector<int64_t> result;

        // trivial case
        if (K == 1)
        {
            result.push_back(K);
        }
        else
        {
            // K to the (C-1)
            int64_t offset = 1;
            for (int j = 0; j < (C - 1); j++)
            {
                offset *= K;
            }

            // assuming S == K for now
            for (int j = 0; j < K; j++)
            {
                result.push_back(j*offset + 1);
            }
        }

        cout << "Case #" << (i + 1) << ": ";
        for (int64_t r : result)
        {
            cout << r << " ";
        }
        cout << endl;
    }
}