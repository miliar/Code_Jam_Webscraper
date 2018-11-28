#include <vector>
#include <iostream>
using namespace std;

void print_args(){}

template <typename T, typename... Args>
void print_args(const T & val, Args... args)
{
	cout << val << " ";
	print_args(args...);
}

template <typename... Args>
void print_case(int test_case, Args... args)
{
	cout << "Case #" << test_case << ": ";
	print_args(args...);
	cout << endl;
}

enum DIR
{
	DOWN = 0,
	LEFT = 1,
	UP = 2,
	RIGHT = 3
};

pair<int,int> DIRECTIONS[4] = {
	make_pair(-1,0),
	make_pair(0,-1),
	make_pair(1,0),
	make_pair(0,1) };

int w, h;

bool dfs(vector<vector<bool>> & grid, DIR dir, int y, int x)
{
	if( y < 0 || y >= h-1 || x < 0 || x >= w )
		return false;
	if( !grid[y][x] )
		return false;
	grid[y][x] = false;
	if( y == 0 )
		return true;
	for(int inc = 0; inc < 3; inc++)
	{
		DIR new_dir = (DIR) (((dir+1)-inc+4) % 4);
		if( dfs(grid, new_dir, y + DIRECTIONS[new_dir].first, x + DIRECTIONS[new_dir].second) )
			return true;
	}
	return false;
}

int main()
{
	int num_cases;
	cin >> num_cases;
	for(int c = 0; c < num_cases; c++)
	{
		int num_b;
		cin >> w >> h >> num_b;
		vector<vector<bool>> grid(h, vector<bool>(w, true));
		for(int n = 0; n < num_b; n++)
		{
			int x0, y0, x1, y1;
			cin >> x0 >> y0 >> x1 >> y1;
			for(int x = x0; x <= x1; x++)
				for(int y = y0; y <= y1; y++)
					grid[y][x] = false;
		}

		int ans = 0;
		for(int x = 0; x < w; x++)
		{
			if( grid[h-1][x] )
				ans += dfs(grid, DOWN, h-2, x);
		}
		print_case(c+1, ans);
	}
	return 0;
}
