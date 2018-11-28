#include <stdio.h>
#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <vector>
#include <assert.h>

using namespace std;

typedef unsigned int uint;

int main()
{
	uint T;
    cin >> T;

    uint grid[4][4];    
    uint first_row, second_row;
    vector<uint> candidates (8);
    for(int i = 1; i <= T; ++i)
    {
        vector<uint> found;
        cin >> first_row;
        for(int j = 0; j < 4; ++j)
            for(int k = 0; k < 4; ++k)
                cin >> grid[j][k];

        for(int k = 0; k < 4; ++k)
            candidates[k] = grid[first_row-1][k];

        cin >> second_row;
        for(int j = 0; j < 4; ++j)
            for(int k = 0; k < 4; ++k)
                cin >> grid[j][k];

        for(int k = 0; k < 4; ++k)
            candidates[k+4] = grid[second_row-1][k];

        sort(candidates.begin(), candidates.end());
        assert(candidates.size() == 8);
        for(int k = 0; k < 7; ++k) {
            if (candidates[k] == candidates[k+1])
                found.push_back(candidates[k]);
        }
        if (found.size() == 0)
            cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
        else if (found.size() == 1)
            cout << "Case #" << i << ": " << found[0] << endl;
        else
            cout << "Case #" << i << ": " << "Bad magician!" << endl;
    }
	return 0;
}