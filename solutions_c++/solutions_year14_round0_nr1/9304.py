/*
ID: enggi231
LANG: C++
PROG: 
 */

#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>

#define ll long long

using namespace std;

fstream out;
int t, a, b, arr[4][4][2];
int histo[17];

vector<int> ans;


int main()
{
	cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> a;
        for (int y = 0; y < 4; y++)
            for (int x = 0; x < 4; x++)
                cin >> arr[x][y][0];
        cin >> b;
        for (int y = 0; y < 4; y++)
            for (int x = 0; x < 4; x++)
                cin >> arr[x][y][1];
        for (int j =0;j <= 16; j++)
            histo[j] = 0;
        
        for (int j = 0; j < 4; j++)
            histo[arr[j][a-1][0]]++;
        for (int j = 0; j < 4; j++)
            histo[arr[j][b-1][1]]++;
       
        ans.clear();
        for (int j = 1; j <= 16; j++)
            if (histo[j] > 1)
                ans.push_back(j);
        if (ans.size() == 0)
            cout << "Case #" << i <<": Volunteer cheated!" <<endl;
        if (ans.size() == 1)
            cout  << "Case #" << i <<": "<<ans[0] <<endl;
        if (ans.size() > 1)
            cout  << "Case #" << i <<": Bad magician!" <<endl;
        
    }
    
	return 0;
}

