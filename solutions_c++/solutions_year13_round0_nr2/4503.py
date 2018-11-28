#include <iostream>
#include <vector>

std::vector<std::vector<int> > grassHeight;
std::vector<int> largestRow;
std::vector<int> largestCol;
std::string result;

void trimGrass()
{
	grassHeight.clear();
	largestRow.clear();
	largestCol.clear();

	int n, m, temp;
	std::cin >> n >> m;

	grassHeight.resize(n);
	largestRow.resize(n);
	largestCol.resize(m);
	for(int i = 0; i < n; i++)
	{
		grassHeight[i].resize(m);

		for(int j = 0; j < m; j++)
		{
			std::cin >> temp;
			grassHeight[i][j] = temp;
		}
	}

	int row;
	for(int i = 0; i < n; i++)
	{
		row = grassHeight[i][0];
		for(int j = 1; j < m; j++)
		{
			if(grassHeight[i][j] > row)
				row = grassHeight[i][j];
		}
		largestRow[i] = row;
	}

	int col;
	for(int j = 0; j < m; j++)
	{
		col = grassHeight[0][j];
		for(int i = 1; i < n; i++)
		{
			if(grassHeight[i][j] > col)
				col = grassHeight[i][j];
		}
		largestCol[j] = col;
	}

}

bool check()
{
	for(int i = 0; i < grassHeight.size(); i++)
	{
		for(int j = 0; j < grassHeight[0].size(); j++)
		{
			if(grassHeight[i][j] < largestRow[i] && grassHeight[i][j] < largestCol[j])
			{
				return false;
			}
		}
	}

	return true;
}

int main()
{
	int numCases;
	std::cin >> numCases;
	std::cin.get();

	for(int i = 0; i < numCases; i++)
	{
		trimGrass();
		
		std::string s = (check()) ? "YES" : "NO";
		std::cout << "Case #" << (i + 1) << ": " << s.c_str() << std::endl;
	}

	return 0;
}