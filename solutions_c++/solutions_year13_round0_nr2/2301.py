
#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;

int nextInt() {
	int res;
	scanf("%d", &res);
	return res;
}

int main() {
	int tst = nextInt();
	for (int cas = 0; cas < tst; ++cas) {
		int rows = nextInt();
		int cols = nextInt();
		vector<vector<int> > height(rows, vector<int>(cols));
		for (int row = 0; row < rows; ++row)
			for (int col = 0; col < cols; ++col) {
				height[row][col] = nextInt();
				assert(height[row][col] == 1 || height[row][col] == 2);
			}
		bool res = true;
		for (int row = 0; row < rows; ++row)
			for (int col = 0; col < cols; ++col) {
				if (height[row][col] == 1) {
					bool okayRow = true;
					bool okayCol = true;
					for (int col2 = 0; col2 < cols; ++col2) 
						if (height[row][col2] == 2)
							okayCol = false;
					for (int row2 = 0; row2 < rows; ++row2) 
						if (height[row2][col] == 2)
							okayRow = false;
					if (!okayRow && !okayCol)
						res = false;
				}
			}
		printf("Case #%d: %s\n", cas + 1, res == true ? "YES" : "NO");
	}
	return 0;
}