#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<vector<char> > desk(4);

char pl[] = {'X', 'O'};

bool test(int x, int y, int dx, int dy, char c) 
{
    int count = 0;
    for (int i = 0; i < 4; ++i) {
        if (desk[x][y] == c || desk[x][y] == 'T') {
            ++count;
        }
        x += dx;
        y += dy;
    }
    return count == 4;
}

string solve() 
{
    int n, m;
    cin >> n >> m;
    vector<vector<int> > a(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }
    for (int w = 1; w <= 100; ++w) {
        vector<int> r1(n), r2(n);
        vector<int> c1(m), c2(m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (a[i][j] == w) {
                    ++r1[i];
                    ++c1[j];
                } else if (a[i][j] > w) {
                    ++r2[i];
                    ++c2[j];
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            if (r2[i] == 0 && r1[i] > 0) {
                for (int j = 0; j < m; ++j) {
                    if (a[i][j] == w) {
                        --c1[j];
                    }
                }
            }
        }

        for (int j = 0; j < m; ++j) {
            if (c2[j] != 0 && c1[j] > 0) {
                return "NO";
            }
        }
    }
    return "YES";
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
	return 0;
}

