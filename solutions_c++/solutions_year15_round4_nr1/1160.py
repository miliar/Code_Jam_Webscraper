#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <unordered_map>

using namespace std;

template <class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cerr << "Case #" << caseNumber << endl;
    if (ans != -1) {
        cout << "Case #" << caseNumber << ": " << ans << endl;
    } else {
        cout << "Case #" << caseNumber << ": " << "IMPOSSIBLE" << endl;
    }
}

const int dx[4] = {0, 1, 0, -1 };
const int dy[4] = {-1, 0, 1, 0 };

int ArrowToDir(char arrow) {
    if (arrow == '^') {
        return 0;
    }
    if (arrow == '>') {
        return 1;
    }
    if (arrow == 'v') {
        return 2;
    }
    if (arrow == '<') {
        return 3;
    }
    return -1;
}

bool Walk(const vector<string>& field, int y, int x, int dir) {
    while (x > -1 && x < field[0].size() && y > -1 && y < field.size()) {
        x = x + dx[dir];
        y = y + dy[dir];
        if (x > -1 && x < field[0].size() && y > -1 && y < field.size()) {
            if (field[y][x] != '.') {
                return false;
            }
        }
    }
    return true;
}

int SolveTestCase() {
    int rows, cols;
    cin >> rows >> cols;
    vector<string> field(rows);
    string tmp;
    getline(cin, tmp);
    for (size_t i = 0; i < field.size(); i++) {
        getline(cin, field[i]);
    }
    bool possible = true;
    int ans = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (field[i][j] != '.') {
                int dir = ArrowToDir(field[i][j]);
                if (Walk(field, i, j, dir)) {
                    ans++;
                    bool flag = false;
                    for (int d = 0; d < 4; d++) {
                        flag = flag || !Walk(field, i, j, d);
                    }
                    if (!flag) {
                        possible = false;
                        break;
                    }
                }
                
            }
        }
    }
    if (!possible) {
        return -1;
    } else {
        return ans;
    }
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase() );

	return 0;
}