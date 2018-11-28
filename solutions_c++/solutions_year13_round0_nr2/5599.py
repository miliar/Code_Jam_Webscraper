//
//  main.cpp
//  GCJ2013QAB
//
//  Created by Seki Inoue on 2013/04/13.
//
//

//
//  This code uses project templates developed by peroxyacyl.
//  https://github.com/peroxyacyl/gcj-xcode-template
//


#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;



const static string kProblemSet = "small";

int main(int argc, const char * argv[]) {
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );
	int T = 0;
    
	ifs >> T;
    
    for (int testCase = 0; testCase < T; testCase++) {
        int N, M;
        ifs >> N >> M;
        vector<vector<int> > lawn;
        vector<vector<int> > searched;
        
        for (int i = 0; i < N; i++) {
            vector<int> row;
            vector<int> se;
            for (int j = 0; j < M; j++) {
                int cell;
                ifs >> cell;
                row.push_back(cell);
                
                bool sf = false;
                if (cell == 2) {
                    sf = true;
                }
                
                se.push_back(sf);
            }
            lawn.push_back(row);
            searched.push_back(se);
        }
        
        for (int i = 0; i < N; i++) {
            bool col = true;
            for (int j = 0; j < M; j++) {
                col &= (lawn[i][j] == 1);
            }
            if (col) {
                for (int j = 0; j < M; j++) {
                    searched[i][j] = 1;
                }
            }
        }
        
        for (int i = 0; i < M; i++) {
            bool row = true;
            for (int j = 0; j < N; j++) {
                row &= (lawn[j][i] == 1);
            }
            if (row) {
                for (int j = 0; j < N; j++) {
                    searched[j][i] = 1;
                }
            }
        }
        
        bool yes = true;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (searched[i][j] == 0) {
                    yes = false;
                    break;
                }
            }
            if (!yes) {
                break;
            }
        }
        
        
        string result = (yes)?"YES":"NO";
        
        cout << "Case #" << testCase+1 << ": " << result << endl;
        ofs << "Case #" << testCase+1 << ": " << result << endl;
    }
    
	return 0;
}
