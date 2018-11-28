//
//  main.cpp
//  QualifsLawnMower
//
//  Created by MrAaaah on 12/04/13.
//  Copyright (c) 2013 MrAaaah. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

bool isPossible(vector< vector<int> >& lawn, int i, int j) {
    int h = lawn[i][j];
    bool vertOK = true, horiOK = true;
    
    //check vertical
    for (int n = 0; n < lawn.size(); ++n) {
        if (n != i && lawn[n][j] > h) {
            vertOK = false; break;
        }
    }
    
    //check horizontal
    for (int m = 0; m < lawn[0].size(); ++m) {
        if (m != j && lawn[i][m] > h) {
            horiOK = false; break;
        }
    }
    
    return vertOK || horiOK;
}

int main(int argc, const char * argv[])
{
    int cases, a, n, m;
    bool possible;
    
	cin >> cases;
    
	for (int c = 1; c <= cases; ++c)
	{
        possible = true;
        vector< vector<int> > lawn;

		cin >> n; cin >> m;
        
        for (int i = 0; i < n; ++i) {
            vector<int> line;
            for (int j = 0; j < m; ++j) {
                cin >> a;
                line.push_back(a);
            }
            lawn.push_back(line);
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (!isPossible(lawn, i, j)) {
                    possible = false;
                    break;
                }
            }
            
            if (!possible)
                break;
        }
        
		cout << "Case #" << c << ": ";
        if (possible)
            cout << "YES";
        else
            cout << "NO";
        cout << endl;
	}

    return 0;
}

