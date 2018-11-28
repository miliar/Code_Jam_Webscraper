/*
 ID: sarahwo1
 PROG: humble
 LANG: C++
 */
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <cctype>
#include <streambuf>
#include <string>
#include <sstream>
#include <cmath>
#include <stack>
//#include <queue>
#include <ctime>
#include <time.h>
#include <iomanip>
#include <set>

using namespace std;
#define INF (2147483630);

int grid1[4][4]; //row, col
int grid2[4][4];



int main()
{
    ofstream cout("/Users/sarahwooders/Desktop/money.txt");
    ifstream cin("/Users/sarahwooders/Desktop/text.txt");
    
    int cases;
    cin >> cases;
    
    for(int i = 0; i < cases; i ++)
    {
        vector<int> poss1;
        vector<int> poss2;
        vector<int> ans;
        int row1;
        int row2;
        
        cin >> row1;
        row1 --;
        for(int a = 0; a < 4; a ++) for(int b = 0; b < 4; b ++) cin >> grid1[a][b];
        cin >> row2;
        row2 --;
        for(int a = 0; a < 4; a ++) for(int b = 0; b < 4; b ++) cin >> grid2[a][b];
        
        for(int j = 0; j < 4; j ++) poss1.push_back(grid1[row1][j]);
        for(int j = 0; j < 4; j ++) poss2.push_back(grid2[row2][j]);
        
        for(int a = 0; a < 4; a ++)
        {
            int x = poss1[a];
            bool found = false;
            for(int b = 0; b < 4; b ++)
            {
                if(poss2[b] == x) found = true;
            }
            if(found) ans.push_back(x);
        }
        
        if(ans.empty()) cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
        else if(ans.size() == 1) cout << "Case #" << i + 1 << ": " << ans[0] << endl;
        else cout << "Case #" << i + 1 << ": Bad magician!" << endl;
        
        
    }
    
}

