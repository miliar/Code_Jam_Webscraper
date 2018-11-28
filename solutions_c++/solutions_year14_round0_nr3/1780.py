#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#include <sstream>
#include <boost/smart_ptr/scoped_array.hpp>
using namespace std;
ifstream fin("C-small-attempt0.in");
ofstream fout("output.txt");

typedef pair<int, int> PI;

std::string f(const int r, const int c, const int m)
{
	const int size = r * c;
	boost::scoped_array<bool> field_line(new bool[size]);
	memset(field_line.get(), 0, sizeof(bool) * size);
	boost::scoped_array<bool*> field(new bool*[r]);
	for(int i = 0; i < r; ++i) field[i] = field_line.get() + c * i;

	for(int i = 0; i < m; ++i) field_line[i] = true;
	sort(field_line.get(), field_line.get() + size);

	boost::scoped_array<bool> dfs_line(new bool[size]);
	boost::scoped_array<bool*> dfs(new bool*[r]);
	for(int i = 0; i < r; ++i) dfs[i] = dfs_line.get() + c * i;

	queue<PI> q;

	do
	{
		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j)
			{
				if(!field[i][j])
				{
					q.push(PI(i, j));
					memset(dfs_line.get(), 0, size * sizeof(bool));
					while(!q.empty())
					{
						PI cur = q.front();
						q.pop();
						dfs[cur.first][cur.second] = true;
						int count = 0;
						for(int x = -1; x <= 1; ++x)
						{
							if(cur.first + x < 0 || cur.first + x >= r) continue;
							for(int y = -1; y <= 1; ++y)
							{
								if(x == 0 && y == 0) continue;
								if(cur.second + y < 0 || cur.second + y >= c) continue;
								if(field[cur.first + x][cur.second + y]) count++;
							}
						}
						if(count == 0)
						{
							for(int x = -1; x <= 1; ++x)
							{
								if(cur.first + x < 0 || cur.first + x >= r) continue;
								for(int y = -1; y <= 1; ++y)
								{
									if(cur.second + y < 0 || cur.second + y >= c) continue;
									if(!dfs[cur.first + x][cur.second + y])
									{
										q.push(PI(cur.first + x, cur.second + y));
									}
								}
							}
						}
					}

					bool ok = true;

					for(int x = 0; x < r && ok; ++x)
					{
						for(int y = 0; y < c && ok; ++y)
						{
							if(!field[x][y] && !dfs[x][y]) ok = false;
						}
					}
					if(ok)
					{
						ostringstream os;
						for(int x = 0; x < r; ++x)
						{
							for(int y = 0; y < c; ++y)
							{
								if(x == i && y == j) os << 'c';
								else if(field[x][y]) os << '*';
								else os << '.';
							}
							os << '\n';
						}
						return os.str();
					}
				}
			}
		}
	} while(next_permutation(field_line.get(), field_line.get() + size));

	return "Impossible\n";
}

int main()
{
	int T;
	fin >> T;
	for(int i = 1; i <= T; ++i)
	{
		int r, c, m;
		fin >> r >> c >> m;
		fout << "Case #" << i << ":\n" << f(r, c, m);
	}
}
