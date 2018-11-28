#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
 
using namespace std;
 
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int T;
    fin >> T;
     
    int N;
    int grid[100][50];
    for (int t = 1 ; t <= T; t++)
    {  
        fin >> N;
        for (int i = 0 ; i < 100 ; i++) {
            for (int j = 0 ; j < 50 ; j++)
                grid[i][j] = 0;
        }

        for (int i = 0 ; i < 2*N-1 ; i++) {
            for (int j = 0 ; j < N ; j++) {
                fin >> grid[i][j];
            }
        }

        vector<int> ans;
        /*
        // Figure out first colum+row
        int smallest = 2500;
        for (int i = 0 ; i < 2*N-1 ; i++) {
            for (int j = 0 ; j < N ; j++) {
                fin >> grid[i][j];
                if (j == 0) {
                    if (smallest > grid[i][j]) smallest = grid[i][j];
                }
            }
        }
        int count = 0; int s_1 = 0; int s_2 = 0;
        for (int i = 0 ; i < 2*N-1 ; i++) {
            if (grid[i][loop] == smallest) {
                count++;
                if (count == 1) {
                    s_1 = i;
                }
                if (count == 2) { 
                    s_2 = i;
                }
            }
        }
        int ans_c = 0;
        vector<int> ans;
        if (count == 1) {
            // Found Answer;
            for (int i = 0 ; i < 2*N-1 ; i++) {
                if (i == s_1) continue;
                bool add = true;
                for (int j = 0 ; j < N ; j++) {
                    if (used[j] == false && grid[i][0] == grid[s_i][j]) {
                        used[j] = true;
                        add = false;
                        break;
                    }
                }
                if (add) {
                    ans.push_back(grid[i][0]);
                    ans_c++;
                }
            }
            std::sort(ans.begin(), ans.end());
        }
        */

        int count_n[2501];
        for (int i = 1 ; i <= 2500 ; i++) {
            count_n[i] = 0;
        }
        for (int i = 0 ; i < 2*N-1 ; i++) {
            for (int j = 0 ; j < N ; j++) {
                count_n[grid[i][j]]++;
            }
        }
        for (int i = 1 ; i <= 2500 ; i++) {
            if (count_n[i] % 2 != 0)
                ans.push_back(i);
        } 
        std::sort(ans.begin(), ans.end());

        fout << "Case #" << t << ":";
        for (int i = 0 ; i < N ; i++) 
            fout << " " << ans[i];
        fout << endl;
        
    }
}
