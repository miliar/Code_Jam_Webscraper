
#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct Grass
{
	int m_row;
	int m_col;
	int m_h;
};


void DebugLawn(int *pLawn, int row, int col)
{
	int i, j, idx;
	for (i = 0; i < row; i++)
	{
		for (j = 0; j < col; j++)
		{
			idx = i * col + j;
			printf("%d", pLawn[idx]);
		}
		printf("\n");
	}
}


bool CreateLawn(int *pLawn, int row, int col)
{
	int i, j, idx;
	int *pStartLawn = new int[row * col];
	for (i = 0; i < row; i++)
	{
		for (j = 0; j < col; j++)
		{
			idx = i * col + j;
			pStartLawn[idx] = 0;
		}
	}

	map<int, vector<struct Grass>, greater<int> > grass_db;
	map<int, vector<struct Grass>, greater<int> >::iterator grass_it;
	for (i = 0; i < row; i++)
	{
		for (j = 0; j < col; j++)
		{
			idx = i * col + j;
			struct Grass grass;
			grass.m_row = i;
			grass.m_col = j;
			grass.m_h = pLawn[idx];
			grass_it = grass_db.find(grass.m_h);
			if (grass_it == grass_db.end())
			{
				vector<struct Grass> grass_arr;
				grass_arr.push_back(grass);
				grass_db.insert(pair<int, vector<struct Grass> >(grass.m_h, grass_arr));
			}
			else
			{
				grass_it->second.push_back(grass);
			}
		}
	}

	bool bCreateOk = true;
	grass_it = grass_db.begin();
	while (grass_it != grass_db.end() && bCreateOk)
	{
		int grass_h = grass_it->first;
		for (i = 0; i < grass_it->second.size() && bCreateOk; i++)
		{
			int grass_ok = false;
			int grass_row = grass_it->second[i].m_row;
			int grass_col = grass_it->second[i].m_col;

			for (j = 0; j < col; j++)
			{
				idx = grass_row * col + j;
				if (pStartLawn[idx] > grass_h)
					break;
			}
			if (j >= col)
				grass_ok = true;

			for (j = 0; j < row && !grass_ok; j++)
			{
				idx = j * col + grass_col;
				if (pStartLawn[idx] > grass_h)
					break;
			}
			if (j >= row)
				grass_ok = true;

			if (grass_ok)
			{
				idx = grass_row * col + grass_col;
				pStartLawn[idx] = grass_h;
			}
			else
				bCreateOk = false;
		}

		grass_it++;
	}

	delete[] pStartLawn;
	return bCreateOk;
}


int main(int argc, char *argv[])
{
	int i, j, nCaseCnt;

	scanf("%d", &nCaseCnt);
	for (i = 0; i < nCaseCnt; i++)
	{
		int row, col, idx;
		scanf("%d %d", &row, &col);

		int *pLawn = new int[row * col];
		for (idx = 0; idx < row * col; idx++)
			scanf("%d", pLawn + idx);

		bool bCreateOk = CreateLawn(pLawn, row, col);
		if (bCreateOk)
			printf("Case #%d: YES\n", i+1);
		else
			printf("Case #%d: NO\n", i+1);
	}

	return 0;
}
