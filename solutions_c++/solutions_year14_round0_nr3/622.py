#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void print(const vector< vector<char> >& grid) {
    for (int r = 0; r < grid.size(); ++r) {
	for (int c = 0; c < grid[r].size(); ++c) {
	    cout << grid[r][c];
	}
	cout << endl;
    }
}

int main(int argc, char *argv[])
{
    ifstream in(argv[1]);
    int n;
    in >> n;

    for (int i = 1; i <= n; ++i) {
	int R, C, M;
	in >> R >> C >> M;

//	cout << R << " " << C << " " << M << endl;

	vector< vector<char> > grid(R, vector<char> (C, '*'));
	grid[R - 1][C - 1] = 'c';

	int size = R * C;
	if ((size - M) == 1) {
	    cout << "Case #" << i << ":" << endl;
	    print(grid);
	    continue;
	}

	if (R == 1) {
	    int c = 0;
	    while (M--) c++;
	    while (c != C - 1) grid[0][c++] = '.';
	    cout << "Case #" << i << ":" << endl;
	    print(grid);
	    continue;
	}

	if (C == 1) {
	    int r = 0;
	    while (M--) r++;
	    while (r != R - 1) grid[r++][0] = '.';
	    cout << "Case #" << i << ":" << endl;
	    print(grid);
	    continue;
	}
	
	int empty = size - M;
	if ((empty == 2) || (empty == 3) || (empty == 5) || (empty == 7)) {
	    cout << "Case #" << i << ":" << endl << "Impossible" << endl;
	    continue;
	}

	if (((C == 2) || (R == 2)) && (empty % 2)) {
	    cout << "Case #" << i << ":" << endl << "Impossible" << endl;
	    continue;
	}

	int x = empty / 2;
	if (x < C) {
	    if (empty % 2) {
		x--;
		grid[R - 3][C - 1] = grid[R - 3][C - 2] = grid[R - 3][C - 3] = '.';
	    }

	    for (int r = 0; r < x; ++r) {
		grid[R - 1][C - 1 - r] = '.';
		grid[R - 2][C - 1 - r] = '.';
	    }
	    grid[R - 1][C - 1] = 'c';
	    cout << "Case #" << i << ":" << endl;
	    print(grid);
	    continue;
	}

	if (x >= C) {
	    int newc = empty / C;
	    int r;
	    for (r = 0; r < newc; ++r) {
		for (int c = 0; c < C; ++c) {
		    grid[R - 1 - r][c] = '.';
		}
	    }
	    
	    if ((empty % C) > 1) {
		for (int c = 0; c < (empty % C); ++c) {
		    grid[R - 1 - r][c] = '.';
		}
	    }
	    else if ((empty % C) == 1) {
		if (r != 2) {
		    grid[R - 1 - r][0] = '.';
		    grid[R - 1 - r][1] = '.';
		    grid[R - r][C - 1] = '*';
		}
		else {
		    grid[R - 1 - r][0] = '.';
		    grid[R - 1 - r][1] = '.';
		    grid[R - 1 - r][2] = '.';
		    grid[R - r][C - 1] = '*';
		    grid[R - r + 1][C - 1] = '*';
		}
	    }

	    grid[R - 1][0] = 'c';
	    cout << "Case #" << i << ":" << endl;
	    print(grid);
	    continue;
	}
    }

    return 0;
}
