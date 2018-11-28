#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <string>
#include <math.h>

using namespace std;

int main() {
    string filename ("input_a");
    string line;
    ifstream file (filename);
    int k;

    //
    getline (file, line);
    k = stoi(line);

    for (int t = 0; t < k; t++) {   //for each test case
        int r, c;
        vector<string> grid;

        // parsing
        getline (file, line);
        for (int i = 0; i < line.size(); i++) {
            if (line[i] == ' ') {
                r = stoi(line.substr(0, i));
                c = stoi(line.substr(i + 1, line.size() - i - 1));
                break;
            }
        }

        for (int i = 0; i < r; i++) {
            getline (file, line);
            grid.push_back(line);
        }

        // main
        int res = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == '.') continue;

                int above = 0;                                                                                        
                int below = 0;                                                                                        
                int left = 0;                                                                                         
                int right = 0;                                                                                        
                                                                                                                      
                for (int n = 0; n < i; n++) {                                                                         
                    if (grid[n][j] != '.') above++;                                                                   
                }                                                                                                     

                for (int n = i+1; n < r; n++) {
                    if (grid[n][j] != '.') below++;
                }

                for (int n = 0; n < j; n++) {
                    if (grid[i][n] != '.') left++;
                }

                for (int n = j+1; n < c; n++) {
                    if (grid[i][n] != '.') right++;
                }

                if (above + below + left + right == 0) res = -1;
                else if (grid[i][j] == '^' && above == 0) res++;
                else if (grid[i][j] == '<' && left == 0) res++;
                else if (grid[i][j] == '>' && right == 0) res++;
                else if (grid[i][j] == 'v' && below == 0) res++;
            }
            if (res == -1) break;
        }

        if (res == -1)
            cout << "Case #" << t+1 << ": IMPOSSIBLE" << "\r\n";
        else
            cout << "Case #" << t+1 << ": " << res << "\r\n";
    }
    return 0;
}