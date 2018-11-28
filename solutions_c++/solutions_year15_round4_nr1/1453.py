#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

#define min(x, y) (((x) < (y)) ? (x) : (y))
 
using namespace std;
int R, C;
char peggle[101][101];
bool direction[4];

void check_direction(int s_i, int s_j) {
    direction[0] = false;
    for (int i = s_i+1 ; i < R ; i++)
        if (peggle[i][s_j] != '.'){
            //cout << i << ", " << s_j << endl;
            direction[0] = true;
        }

    direction[1] = false;
    for (int i = s_i-1 ; i >= 0 ; i--)
        if (peggle[i][s_j] != '.'){
            //cout << i << ", " << s_j << endl;
            direction[1] = true;
        }

    direction[2] = false;
    for (int j = s_j+1 ; j < C ; j++)
        if (peggle[s_i][j] != '.') {
            //cout << s_i << ", " << j << endl;
            direction[2] = true;
        }
            

    direction[3] = false;
    for (int j = s_j-1 ; j >= 0 ; j--)
        if (peggle[s_i][j] != '.'){
            //cout << s_i << ", " << j << endl;
            direction[3] = true;
        }
}

bool check_match(int i, int j) {
    if (peggle[i][j] == 'v' && direction[0])
        return true;
    if (peggle[i][j] == '^' && direction[1])
        return true;
    if (peggle[i][j] == '>' && direction[2])
        return true;
    if (peggle[i][j] == '<' && direction[3])
        return true;
    return false;
}
 
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T;
    fin >> T;
     
    
    for (int t = 1 ; t <= T ; t++) {
        fin >> R >> C;
        for (int i = 0 ; i < R ; i++)
            for (int j = 0 ; j < C ; j++)
                fin >> peggle[i][j];

        bool possible = true;
        int answer = 0;
        for (int i = 0 ; i < R ; i++) {
            for (int j = 0 ; j < C ; j++) {
                if (peggle[i][j] != '.') {
                    check_direction(i, j);
                    if (!check_match(i, j))
                        answer++;
                    if (!direction[0] && !direction[1] && !direction[2] && !direction[3])
                        possible = false;
                }
            }
            if (possible == false)
                break;
        }

        if (possible)
            fout << "Case #" << t << ": " << answer << endl;       
        else
            fout << "Case #" << t << ": " << "IMPOSSIBLE" << endl; 
    }
}
